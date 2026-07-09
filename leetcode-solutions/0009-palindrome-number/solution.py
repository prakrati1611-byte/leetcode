class Solution(object):
    def isPalindrome(self, x):
       reverse = 0
       temp=x
       while temp>0:
          r= temp%10
          temp//=10
           
          reverse=reverse*10+r
       if  reverse==x:
            return True
       else:
            return False

