class Solution(object):
    def countSwaps(self,a):
        numSwap = 0
        for j in range(len(a)):
            for i in range(len(a) - 1):
                if a[i] > a[i + 1]:
                    tmp = a[i]
                    a[i] = a[i + 1]
                    a[i + 1] = tmp
                    numSwap += 1
        print("Array is sorted in",numSwap,"swaps.")
        print("First Element:", a[0])
        print("Last Element:",a[-1])
        print()
if __name__ == '__main__':
    test = Solution()
    test.countSwaps([6,4,1])
    