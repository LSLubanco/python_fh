'''
Check if an entered year is a leap year. The following rules must be observed:

not divisible by 4 -> no leap year
divisible by 4 -> leap year
divisible by 100 -> no leap year
divisible by 400 -> leap year
'''

def is_leap_year(year):
    if(year % 4 == 0 and year % 100 != 0)or(year % 400 == 0 ):
        print("It is a leap year")
        return True

    else:
        print("It is not a leap year")
        return False

def main():
    done = False
    while not done:
        while True:
            try:
                num = int(input("Enter a year to be checked: "))
                break
            except ValueError:
                print("Please enter an integer")
        is_leap_year(num)

        while True:
            user_input = input("Do you want try another year? (y/n) ")
            if (user_input.lower() == 'y' or user_input.lower() == 'n'):
                break
            else:
                print("please answer only with:\ny for yes\nn for no")

        if(user_input == 'n'):
            done = True
if __name__ == "__main__":
    main()
