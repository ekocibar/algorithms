"""
https://www.hackerrank.com/challenges/ctci-ransom-note
"""

def checkMagazine(magazine, note):
    dict = {}
    for word in magazine:
        dict[word] = dict.get(word,0) + 1

    for word in note:
        if dict.get(word, 0) == 0:
            print('No')
            return
        else:
            dict[word] -= 1
    print('Yes')

# O(n2)
# def checkMagazine(magazine, note):

#     for word in note:
#         if word in magazine:
#             magazine.remove(word)
#         else:
#             print('No')
#             return
#     print('Yes')