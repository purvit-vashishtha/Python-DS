# Merge Sort for finding Median Sorted Arrays
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        def merge(l1,l2,a):
            i = 0
            j = 0
            k = 0
            while i<len(l1) and j<len(l2):
                if l1[i]<l2[j]:
                    a.append(l1[i])
                    k += 1
                    i += 1
                else:
                    a.append(l2[j])
                    j += 1
                    k += 1
            while i<len(l1):
                a.append(l1[i])
                i += 1
                k += 1
            while j<len(l2):
                a.append(l2[j])
                j += 1
                k += 1
            return a
        
        a=[]
        mergearr = merge(nums1,nums2,a)
        if len(mergearr)%2==0:
            median1 = len(mergearr)//2
            median2 = len(mergearr)//2 -1
            ans = float(mergearr[median1+mergearr[median2]])/2
            return ans
        else:
            return mergearr[len(mergearr)//2]
