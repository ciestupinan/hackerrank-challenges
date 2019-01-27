"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format:
The first line contains n. The second line contains an array A[] of n integers each separated by a space.

Constraints:
2 <= n <= 10
-100 <= A[i] <= 100

Output Format:
Print the runner-up score.

    >>> runner_up_score(5,[2,3,6,6,5])
    5

    >>> runner_up_score(5, [8,7,6,5,4])
    7

"""


def runner_up_score(n, scores):
    
    sorted_scores = sorted(list(scores))
    reversed_scores = sorted_scores[::-1]
    first_place = reversed_scores[0]

    for i in range(len(reversed_scores)):

        # there can be multiple same numbers
        # this goes backwards from greatest to smallest
        # it will stop at the second greatest number
        #   because the list is sorted
        if reversed_scores[i] != first_place:
            return reversed_scores[i]




if __name__ == '__main__':
    # n = int(input())
    # arr = map(int, input().split())
    # print(runner_up_score(n, arr))

    import doctest
    if doctest.testmod().failed == 0:
        print('ALL TESTS PASSED')

