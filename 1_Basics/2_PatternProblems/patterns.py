"""
Solve any Star Pattern program in Python : https://www.youtube.com/watch?v=fX64q6sYom0

^^ Show How by just combining the Square, Increasing and Decreasing Triangle Pattern
    We can solve almost all the pattern problems easily


"""


def square(size: int):
    """
    * * * * *
    * * * * *
    * * * * *
    * * * * *
    * * * * *

    """
    for row in range(0, size):
        for column in range(0, size):
            print("*", end=" ")
        print()

    print("\n")
    # for each row I will first print all the columns
    # then I will print the columns for the 2nd row
    # and so on


def right_angle_equilateral_triangle(size: int):
    """
    * ` ` ` `
    * * ` ` `
    * * * ` `
    * * * * `
    * * * * *


    After completing the diagram with the missing dots
    we can see that, we are on each row we are traversing we are INCREASING the number of columns to be printed

    for the 0th row the number of columns are 0+1 = 1
    for the 1st row ``   ``    ``    ``    `` 1+1 = 2

    and so on
    """

    for row in range(0, size):
        for column in range(0, row + 1):
            print("*", end=" ")
        print()

    print("\n")


def right_angle_equilateral_triangle__flipped_vertically(size: int):
    """
        * * * * *
        * * * * `
        * * * ` `
        * * ` ` `
        * ` ` ` `

        After completing the diagram with the missing dots
        we can see that, we are on each row we are traversing we are DECREASING the number of columns to be printed

        for the 0th row the number of columns are size-0 = size
        for the 1st row ``   ``    ``    ``    `` size-1 = size-1
        for the 2nd row ``   ``    ``    ``    `` size-2 = size-2

        and so on
        """

    for row in range(0, size):
        for column in range(0, size - row):
            print("*", end=" ")
        print()

    print("\n")

    pass


def right_angle_equilateral_triangle__with_number__increasing_column_wise(size: int):
    """
    Column Wise       Direction Left --> Right

    0 1 2 3 4
    | | | | |
    V V V V V

    1 ` ` ` `               <--     Row 1        Row Wise      Direction   Top --> Bottom
    1 2 ` ` `               <--     Row 2
    1 2 3 ` `               <--     Row 3
    1 2 3 4 `               <--     Row 4
    1 2 3 4 5               <--     Row 5




    After completing the diagram with the missing dots
    we can see that, we are on each row we are traversing we are increasing the number of columns to be printed
        as well as the value of the columns increase here

    for the 0th row the number of columns are 0+1 = 1       and the value is 0+1
    for the 1st row ``   ``    ``    ``    `` 1+1 = 2       and the value is 0+1  0+2
    for the 2nd row ``   ``    ``    ``    `` 2+1 = 3       and the value is 0+1  0+2  0+3

    and so on
    """

    # 0
    # 0 1
    # 0 1 2
    # 0 1 2 3
    # 0 1 2 3 4

    for row in range(0, size):
        for column in range(0, row + 1):  # The column value is increasing from 0 to row+1 value
            print(column, end=" ")
        print()
    print("\n")

    # The above starts from 0, we can start it from 1 to get our desired result
    for row in range(1, size + 1):
        for column in range(1, row + 1):  # The column value is increasing from 0 to row+1 value
            print(column, end=" ")
        print()

    print("\n")


def right_angle_equilateral_triangle__with_number__increasing_row_wise(size: int):
    """
     Column Wise       Direction Left --> Right

     0 1 2 3 4
     | | | | |
     V V V V V

     1 ` ` ` `               <--     Row 1        Row Wise      Direction   Top --> Bottom
     2 2 ` ` `               <--     Row 2
     3 3 3 ` `               <--     Row 3
     4 4 4 4 `               <--     Row 4
     5 5 5 5 5               <--     Row 5


     :param size:
     :return:

     After completing the diagram with the missing dots
     we can see that, we are on each row we are traversing we are increasing the number of columns to be printed
         BUT we the numbers in the columns are constant, Rather the numbers in the rows are incerasing

     for the 0th row the number of columns are 0+1 = 1       and the value is 0+1
     for the 1st row ``   ``    ``    ``    `` 1+1 = 2       and the value is 0+2  0+2
     for the 2nd row ``   ``    ``    ``    `` 2+1 = 3       and the value is 0+3  0+3  0+3

     and so on
     """

    # 0
    # 1 1
    # 2 2 2
    # 3 3 3 3
    # 4 4 4 4 4

    for row in range(0, size):
        for column in range(0, row + 1):  # The column value is increasing from 0 to row+1 value
            print(row, end=" ")
        print()
    print("\n")

    # The above starts from 0, we can start it from 1 to get our desired result
    for row in range(1, size + 1):
        for column in range(1, row + 1):  # The column value is increasing from 0 to row+1 value
            print(row, end=" ")
        print()

    # Note :  We only needed to print the values of row instead of columns, compared to the above solution
    print("\n")

    pass


def pyramid_pattern(size):
    """
    - - - - * ` ` ` `         row size = 5
    - - - * * * ` ` `
    - - * * * * * ` `
    - * * * * * * * `
    * * * * * * * * *

    Note: This can be seen as combination of
     1. one decreasing triangle of spaces  of 1 less size
     2. one increasing triangle of *
     3. one increasing triangle of *       of 1 less size

    """
    for row in range(0, size):
        small_triangle_size = size - 1

        # printing - decreasing triangle of spaces      of 1 less size
        for column in range(0, small_triangle_size - row):
            print(" ", end=" ")

        # printing - increasing triangle of *
        for column in range(0, row + 1):
            print("*", end=" ")

        # printing - increasing triangle of *           of 1 less size
        for column in range(0, row):
            print("*", end=" ")

        print()


#        Thought : If we were given this pattern as a matrix, we could have just easily done a Transpose of the matrix
#                    to find our solution
#        * ` ` ` `                     * ` ` ` `
#        * * ` ` `                     * * ` ` `
#        * * * ` `   ---> Transpose    * * * ` `
#        * * * * `                     * * * * `
#        * * * * *                     * * * * *


if __name__ == '__main__':
    n = 30
    square(n)
    right_angle_equilateral_triangle(n)
    right_angle_equilateral_triangle__flipped_vertically(n)
    right_angle_equilateral_triangle__with_number__increasing_column_wise(n)
    right_angle_equilateral_triangle__with_number__increasing_row_wise(n)

    pyramid_pattern(n)
