#!/usr/bin/env python3
""" Simple pagination"""
import csv
import math
from typing import List, Tuple


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


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a specific page of the dataset.

        Args:
        page (int): The page number to retrieve (1-indexed).
        page_size (int): The number of items per page.

        Returns:
        List[List]: A list containing the items for the specified
        page or an empty list if out of range.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)

        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]
