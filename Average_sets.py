"""
Task is  to compute average of different plant heights in a
garden using the knowledge of sets.
"""

from __future__ import division
def average(array):
    height_lst = set(arr)
    avg = sum(height_lst)/len(height_lst)
    return avg

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    result = average(arr)
    print result
