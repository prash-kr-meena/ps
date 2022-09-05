def range_overlaps(start_A, end_A, start_B, end_B):
    """ NOTICE
        Instead of focusing on the logic, that when two ranges will overlap (That will have more cases)
        Focus on the logic, when two ranges will not overlap

                        A----------A

        B--------B                      B--------B
    """

    # case when range_B will not overlap range_A
    if start_B > end_A or end_B < start_A:
        return False
    else:
        return True


if __name__ == "__main__":
    pass
