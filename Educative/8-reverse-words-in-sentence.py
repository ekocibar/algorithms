# 8. Reverse Words in a Sentence
'''Reverse the order of words in a given sentence (an array of characters).
"Hello World"  >>   "World Hello"'''
def reverse_words(sentence):
  list_of_words = sentence.split()
  return ' '.join(list_of_words[::-1])
reverse_words('We love Python')


# Another approach
def str_rev(str, start, end):
  if str == None or len(str) < 2:
    return

  while start < end:
    temp = str[start]
    str[start] = str[end]
    str[end] = temp

    start += 1
    end -= 1
  return str

def reverse_words(sentence):
  # Here sentence is a null-terminated string ending with char '\0'.
  if sentence == None or len(sentence) == 0:
    return

  #  To reverse all words in the string, we will first reverse
  #  the string. Now all the words are in the desired location, but
  #  in reverse order: "Hello World" -> "dlroW olleH".

  str_len = len(sentence)
  sentence = str_rev(sentence, 0, str_len - 2)

  # Now, let's iterate the sentence and reverse each word in place.
  # "dlroW olleH" -> "World Hello"

  start = 0
  end = 0

  while True:

  # find the  start index of a word while skipping spaces.
    while start < len(sentence) and sentence[start] == ' ':
      start += 1

    if start == str_len:
      break

  # find the end index of the word.
    end = start + 1
    while end < str_len and sentence[end] != ' ' and sentence[end] != '\0':
      end += 1

  # let's reverse the word in-place.
    sentence = str_rev(sentence, start, end - 1)
    start = end
  return sentence
