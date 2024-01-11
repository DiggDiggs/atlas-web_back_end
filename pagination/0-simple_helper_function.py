#!/usr/bin/env python3
"""
Basic Helper Function

Define a function named `index_range` that takes two integer parameters: 
`page` and `page_size`.

The function should output a tuple of size two, comprising a `start index` 
and an `end index`. These indices represent the range of indexes to extract 
from a list, given the specified pagination parameters.

Keep in mind that page numbering starts at 1, where the initial page is 
labeled as page 1.
"""


from typing import Tuple

def index_range(page: int, 
                page_size: int) -> Tuple[int, int]:
    """Calculate the start and end index for pagination.

    Args:
        page (int): Starting page number.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: Tuple of start and end index.
    """

    end_index = page * page_size
    start_index = end_index - page_size
    
    return start_index, end_index


