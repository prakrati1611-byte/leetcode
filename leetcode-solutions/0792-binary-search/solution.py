class Solution(object):
    def search(self, nums, target):
        def find(nums,target):
            low=0
            high=len(nums)-1

            while low<high:
                mid=low+(high-low)//2
                if nums[low]<=nums[mid]:
                     if nums[low]<=target<=nums[mid]:
                        high=mid
                     else:
                        low=mid+1
                else:
                    if nums[mid]<target<=nums[high]:
                        low=mid+1
                    else:
                        high=mid
            return low if nums[low] == target else -1
        return find(nums,target)

if __name__=="__main__":
    nums=[-1,0,3,5,9,10]
    target=9
    print(Solution().search(nums, target))
    
                

