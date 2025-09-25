import math 
import sys
import time
import numpy as np

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

def pythagorean_triplets_lists(limit):
    results = []
    nums = list(range(1, limit+1))
    squares = square_list(nums)
    added_squares = add_list(squares, squares)
    for key, value in added_squares.items():
        if value in squares:
            results.append((int(key[0]**(0.5)), int(key[1]**(0.5)), np.where(np.array(nums)**2==value)[0][0]+1))
    return results


def square_list(int_list):
    return [x**2 for x in int_list]

def add_list(list1, list2):
    dictionary = {}
    for x1 in list1:
        for x2 in list2:
            dictionary[(x1, x2)] = x1+x2
    return dictionary


def main():
    try:
        n = int(sys.argv[1])
        if n<1:
            raise ValueError
        print()
        print(f"Square of {n}: {square(n)}")
        print("#"*10)
        start_time = time.time()
        triplets = pythagorean_triplets(n)
        end_time = time.time()
        print(end_time-start_time)
        start_time = time.time()
        triplets = pythagorean_triplets_lists(n)
        end_time = time.time()
        print("alternative:", end_time-start_time)
        print()
        print("Pythagorean triplets (x,y,z):")
        for (x,y,z) in triplets:
            print(f"({x},{y},{z}): {x**2} + {y**2} = {z**2}")
        print("#"*10)
        
        print()
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