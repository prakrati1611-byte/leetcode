class Solution(object):
    def FindPow(self, x, n):
      if n==0:
        return 1
      a= self.FindPow(x,n//2)
      if n%2==0:
        return a*a
      else:
        return a*a*x
    def myPow(self, x, n):
        if n>=0:
            return self.FindPow(x,n)
        else:
            return 1/self.FindPow(x,n*(-1))
        
