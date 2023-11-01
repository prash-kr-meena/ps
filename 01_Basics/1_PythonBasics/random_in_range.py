"""
random — Generate pseudo-random numbers
Python Doc : https://docs.python.org/3/library/random.html

Warning The pseudo-random generators of this module should not be used for security purposes. 
For security or cryptographic uses, see the secrets' module.
"""
import random
from typing import List, Iterable, Any, Sized


def random_int_range(inclusive: int, exclusive: int, step: int = 1) -> int:
    """
    Note : random.randrange() works only with int type
    :param inclusive:       This will be included in result
    :param exclusive:       This will never be in result
    :param step:            Step point of range, By default step is 1
    :return:

    Example
    random.randrange(0, 10, 2) will generate any random numbers from [0, 2, 4, 6, 8].
    """
    return random.randrange(inclusive, exclusive, step)  # as we want to include the last array element too


def random_float__0_to_1() -> float:
    """
    Almost all module functions depend on the basic function random(),
    which generates a random float uniformly in the semi-open range [0.0, 1.0)          Note 1 is not included
    """
    return random.random()


def random_int(inclusive: int, exclusive: int) -> int:
    """
    Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1, 1).
    :param inclusive:       This will be included in result
    :param exclusive:       This will never be in result
    :return:
    """
    return random.randint(inclusive, exclusive)


def random_sequence_element(sequence: List[Any]) -> Any:  # Any because our sequence is not of any specific type
    """
    Return a random element from the non-empty sequence seq.
    Note : If seq is empty, raises IndexError.
    :param sequence:    should not be empty
    :return:
    """
    return random.choice(sequence)


def shuffle_sequence_inplace(sequence: List[Any]) -> None:
    return random.shuffle(sequence)


def generate_sample_sequence_of_size_k(sequence: List[Any], k: int) -> None:
    """
    Note : k can't be greater than the size of the sequence itself

    :param sequence:    original sequence
    :param k:           size of the sample sequence to be generatd
    :return:            sample sequence
    """
    random.sample(sequence, k)


if __name__ == '__main__':
    # Functions for int
    print(random_int(1, 3))
    print(random_int_range(1, 9, 2))
    print(random_int_range(1, 9))

    # Functions for float
    print(random_float__0_to_1())  # We can use this to simulate the random.randint() method as well

    # Functions for sequence
    sequence = [1, 2, 3, 4, 'a', 'b', 'c', {"key": "value"}, ["internal", "list"], 5, 6, 7]
    print("Original : ", sequence)
    print(random_sequence_element(sequence))
    shuffle_sequence_inplace(sequence)
    print("Shuffled : ", sequence)
    generate_sample_sequence_of_size_k(sequence, 10)
