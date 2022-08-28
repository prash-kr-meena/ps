"""
YouTube :   How to find GCD and LCM mathematically  https://www.youtube.com/watch?v=uwdGP2OaahI
GFG     :   https://www.geeksforgeeks.org/program-to-find-lcm-of-two-numbers/

Find LCM of two numbers
LCM : Lowest common multiple


Note : Python already has support for LCM in its math library,   We can pass as many number as we like in the lcm method
        we can assume that the internal gcd() method uses the  Euclidean’s theorem
        Whose time complexity comes to be   O(lg min(a,b))
"""
from math import gcd, lcm


def lowest_common_multiplier(a: int, b: int) -> int:
    """
    LCM =  ___a x b___
            gcd(a,b)

    Note : This above formula does not apply for number more than 2
    ie  LCM  !=  ___a x b x c___
                   gcd(a,b,c)

    GFG : LCM of given array elements https://www.geeksforgeeks.org/lcm-of-given-array-elements/
    """
    return a * b // gcd(a, b)


if __name__ == '__main__':
    # we could also use a list of tuple
    nums_a = [0, 1, 3, 8, 10, 15, 40, 89]
    nums_b = [1, 0, 8, 15, 3, 89, 10, 40]
    numb_c = [1, 0, 8, 15, 3, 89, 10, 40]

    print(f" {' ':3} {' ':3}   \t\t{'gcd':5}  \t{'lcm':3}  \t{'lowest_common_multiplier':3}")
    for x, y in zip(nums_a, nums_b):
        print(f"({x:3},{y:3}) -> \t{gcd(x, y):5}  \t{lcm(x, y):5}  \t{lowest_common_multiplier(x, y):5}")

    print()
    for x, y, z in zip(nums_a, nums_b, numb_c):
        print(f"({x:3},{y:3},{z:3} -> {gcd(x, y, z):5}  \t{lcm(x, y, z):5}")
