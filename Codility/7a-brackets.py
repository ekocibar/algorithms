'''BRACKETS
https://app.codility.com/programmers/lessons/7-stacks_and_queues/brackets/


A string S consisting of N characters is considered to be properly nested if
any of the following conditions is true:

    S is empty;
    S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
    S has the form "VW" where V and W are properly nested strings.

For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

    def solution(S)

that, given a string S consisting of N characters, returns 1 if S is properly
nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given
S = "([)()]", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

    N is an integer within the range [0..200,000];
    string S consists only of the following characters:
        "(", "{", "[", "]", "}" and/or ")".
'''
def solution(S):
    my_stack = []
    # note: use 'insert(index, item)' and 'pop(index)'
    for char in S:
        if char == '{' or char == '[' or char == '(':
            my_stack.insert( len(my_stack), char)

        # note: check if the stack is empty or not (be careful)
        if len(my_stack) == 0:
            return 0
        elif char == ')':
            pop = my_stack.pop( len(my_stack)-1 )
            if pop != '(':
                return 0
        elif char == ']':
            pop = my_stack.pop( len(my_stack)-1 )
            if pop != '[':
                return 0
        elif char == '}':
            pop = my_stack.pop( len(my_stack)-1 )
            if pop != '{':
                return 0

    # note: check if the stack is empty or not (be careful)
    if len(my_stack)!=0:
        return 0
    else:
        return 1