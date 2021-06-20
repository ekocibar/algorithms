"""
https://www.hackerrank.com/challenges/counting-valleys
"""

def countingValleys(steps, path):
    valley_count = 0
    current_position = 0
    for direction in path:
        if direction == 'U':
            current_position += 1
            if current_position == 0:
                valley_count +=1
        else:
            current_position -= 1

    return valley_count