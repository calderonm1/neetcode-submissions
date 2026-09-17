class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = []
        count1, count2 = 0, 0
        
        # combine the arrays
        while count1 < len(nums1) and count2 < len(nums2):
            if nums1[count1] < nums2[count2]:
                nums3.append(nums1[count1])
                count1 += 1
            else:
                nums3.append(nums2[count2])
                count2 += 1

        # extend the existing array with the remainder of the previous array
        while count1 < len(nums1):
            nums3.append(nums1[count1])
            count1 += 1
        while count2 < len(nums2):
            nums3.append(nums2[count2])
            count2 += 1

        print(nums3)

        # identify the mean
        # edge case where nums3 is empty
        if len(nums3) == 0:
            return None
        # if nums3 is even-length
        elif len(nums3) % 2 == 0:
            idx1 = len(nums3) / 2
            idx2 = idx1 - 1

            return (nums3[int(idx1)] + nums3[int(idx2)]) / 2
        else:
            return nums3[len(nums3) // 2]