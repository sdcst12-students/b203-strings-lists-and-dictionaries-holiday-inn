#!python3

'''
use a for loop to iterate through all possible integers to find the factors of 24
'''
def main():
    factors = []
    myNumber = 24
    for i in range(1,myNumber):
        if (myNumber/i)%1 == 0:
            factors.append(i)
    print(factors)


if __name__ == "__main__":
    main()