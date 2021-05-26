'''https://leetcode.com/problems/group-anagrams/
Given an array of strings strs, group the anagrams together. You can return the
answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all the original letters exactly once.


Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]



Constraints:

    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lower-case English letters.
'''
def groupAnagrams(strs):
    distinct_anagrams = {}
    for string in strs:
        sorted_string_list = sorted(string)
        sorted_string_key = ''.join(sorted_string_list)
        distinct_anagrams[sorted_string_key] = distinct_anagrams.\
            get(sorted_string_key, []) + [string]

    return distinct_anagrams.values()

groupAnagrams(["eat","tea","tan","ate","nat","bat"])