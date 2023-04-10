"""
https://www.codewars.com/kata/514b92a657cdc65150000006/train/python

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. 
Additionally, if the number is negative, return 0 (for languages that do have them).
Note: If the number is a multiple of both 3 and 5, only count it once.

"""

# my code
def solution(number):
    if number < 0:
        return 0
    else:
        sum = 0
        for x in range(0, number):
            if (x % 3) == 0 and (x % 5) == 0:
                sum += x
            elif (x % 3) == 0:
                sum += x
            elif (x % 5) == 0:
                sum += x
        return sum

# alternative
