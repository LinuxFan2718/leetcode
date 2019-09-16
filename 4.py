from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2)
        if total_len % 2 == 0:  # even, need average of two middle numbers
            i = 0
            total_iterations = total_len // 2 - 1 # using // gives an integer
            while len(nums1) > 0 and len(nums2) > 0: # neither array is empty
                if i == total_iterations: # we are done
                    if nums1[0] < nums2[0]:
                        first_summand = nums1.pop(0)
                        if len(nums1) == 0:
                            return (first_summand + nums2[0]) / 2
                        else:
                            return (first_summand + min(nums1[0], nums2[0])) / 2
                    if nums1[0] == nums2[0]:
                        return (nums1[0] + nums2[0]) / 2
                    if nums1[0] > nums2[0]:
                        first_summand = nums2.pop(0)
                        if len(nums2) == 0:
                            return (first_summand + nums1[0]) / 2
                        else:
                            return (first_summand + min(nums1[0], nums2[0])) / 2
                # end of code handling the end
                if nums1[0] < nums2[0]:
                    nums1.pop(0)
                else:
                    nums2.pop(0)
                i += 1
            # one of the arrays is empty so jump to the two medians and average them
            remaining_nums = nums1 if len(nums1) > 0 else nums2
            first_summand_i = total_iterations - i
            return (remaining_nums[first_summand_i] + remaining_nums[first_summand_i+1]) / 2
        elif total_len % 2 == 1: # odd, simply find middle number
            i = 0
            total_iterations = total_len // 2 # the index of median element if had one sorted array         
            while len(nums1) > 0 and len(nums2) > 0: # neither array is empty
                if i == total_iterations: # we are done
                    return min(nums1[0], nums2[0])
                if nums1[0] < nums2[0]:
                    nums1.pop(0)
                else:
                    nums2.pop(0)
                i += 1
            # one of the arrays is empty
            remaining_nums = nums1 if len(nums1) > 0 else nums2
            index_median = total_iterations - i
            return remaining_nums[index_median]
solution = Solution()
nums1 = [1, 2]
nums2 = [3, 4]
answer = solution.findMedianSortedArrays(nums1, nums2)
print(answer)
nums1 = [1, 3]
nums2 = [2]
answer = solution.findMedianSortedArrays(nums1, nums2)
print(answer)
nums1 = []
nums2 = [2]
answer = solution.findMedianSortedArrays(nums1, nums2)
print(answer)