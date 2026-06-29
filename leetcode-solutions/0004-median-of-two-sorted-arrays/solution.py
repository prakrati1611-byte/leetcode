class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        lst = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                lst.append(nums1[i]); i += 1
            else:
                lst.append(nums2[j]); j += 1
        while i < len(nums1):
            lst.append(nums1[i]); i += 1
        while j < len(nums2):
            lst.append(nums2[j]); j += 1

        mid = len(lst) // 2
        if len(lst) % 2 != 0:
            return float(lst[mid])
        else:
            return (lst[mid-1] + lst[mid]) / 2.0
