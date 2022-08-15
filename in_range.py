from pickle import HIGHEST_PROTOCOL
from tracemalloc import start


def in_range(nums, lowest, highest):
    """Print numbers inside range.

    - nums: list of numbers
    - lowest: lowest number to print
    - highest: highest number to print

    For example:

      in_range([10, 20, 30, 40], 15, 30)

    should print:

      20 fits
      30 fits
    """

    # YOUR CODE HERE
    min = lowest
    max = highest

    for num in nums:
        if num >= lowest and num <= highest:
            print(f"{num} fits")

    # for in_range in list(range(15, 30+1)):
    #     print(in_range)
    #         for num in nums:
    #             print(f"num:{num}")
    #             if (min > num):
    #                 min = num
    #             if (max < num):
    #                 max = num


in_range([10, 20, 30, 40, 50], 15, 30)
