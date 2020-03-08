import numpy as np
import pandas as pd
import matplotlib.pyplot as  plt


#First part of the exercise
def first_and_second(x,y,df):
    plt.plot(x,y)
    plt.xlabel('Months')
    plt.ylabel('Sunspots')
    plt.axis('tight')
    plt.title('Months x Sunspots')
    plt.show()

    #Second - using insets and only first thousand datapoints
    x_short = df['Months'][0:1000]

    y_short = df['Sunspots'][0:1000]

    fig = plt.figure()
    axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
    axes2 = fig.add_axes([0.6,0.6,0.3,0.2])
    axes1.plot(x_short,y_short,'r')
    axes1.set_xlabel('Months')
    axes1.set_ylabel('Sunspots')
    axes1.set_title('Months x Sunspots [First 1000 Samples]')
    axes2.plot(x,y)
    axes2.set_xlabel('Months')
    axes2.set_ylabel('Sunspots')
    axes2.set_title('Months x Sunspots')
    plt.show()

# Third part -- Move average filter

def move_avg(data,radius):
    row,=data.shape
    new_y_size = row-radius*2
    new_y = np.zeros(new_y_size)
    k = 0
    for idx,element in enumerate(data):
        #print(idx)
        if (idx > (radius-1)) and (idx < (row-radius)):
            #print("Here")
            new_y[k]=np.average(data[idx-radius:idx+radius])
            k +=1
    return new_y,new_y_size
def plot_handler(data0,t0,data1,t1,data2,t2,data3,t3):
    fig,axes = plt.subplots(4,1,figsize=(8,4))
    fig.tight_layout()
    axes[0].plot(np.arange(0,t0),data0)
    axes[0].set_title("Original Plot",loc='left')
    axes[0].set_xlabel('Months')
    axes[0].set_ylabel('Sunspots')
    axes[1].plot(np.arange(0,t1),data1,'k')
    axes[1].set_title("Radius = 5",loc='left')
    axes[1].set_xlabel('Months')
    axes[1].set_ylabel('Sunspots')
    axes[2].plot(np.arange(0,t2),data2,'r')
    axes[2].set_xlabel('Months')
    axes[2].set_ylabel('Sunspots')
    axes[2].set_title("Radius = 50",loc='left')
    axes[3].plot(np.arange(0,t3),data3,'m')
    axes[3].set_title("Radius = 100",loc='left')
    axes[3].set_xlabel('Months')
    axes[3].set_ylabel('Sunspots')
    plt.show()


def main():
    headers = ['Months','Sunspots']
    df = pd.read_csv("sunspots.csv",  header=None, names=headers)

    x = df['Months']
    y = df['Sunspots']
    first_and_second(x,y,df)
    rows,=y.shape
    d1,t1 = move_avg(y,5)
    d2,t2 = move_avg(y,50)
    d3,t3 = move_avg(y,100)
    plot_handler(y,rows,d1,t1,d2,t2,d3,t3)
    print(d1.shape)
    print(t1)
if __name__ == "__main__":
    main()
