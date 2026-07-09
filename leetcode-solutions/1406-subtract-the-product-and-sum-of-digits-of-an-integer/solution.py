class Solution(object):
    def subtractProductAndSum(self, n):
        temp=n
        s=0
        product=1

        while temp>0:
           r= temp%10
           temp//=10
           s+=r
           product*=r 
        return product-s

        
        """
        :type n: int
        :rtype: int
        """
        
