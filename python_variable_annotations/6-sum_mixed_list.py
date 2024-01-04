#!/usr/bin/env python3
""" Function with type annotations """

from typing import List, Union

def compute_sum_of_mixed_elements(elements: List[Union[int, float]]) -> float:
    """ Computes and returns the sum of integers and floats in the provided list """
    result_sum = 0.0
    for element in elements:
        result_sum += element
    return result_sum

