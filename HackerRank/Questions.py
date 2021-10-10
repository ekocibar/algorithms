

# Swap two digits from an integer, the result should be the maximum.
# For example 3580 -> 8350



# Write a function that would calculate a Pascal triangle element, given its
# coordinates.



# Call a function F in a loop. F returns a string of 140 chars. Write to the
# output 1 when F returns a string with the same letters (basically a permutation)
# of a string previously returned. (the question was not this well formed
'''Short python answer:'''
def findPermutationsSort():
    res = f([])
    perm_dict = {}
    for s in res:
        key = ''.join(sorted(s))
        if key in perm_dict:
            print 1
        else:
            perm_dict[key] = 1


# Given the following list of objects {user, loginTime, logoutTime}.
# What is the maximum number of concurrent users logged in at the same time?
# Input: [ {user: A, login: 1, logout: 3}, {user: B, login: 3, logout: 4},
# {user: C, login: 1, logout: 2}, {user: D, login: 123123123, logout: 987987987},
# {user: E, login: 1, logout: 3} ] Output: 3






# We have a log file, can grow pretty big. Each line is a trace-log, and the
# first field is the RequestID. We need to scan the file, and print all the
# logs for requests which resulted in error ..
# 001 BEGIN 001 fetched from db 001 some processing ..
# 002 BEGIN .. 002 fetched from db 001 returned success
# 003 BEGIN 001 END 003 some work 002 ERROR 003 some other work




# Union of n arrays with x elements. Output common members contained in at least
# 2 arrays. Explain the complexity of the algorithm used. We have a digested
# server log with username, visited page and timestamp. Create a processing
# algorithm that will output the most visited page/areas in such a way that
# will match partial path as well. i.e.
# { { user: "user1", page="/home" },
# { user: "user1", page="/home/account" },
# { user: "user1", page="/home/account/profile" },
# { user: "user1", page="/home/account/login" },
# { user: "user2", page="/about" },
# { user: "user2", page="/about/contact" },
# { user: "user2", page="/home" } }
# the output user1 - home/account - home user2 - /about PS I'm rephrasing
# because I cannot recall exactly the question





# if p1 and p2 are two consecutive prime number,
# in which cases (p1 + p2) / 2 is a prime number.




# Given an array of numbers, e.g. [5,0,9,2,5,5,5] -
# return all the consecutive numbers that add up to N.
# There were two followup questions to this. a) What if there are lot of zeros
# after the sum is 10. E.g. 505000000 - what would it return? b) what if we
# allow negative numbers. For example 5,5,-6,6,0,0 We also discussed its time complexity.



# Given an array of integers and integer K, return another array holding integers
# appeared K times in the given array





# retweet twitter tweets if newer one is an anagram of older one





# Count number of islands in a matrix.



# Given 2 lists how to get the smallest common item between them.



# Given a string of parentheses, check if the parentheses are balanced.
# Then the question was extended to all types of brackets.




"FRONTEND"



# What is A/B testing? How to do it? How to evaluate it?





# Coding with Pen and Paper: Tool-tips in depth (on newly added dom,
# delay on focusout etc)



#  questions about implementation of UI elements on the page. The element should
# be added dynamically to any part of the page. Implement one of the lodash functions



# What does "box-sizing: border-box;" do?
# Does it include the content, the margin, the padding and/or the border




# Form validation during the live coding test and explain closure.



# Face to face interview on site:
# 1 - Create a tooltip that can be attached to any DOM element
# 2 - Flatten an array



# Build web form with some inputs in it and ability to validate some of them.
# Knowledge of vanilla JavaScript. Event bubbling. Hot to prevent form from
# been submitted in two ways.


# Develop the data structure and javascript/html code for a table with stock
# info that refreshes each 5 min



# Develop a form generic form validator


# Develop a dropdown menu with hover intention of 300ms


# What this is in JavaScript


# Prioritise tasks in order of importance


