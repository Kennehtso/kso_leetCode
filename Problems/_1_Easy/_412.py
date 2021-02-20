from typing import List
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        r = []
        for e in range(1, n+1):
            if e%15==0: r.append("FizzBuzz")
            elif e%3==0: r.append("Fizz")
            elif e%5==0: r.append("Buzz")
            else: r.append(e)
        print(r)
        return r
slt = Solution()
# Test Case
slt.fizzBuzz(15)
3 , 6, 9, 12, 15, 18, 21, 24, 27, 30
"""
412. Fizz Buzz

Write a program that outputs the string representation of numbers from 1 to n.
But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. 
For numbers which are multiples of both three and five output “FizzBuzz”.

Example:
n = 15,
Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]

""" 