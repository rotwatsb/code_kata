import functools

class Solution(object):
    def numberToWords(self, num):
        if num == 0:
            return "Zero"
        
        num = ''.join(reversed(str(num))) if num > 9 else str(num)
        english = []

        prfxs1 = {
            '00': "",
            '10': "One",
            '20': "Two",
            '30': "Three",
            '40': "Four",
            '50': "Five",
            '60': "Six",
            '70': "Seven",
            '80': "Eight",
            '90': "Nine",
            '01': "Ten",
            '11': "Eleven",
            '21': "Twelve",
            '31': "Thirteen",
            '41': "Fourteen",
            '51': "Fifteen",
            '61': "Sixteen",
            '71': "Seventeen",
            '81': "Eighteen",
            '91': "Nineteen"}
        
        prfxs2 = {
            '0': "",
            '1': "",
            '2': "Twenty",
            '3': "Thirty",
            '4': "Forty",
            '5': "Fifty",
            '6': "Sixty",
            '7': "Seventy",
            '8': "Eighty",
            '9': "Ninety"}

        prfxs3 = {
            0: "",
            1: "Thousand",
            2: "Million",
            3: "Billion"}

        i = 0
        while i * 3 < len(num):
            if int(num[i * 3: (i+1) * 3]) != 0:
                english.append(strip(self.num2words(num[i * 3: (i + 1) * 3], i, prfxs1, prfxs2, prfxs3)))
            i += 1
        return strip(' '.join(reversed(english)) if len(english) > 1 else english[0])

    def num2words(self, num, i, prfxs1, prfxs2, prfxs3):
        english = []
        if len(num) > 2 and not num[2] == '0':
            english.append(prfxs1[num[2] + '0'])
            english.append("Hundred")
        if len(num) > 1 and not num[1] == '0' and not num[1] == '1':
            english.append(prfxs2[num[1]])
            english.append(prfxs1[num[0] + '0'])
        elif len(num) > 1 and (num[1] == '0' or num[1] == '1'):
            english.append(prfxs1[num[0:2]])
        elif len(num) == 1:
            english.append(prfxs1[num[0] + '0'])
        if not i == 0:
            english.append(prfxs3[i])
        english = list(filter(lambda x: x != "", english))
        return strip(' '.join(list(x for x in english)) if len(english) > 1 else english[0])

def strip(x):
    x = x.strip()
    return x
                           
                           
    
