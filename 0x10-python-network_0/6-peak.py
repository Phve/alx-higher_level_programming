#!/usr/bin/python3
"""Algorithms for a  list of integers."""


def find_peak(list_of_integers):
    """Finds a peak in list of unsorted integers."""
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
