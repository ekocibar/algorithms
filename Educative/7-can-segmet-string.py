# 7. String segmentation
'''You are given a dictionary of words and a large input string. You have to
find out whether the input string can be completely segmented into the words of
a given dictionary. The following two examples elaborate on the problem further.
Given a dictionary of words.
apple apple pear pie
Input string of “applepie” can be segmented into dictionary words.
Input string “applepeer” cannot be segmented into dictionary words.'''
def can_segment_string(s, dictionary):
  for i in range(1, len(s)+1):
    first_part = s[:i]
    if first_part in dictionary:
      second_part = s[i:]
      if not second_part or second_part in dictionary\
        or can_segment_string(second_part,dictionary):
        return True
  return False
