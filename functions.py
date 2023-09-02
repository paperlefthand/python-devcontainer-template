from typing import List


def add(a: int, b: int) -> int:
    """2つの数値の和をとる

    Args:
        a (int): 数値
        b (int): 数値

    Returns:
        int: 引数aとbの和
    """
    return a + b


def add_list(nums: List[int]) -> int:
    return sum(nums)
