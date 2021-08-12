class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ad_factor = factor = 2*numRows - 2
        final = ''
        if numRows == 1: return s
        for i in range(numRows):
            even, odd = ad_factor, (factor-ad_factor)
            count=0
            while i<len(s):
                final += s[i]
                #print(i)
                add_factor=(even if count%2 == 0 else odd)
                i+=(ad_factor if add_factor==0 else add_factor)
                count+=1
                #print(i)
            ad_factor = (factor if (ad_factor-2)==0 else (ad_factor-2))
        return final
