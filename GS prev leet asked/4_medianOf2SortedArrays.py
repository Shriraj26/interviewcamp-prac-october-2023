"""
Neetcode Bin Search
Go through this problem again
https://www.youtube.com/watch?v=q6IEA26hvXc
TC - O(log(min( len(A), len(B))))!!!  --> O(log(min(m,n))) 
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        A, B = nums1, nums2
        # B is small array than A
        if len(B) < len(A):
            A, B = B, A

        total = len(nums1) + len(nums2)
        half = total // 2

        l, r = 0, len(A) - 1 # left partition and right partition for entire array
        while True:
            i = (l + r) // 2 # Partition for A
            j = half - i - 2 # partition for B

            # Values at left and right partitions for A and B
            Aleft = A[i] if i >= 0 else -float('inf')
            Bleft = B[j] if j >= 0 else -float('inf')
            Aright = A[i+1] if (i+1) < len(A) else float('inf')
            Bright = B[j+1] if (j+1) < len(B) else float('inf')

            # Condition when we got partition
            if Aleft <= Bright and Bleft <= Aright:
                # odd length 
                if total % 2 == 1: # median is in right partition, 
                    return min(Aright,Bright)

                # even length
                else:
                    return (max(Aleft, Bleft) + min(Aright,Bright)) / 2
            
            # it means that left partition has extra elements
            elif Aleft > Bright:
                r = i - 1
            # this means that right has extra
            else:
                l = i + 1

            




