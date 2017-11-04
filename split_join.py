"""
You are given a string. Split the string on a " " (space) delimiter and
join using a - hyphen.
"""

def split_and_join(line):
    lst = line.split(" ")
    line = "-".join(lst)
    return line

if __name__ == '__main__':
    line = raw_input()
    result = split_and_join(line)
    print result
