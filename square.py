def square(n):
    """
    Simple function to square a number

    Args:
        n (float): number to square

    Returns:
        float: square of n
    """
    return n*n

def main():
    try:
        n = float(input("Enter number to square:"))
        print(square(n))

    except ValueError:
        print("Please enter a valid number")

if __name__=='__main__':
    main()