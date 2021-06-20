"""
https://www.hackerrank.com/challenges/repeated-string
"""

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    length_of_base_string = len(s)

    if not length_of_base_string:
        return 0

    num_repeat_string = n//length_of_base_string
    remainder_length_string = n%length_of_base_string
    num_occurencies_in_base_string = 0
    num_occurencies_in_remainder_string = 0

    # Get occurencies in base
    for char in s:
        if char == 'a':
            num_occurencies_in_base_string += 1

    if remainder_length_string:
        for char in s[:remainder_length_string]:
            if char == 'a':
                num_occurencies_in_remainder_string +=  1

    total_occurencies = num_repeat_string*num_occurencies_in_base_string +\
                        num_occurencies_in_remainder_string
    return total_occurencies

repeatedString('ababcdefg', 6)
repeatedString('ababcdefg', 16)

