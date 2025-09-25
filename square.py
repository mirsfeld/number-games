import math 
import sys

def square(n):
    """
    Simple function to square a number

    Args:
        n (float): number to square

    Returns:
        float: square of n
    """
    return n*n

def check_taxicab_number(tc_candidate):
    if tc_candidate<1729:
        return False, None
    else:
        base_1, base_2 = -1, -1
        for i in range(1,tc_candidate):
            cube_1 = i**3
            if cube_1>tc_candidate:
                break
            candidate_base_2 = round((tc_candidate-cube_1)**(1/3))
            if cube_1 + candidate_base_2**3 == tc_candidate:
                base_1 = i
                base_2 = int(candidate_base_2)
                break
        if min(base_1, base_2)<1:
            return False, None
        base_3, base_4 = -1, -1
        for i in range(min(base_1, base_2),tc_candidate):
            if i==base_1 or i==base_2:
                continue
            cube_3 = i**3

            if cube_3>tc_candidate:
                break
            candidate_base_4 = round((tc_candidate-cube_3)**(1/3))
            if cube_3 + candidate_base_4**3 == tc_candidate:
                base_3 = i
                base_4 = int(candidate_base_4)
                break
        if min(base_3, base_4)<1:
            return False, None
        else:
            print([(base_1, base_2), (base_3, base_4)])
            return True, [(base_1, base_2), (base_3, base_4)]
        
def taxicab_numbers(num_tc_numbers):
    try:
        counter = 0
        tc_candidate = 1729
        results = {

        }
        while counter<num_tc_numbers:
            tc_results = check_taxicab_number(tc_candidate)
            if tc_results[0]:
                results[tc_candidate] = tc_results[1]
                counter += 1
            tc_candidate += 1
        return results

    except ValueError:
        print("Please enter a valid number (positive integer)")

def pythagorean_triplets(upper_limit_z):
    """
    Compute pythagorean triplets.

    Args:
        upper_limit_z (int): upper limit for z value (as stopping criterion)

    Returns:
        list[tuple]: solution triplets (x,y,z) 
    """
    results = []
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
        n = int(sys.argv[1])
        if n<1:
            raise ValueError
        print(f"Square of {n}: {square(n)}")
        
        triplets = pythagorean_triplets(n)
        print("Pythagorean triplets (x,y,z):")
        for (x,y,z) in triplets:
            print(f"({x},{y},{z}): {x**2} + {y**2} = {z**2}")
        
        num_taxicab_numbers = int(sys.argv[2])
        results_tc = taxicab_numbers(num_taxicab_numbers)
        print(f"First {num_taxicab_numbers} taxicab numbers:")
        for key, value in results_tc.items():
            x_1, y_1 = value[0]
            x_2, y_2 = value[1]
            print(f"{key} = {x_1}^3 + {y_1}^3 = {x_2}^3 + {y_2}^3")
        

        

    except ValueError:
        print("Please enter a valid number")

if __name__=='__main__':
    main()