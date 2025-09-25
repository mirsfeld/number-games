def square(n):
    return n*n

if __name__=='__main__':
    try:
        n = float(input("Enter number to square:"))
        print(square(n))
    except ValueError:
        print("Enter a valid number")