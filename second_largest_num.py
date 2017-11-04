"""find the second largest number:
input: The first line contains . The second line contains an array
of  integers each separated by a space.

output: Print the value of the second largest number.
"""
if __name__ == '__main__':
    n = int(raw_input())
    A = map(int, raw_input().split())

#print A

num = set([_ for _ in A])
second_max = sorted(num)[-2]
print second_max
