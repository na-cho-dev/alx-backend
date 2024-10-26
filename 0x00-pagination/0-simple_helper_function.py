#!/usr/bin/env python3
"""Simple helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Function  return a tuple of size two containing a
    start index and an end index corresponding to the
    range of indexes to return in a list for those particular
    pagination parameters.
    """
    start_indx = (page - 1) * page_size
    end_indx = page * page_size

    return (start_indx, end_indx)
