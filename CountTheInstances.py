"""In this challenge, the user enters a string and a substring. You have to print the number of
times that the substring occurs in the given string. String traversal will take place from left to right,
not from right to left.

NOTE: String letters are case-sensitive.

Input Format
The first line of input contains the original string. The next line contains the substring.
"""

def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string)):
         #print (string[i])
         #print (string[i:i+3]) (i:i+3 means from the current position, include the next two positons; beacuse substring
         #length in the current problem is three)
         #
         if (string[i:i+3])==sub_string:
                count+=1
    return count


if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()

    count = count_substring(string, sub_string)
    print count
