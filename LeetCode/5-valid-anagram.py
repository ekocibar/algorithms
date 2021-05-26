'''Given two strings s and t, return true if t is an anagram of s, and false
otherwise.


Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false


Constraints:

    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt
your solution to such a case?
'''

def isAnagram(s, t):
    s_list = []
    t_list = []
    s_list[:0]=s
    t_list[:0]=t
    s_list.sort()
    t_list.sort()

    return s_list == t_list

def isAnagram2(s,t):
    return sorted(s) == sorted(t)