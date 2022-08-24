import re
values = {'IX' : 9, 'XL'  : 40, 'XC' : 90, 'CD': 400, 'CM': 900, 'XC': 90, 'IV': 4, 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


class Solution :
    def romanToInt(self, s):
        number = 0
        for k,v in values.items():
            number += v*(len(re.findall(k, s)))
            s = s.replace(k, '')


        return number

solution = Solution()
#
print(solution.romanToInt('CM'))




