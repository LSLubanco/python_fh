import numpy as np

def create_and_save_arr(n):
    arr = np.random.randn(n)
    np.savetxt('data.csv', arr, delimiter=',')
    np.save("data_np.npy", arr)

def calculate_npy(file_name):
    arr_np = np.load(file_name)
    print("\nThe mean using npy extension is: {}".format(arr_np.mean()))
    print("\nThe variance using npy extension is: {}".format(arr_np.var()))
    print("\nThe standard deviation using npy extension is: {}".format(arr_np.std()))

def calculate_csv(file_name):
    arr_csv = np.genfromtxt(file_name, delimiter=',')
    print("\nThe mean using csv extension is: {}".format(arr_csv.mean()))
    print("\nThe variance using csv extension is: {}".format(arr_csv.var()))
    print("\nThe standard deviation using csv extension is: {}".format(arr_csv.std()))
def compare_results(file_csv,file_npy):
    arr_csv = np.genfromtxt(file_csv, delimiter=',')
    arr_npy = np.load(file_npy)
    if(arr_csv.mean() ==arr_npy.mean() and arr_csv.var() == arr_npy.var() and arr_csv.std() == arr_npy.std()):
        print("\nSame results were obtained")
        return True
    else:
        print("\nDifferent results were obtained")
        return False

def main():
    create_and_save_arr(1000)
    calculate_npy('data_np.npy')
    calculate_csv('data.csv')
    compare_results('data.csv','data_np.npy')

if __name__ == "__main__":
    main()
