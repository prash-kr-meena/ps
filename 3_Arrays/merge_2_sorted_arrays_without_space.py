from typing import List


def merge_2_sorted_arrays(arr: List[int], brr: List[int]):
    """
    Time : O(n + m)
    Space: O(n + m)
    """
    crr = []  # size will increase as we append more elements to it, and eventually     size_c = size_a + size_b
    a = b = 0  # pointers in array A and B

    while a < len(arr) and b < len(brr):  # while either one of them is exhausted
        if arr[a] < brr[b]:
            crr.append(arr[a])
            a += 1
        else:
            crr.append(brr[b])
            b += 1

    while a < len(arr):  # if B is exhausted then put all the elements of A
        crr.append(arr[a])
        a += 1

    while b < len(brr):  # if A is exhausted then put all the elements of B
        crr.append(brr[b])
        b += 1

    return crr


if __name__ == '__main__':
    tuple_of_sorted_arrays = [
        (
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9]
        ),
        (
            [],
            [9, 10, 11]
        ),
        (
            [1, 4, 8, 12],
            [2, 3, 5, 6, 7, 9, 10, 11]
        )
    ]

    for sorted_arrays in tuple_of_sorted_arrays:
        sorted_array_1st = sorted_arrays[0]
        sorted_array_2nd = sorted_arrays[1]
        print("sorted_array_1st    : ", sorted_array_1st)
        print("sorted_array_2nd    : ", sorted_array_2nd)
        print("merged sorted array : ", merge_2_sorted_arrays(sorted_array_1st, sorted_array_2nd))
        print()
