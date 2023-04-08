"""
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

"""
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        array = []

        for i in range(n):
            if (i +1) % 3 == 0 and (i + 1) % 5 == 0:
                array.append("FizzBuzz")
            elif (i + 1) % 3 == 0 and (i + 1) % 5 != 0:
                array.append("Fizz")
            elif (i + 1) % 5 == 0 and (i + 1) % 3 != 0:
                array.append("Buzz")
            else:
                array.append(str(i + 1))
        
        return array
    '''
        Other solution
    '''
    def fizzBuzz2(self, n):
        return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]

if __name__ == "__main__":
    test = Solution()
    ans = test.fizzBuzz2(3)