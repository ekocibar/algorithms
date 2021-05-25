'''NESTING
https://app.codility.com/programmers/lessons/7-stacks_and_queues/nesting/

A string S consisting of N characters is called properly nested if:

        S is empty;
        S has the form "(U)" where U is a properly nested string;
        S has the form "VW" where V and W are properly nested strings.

For example, string "(()(())())" is properly nested but string "())" isn't.

Write a function:

    def solution(S)

that, given a string S consisting of N characters, returns 1 if string S is
properly nested and 0 otherwise.

For example, given S = "(()(())())", the function should return 1 and given
S = "())", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..1,000,000];
        string S consists only of the characters "(" and/or ")".
'''
def solution(S):
    my_stack = []

    for char in S:
        if char == '(':
            my_stack.append(char)
        elif char == ')':
            # note: check if the stack is empty or not (be careful)
            if len(my_stack) == 0:
                return 0
            else:
                pop = my_stack.pop( len(my_stack)-1 )

    # note: check if the stack is empty or not (be careful)
    if len(my_stack) != 0:
        return 0
    else:
        return 1
