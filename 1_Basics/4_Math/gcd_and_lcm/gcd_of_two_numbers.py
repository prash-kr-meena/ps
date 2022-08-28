"""
TUF : https://takeuforward.org/data-structure/find-gcd-of-two-numbers/
GFG : https://www.geeksforgeeks.org/c-program-find-gcd-hcf-two-numbers/


Find GCD (HCF) of two numbers

GCD : Greatest Common Division
HCF : Highest Common Factor



Note : Python already has support for GCD in its math library   , We can pass as many number as we like in the gcd method
        we can assume that the internal gcd() method uses the  Euclidean’s theorem
        Whose time complexity comes to be   O(lg min(a,b))
"""
from math import gcd


def greatest_common_divisor__brute_force(a: int, b: int) -> int:
    """
    Brute force
    Time    : O( min(a,b) )
    Space   : O(1)
    """
    minimum = min(a, b)

    greatest_common_divisor_value = 1
    for i in range(2, minimum + 1):  # Starting from 2,     as 1 is always a factor of every number
        if a % i == 0 and b % i == 0:  # i  is a factor of both a and b
            greatest_common_divisor_value = i  # No need to find max,   As i will always be higher the last i's value

    return greatest_common_divisor_value


def greatest_common_divisor__brute_force_optimized(a: int, b: int) -> int:
    """
    Idea is exactly the same as of the brute force, the only difference is we are going to short circuit the logic
    Where in the normal brute force we are traversing from 1, to min(a,b)
    here if we traverse in the reverse direction ie from min(a,b) to 1
    Then the first common divisor will be our Greatest Common Divisor, and we would not need to travel completely till 1

    Note : The worst case time complexity still remains the same, as in the worst case we could have to travel till 1
    Time  : O(n)
    Space : O(1)
    """
    minimum = min(a, b)
    for i in range(minimum, 0, -1):  # going from minimum to 1  both inclusive
        if a % i == 0 and b % i == 0:  # i  is a factor of both a and b
            return i  # breaking the loop, if found

    return 1  # as 1 is factor of all the number


def greatest_common_divisor__euclidean_algorithm(dividend: int, divisor: int) -> int:
    """
    Euclidean algorithm is based on the long division method
    where
    we make our remainder as our divisor and
    our divisor as our dividend

    and we do this till the time we have our remainder as 0
    and when our remainder is 0, the divisor at the time is our answer, ie the GCD value

    YouTube :   https://www.youtube.com/watch?v=utZcJ0leZ_g
                GCD and LCM using Euclid's Algorithm With Applications | CP Course              Greatly Explained

    Time  : O(log min(a,b))
    Space : O(log min(a,b))     due to the recursive stack space
    """

    if divisor == 0:  # Edge case when divisor is 0, we can't divide by 0
        return dividend

    remainder = dividend % divisor
    if remainder == 0:  # Base Case
        return divisor
    return greatest_common_divisor__euclidean_algorithm(divisor, remainder)


if __name__ == '__main__':
    # we could also use a list of tuple
    nums_a = [0, 1, 2, 8, 10, 15, 40, 80]
    nums_b = [1, 0, 8, 16, 3, 80, 10, 40]
    for x, y in zip(nums_a, nums_b):
        print(f"({x:3},{y:3}) -> "
              f"\t{gcd(x, y):5}"
              f"\t{greatest_common_divisor__brute_force(x, y)}"
              f"\t{greatest_common_divisor__brute_force_optimized(x, y)}"
              f"\t{greatest_common_divisor__euclidean_algorithm(x, y)}")
