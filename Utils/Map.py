from collections import defaultdict

from Utils.Array import input_array


def get_frequencies_in_integer_array(arr: list) -> dict:
    """
    Given an integer list, this method will return a dictionary (map),
    representing the frequencies of each of the elements in the list
    """

    # default dictionary
    freq = defaultdict(lambda: 0)
    for num in arr:
        freq[num] += 1

    return freq


if __name__ == "__main__":
    array = input_array()
    get_frequencies_in_integer_array(array)
