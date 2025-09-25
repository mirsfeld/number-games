import math 

def square(n):
    """
    Simple function to square a number

    Args:
        n (float): number to square

    Returns:
        float: square of n
    """
    return n*n

def pythagoras_triplets(upper_limit_z):
    results = []
    stopping_criterion = False
    for x in range(1,upper_limit_z+1):
        
        for y in range(x, upper_limit_z+1):
            
            z_square = square(x)+ square(y)
            z = math.sqrt(z_square)
            if z>upper_limit_z:
                break
            if z-int(z)==0:
                results.append((x,y,int(z)))
        
    return results


def main():
    try:
        n = int(input("Enter number to square:"))
        print(f"Square of {n}: {square(n)}")
        print(pythagoras_triplets(n))

    except ValueError:
        print("Please enter a valid number")

if __name__=='__main__':
    main()