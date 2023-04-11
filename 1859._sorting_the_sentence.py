"""
    Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.
"""

class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()
        tmp = {}
        sentence = ""
        for i in s:
            tmp[i[-1]] = i[:-1]
        tmp = sorted(tmp.items())
        for i in tmp:
                sentence += i[1] + " "
        return sentence.strip()
    def best_solut(self, s):
        return ' '.join([w[:-1] for w in sorted(s.split(),key=lambda x:x[-1])])
         
if __name__ == "__main__":
    test = Solution()
    ans = test.sortSentence("This1 not3 sentence4 is2")
    ans2 = test.best_solut("This1 not3 sentence4 is2")
    print(ans2)

    
