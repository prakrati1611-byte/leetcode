class Solution(object):
    def countDigits(self, num):
        c=0
        temp=num
        while temp>0:
            r=temp%10
            if num%r==0:
                c+=1
            temp//=10
        return c

        """
        :type num: int
        :rtype: int
        """
        
