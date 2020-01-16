'''
Ethiopian multiplication
Two numbers(integers) are given as input for multiplication
in each iteration the number on the left is truncated while the number
on the right is doubled

After the left side gets equal to 1
all lines which the left side is divisible by two is crossed output
and the right side of the remaining side is summed
the result of the sum is the multiplication
'''

def trunc(l1):
    return l1//2
def pair_idx(n1):
    idx = []
    for i in range(0,len(n1)):
        if n1[i] % 2 != 0:
            idx.append(i)
    return idx
def left_sum(l2, l = []):
    total_sum = 0
    for i in range(0,len(l2)):
        #print(l2[i])
        if i in l:
            total_sum += l2[i]
    return total_sum
def ethiopian(num_for_mult):
    [n1,n2] = num_for_mult
    if(n1 == 0 or  n2 == 0):
        return 0
    else:
        #create a list with the vlaues of n1 and n2
        l1 = [n1]
        l2 = [n2]
        while(n1>1):
            n1 = trunc(n1)
            l1.append(n1)
            n2 = n2*2
            l2.append(n2)
        #print(l1)
        #print(l2)
        index = pair_idx(l1)
        #print(index)
        total_sum = left_sum(l2,index)
        return total_sum
def main():
    print("Welcome to the Ethiopian Multiplication\n\n")
    #ask user to define fractions to be added
    while True:
        num_for_mult = list(int(num) for num in input\
        ("Enter the first and second number separated by space: ").strip().split())
        if (len(num_for_mult) == 2):
            #print("Here")
            #print(len(num_for_mult))
            break
        else:
            print("Please pass only two numbers separated by space for the multiplication")
    total = ethiopian(num_for_mult)
    print("The result of the multiplication of {} and {} is = {}".format(num_for_mult[0],num_for_mult[1],total))
if __name__ == "__main__":
    main()
