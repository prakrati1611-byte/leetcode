class Solution(object):
    def trailingZeroes(self,n):
        c=0
        power=5
        while power<=n :
           c+=n//power
           power=power*5
        return c


