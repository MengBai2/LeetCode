# 4.Median of Two Sorted Arrays

class Solution:
    def findMedianSortedArrays(self, nums1: 'List[int]', nums2: 'List[int]') -> 'float':
        m = len(nums1)
        n = len(nums2)
        mlst = [] # merged list
        i = 0 # index of nums1
        j = 0 # index of nums2
        
        # odd or even
        if (m+n) % 2 == 0: # even
            mid = (m+n)/2
            while len(mlst) < mid + 1 and i < m and j < n:
                if nums1[i] == nums2[j]:
                    mlst.append(nums1[i])
                    mlst.append(nums2[j])
                    i +=1
                    j +=1
                elif nums1[i] < nums2[j]:
                    mlst.append(nums1[i])
                    i +=1
                else:
                    mlst.append(nums2[j])
                    j +=1
            # add additional points or not?
            if len(mlst) - (mid + 1) == 1:
                return (mlst[-2] + mlst[-3])/2
            if len(mlst) < mid+1:

                if i == m :
                    mlst = mlst + nums2[j:int(j + mid - len(mlst)+1)]
                elif j == n  :
                    mlst = mlst + nums1[i:int(i + mid - len(mlst)+1)]
            
                
            return (mlst[-1] + mlst[-2])/2
            
        else:
            mid = (m+n)/2 - 0.5
            while len(mlst) < mid + 1 and i < m and j < n:
                if nums1[i] == nums2[j]:
                    mlst.append(nums1[i])
                    mlst.append(nums2[j])
                    i +=1
                    j +=1
                elif nums1[i] < nums2[j]:
                    mlst.append(nums1[i])
                    i +=1
                else:
                    mlst.append(nums2[j])
                    j +=1
            if len(mlst) - (mid + 1) == 1:
                return mlst[-2]
            if len(mlst) < mid+1:

                if i == m :
                    mlst = mlst + nums2[j:int(j + mid - len(mlst)+1)]
                elif j == n  :
                    mlst = mlst + nums1[i:int(i + mid - len(mlst)+1)]
                
            return mlst[-1]
            