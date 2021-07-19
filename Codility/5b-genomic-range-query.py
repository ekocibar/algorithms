'''GENOMIC RANGE QUERY
https://app.codility.com/programmers/lessons/5-prefix_sums/genomic_range_query/

A DNA sequence can be represented as a string consisting of the letters A, C, G
and T, which correspond to the types of successive nucleotides in the sequence.
Each nucleotide has an impact factor, which is an integer. Nucleotides of types
A, C, G and T have impact factors of 1, 2, 3 and 4, respectively. You are going
to answer several queries of the form: What is the minimal impact factor of
nucleotides contained in a particular part of the given DNA sequence?

The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1]
consisting of N characters. There are M queries, which are given in non-empty
arrays P and Q, each consisting of M integers. The K-th query (0 ≤ K < M)
requires you to find the minimal impact factor of nucleotides contained in the
DNA sequence between positions P[K] and Q[K] (inclusive).

For example, consider string S = CAGCCTA and arrays P, Q such that:
    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6

The answers to these M = 3 queries are as follows:

        The part of the DNA between positions 2 and 4 contains nucleotides G
        and C (twice), whose impact factors are 3 and 2 respectively, so the
        answer is 2.
        The part between positions 5 and 5 contains a single nucleotide T,
        whose impact factor is 4, so the answer is 4.
        The part between positions 0 and 6 (the whole string) contains all
        nucleotides, in particular nucleotide A whose impact factor is 1, so
        the answer is 1.

Write a function:

    def solution(S, P, Q)

that, given a non-empty string S consisting of N characters and two non-empty
arrays P and Q consisting of M integers, returns an array consisting of M
integers specifying the consecutive answers to all queries.

Result array should be returned as an array of integers.

For example, given the string S = CAGCCTA and arrays P, Q such that:
    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6

the function should return the values [2, 4, 1], as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        M is an integer within the range [1..50,000];
        each element of arrays P, Q is an integer within the range [0..N − 1];
        P[K] ≤ Q[K], where 0 ≤ K < M;
        string S consists only of upper-case English letters A, C, G, T.
'''

def solution(S, P, Q):
    cumulative_A = [0] * ( len(S) + 1 )
    cumulative_C = [0] * ( len(S) + 1 )
    cumulative_G = [0] * ( len(S) + 1 )

    for i in range(len(S)):
        if S[i] == 'A':
            cumulative_A[i + 1] = cumulative_A[i] + 1
            cumulative_C[i + 1] = cumulative_C[i]
            cumulative_G[i + 1] = cumulative_G[i]
        elif S[i] == 'C':
            cumulative_A[i + 1] = cumulative_A[i]
            cumulative_C[i + 1] = cumulative_C[i] + 1
            cumulative_G[i + 1] = cumulative_G[i]
        elif S[i] == 'G':
            cumulative_A[i + 1] = cumulative_A[i]
            cumulative_C[i + 1] = cumulative_C[i]
            cumulative_G[i + 1] = cumulative_G[i] + 1
        else:
            cumulative_A[i + 1] = cumulative_A[i]
            cumulative_C[i + 1] = cumulative_C[i]
            cumulative_G[i + 1] = cumulative_G[i]

    M = len(P) # =len(Q)
    result = [0] * M
    for j in range( M ):

        start_position = P[j]
        end_position = Q[j] + 1 # inclusive

        num_A = cumulative_A[end_position] - cumulative_A[start_position]
        num_C = cumulative_C[end_position] - cumulative_C[start_position]
        num_G = cumulative_G[end_position] - cumulative_G[start_position]

        if num_A > 0:
            result[j] = 1
        elif num_C > 0:
            result[j] = 2
        elif num_G > 0:
            result[j] = 3
        else:
            result[j] = 4

    return result
