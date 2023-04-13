class Solution(object):
    def gradingStudents(self, grades):
        # Write your code here
        result = []
        for i in grades:
            if i < 40:
                if i >= 38 and (40 - i) < 3:
                        result.append(40)
                else:
                    result.append(i)
            else:
                a = 0
                for j in range(i, 101):
                    if (j % 5) == 0:
                        if (j - i) < 3:
                            a = j
                        else:
                            j = i
                        break
                result.append(j)
        return result
    def gradingStudents2(self, grades):
        for i in range(len(grades)):
            if grades[i] < 38 :
                continue
            else:
                if (5-(grades[i]%5)) < 3:
                    grades[i] += (5-(grades[i]%5))
        return grades
if __name__ == '__main__':
    test = Solution()
    ans = test.gradingStudents2([73,67,38,33])
    print(ans)
