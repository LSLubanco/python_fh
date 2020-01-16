'''
Function that receives the numerator and denominator of two fractions
and it outputs the sum of the two fractions

Additional task: Simplify the result. The easiest way
to do this is to divide the numerator and denominator by their largest common divisor.
'''
import math #for gcd
def find_lowest(num,den):
    return [int(num/math.gcd(num,den)),int(den/math.gcd(num,den))]
def add_fractions(n1 = [],n2 =[]):
    num1,den1 = [n1[0],n1[1]]
    num2,den2 = [n2[0],n2[1]]
    #Least common multiplier times greates common divisor is used for finding
    #the new denominator

    den_output =int( (den1*den2) / math.gcd(den1,den2) )
    #finding the numerator
    num_output = int( num1*(den_output/den1) + (num2)*(den_output/den2) )

    #Simplifying the result
    [num_output,den_output] = find_lowest(num_output,den_output)

    return [num_output,den_output]


def main():
    #ask user to define fractions to be added
    n1 = list(int(num) for num in input\
    ("Enter the numerator and denominator of the first fraction separated by space: ").strip().split())[:2]
    n2 = list(int(num) for num in input\
    ("Enter the numerator and denominator of the second fraction separated by space: ").strip().split())[:2]
    [a,b] = add_fractions(n1,n2)
    print("Numerator output {}".format(a))
    print("Denominator output {}".format(b))
if __name__ == "__main__":
    main()
