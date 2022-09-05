from typing import List
from Utils.Array import input_array


def get_filled_matrix(row_size, col_size, fill=0):
    return [[fill for _ in range(col_size)] for _ in range(row_size)]


def input_matrix(prompt="arr : ") -> List[List[int]]:
    """
    Jagged Array Is Possible : https://en.wikipedia.org/wiki/Jagged_array
    Notice : you need to be careful, on the no of columns you are putting
    """
    row = int(input("rows :"))

    matrix = []
    for _ in range(row):
        row = input_array(prompt)
        matrix.append(row)
    return matrix


def input_character_matrix() -> List[List[str]]:
    """
    Jagged Array Is Possible : https://en.wikipedia.org/wiki/Jagged_array
    Notice : you need to be careful, on the no of columns you are putting
    """
    row = int(input("row :"))

    matrix = []
    for _ in range(row):
        row = list(input().strip().split())
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(row)


def print_matrix_beautiful(matrix):
    for row in matrix:
        for e in row:
            print(e, end=" ")
        print()


if __name__ == "__main__":
    print_matrix(get_filled_matrix(3, 10, 8))

    arr2D = [[16, 28, 60, 64],
             [22, 41, 63, 91],
             [27, 50, 87, 93],
             [36, 78, 87, 94]]

    print_matrix(arr2D)
    print_matrix_beautiful(arr2D)

    arr2D = input_matrix()
    print(arr2D)
