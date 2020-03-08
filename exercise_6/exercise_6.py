import numpy as np
import pandas as pd
import matplotlib.pyplot as  plt
from scipy.fftpack import rfft, irfft, fftfreq,fft


# My first estimate is that it is approximattely k = 1000 the period
# where k is the month accumulator, so my conclusion initially
# is period T = 1000 mounths
def fft_on_data(y):
    N = len(y)
    print(len(y))
    #t = np.linspace(0,10,1000)
    dt=1
    #F = np.fft.fft(y)
    W = fftfreq(y.size,dt)
    #f_signal = rfft(y.to_numpy())
    f_signal = fft(y.to_numpy())
    plt.plot(W,np.abs(f_signal),'r')
    plt.xlabel("Frequency")
    plt.ylabel("Magnitude")
    plt.xlim(0,0.05) # plotting only relevant part from right axis

    plt.show()
    #plt.plot(F_2)
    #plt.show()
def main():
    headers = ['Months','Sunspots']
    df = pd.read_csv("sunspots.csv",  header=None, names=headers)

    x = df['Months']
    y = df['Sunspots']
    rows,=y.shape
    fft_on_data(y)

if __name__ == "__main__":
    main()


'''

**************************FINAL ANSWER************************
My initial conclusion was 100 months was the period T.

However after performing the fft, the peak is found at : f = 0.0077
Thus the period T is approximatelly 129.87 months which is equal to:
    10,82 Years

The real frequency was not so far from the initial guess. However,
it must be noted that the inital guess was very rough and very uncertain.

Therefore, the conclusion is that the fft allowed to visualize
the frequency in a signal which visually was very difficult to define
a pattern with high certainty.

'''
