from typing import List

from log import logger


class Solution:
    def _linear_solution(self, nums: List[int]) -> int:
        first_max = nums[0]
        second_max = None
        third_max = None

        for n in nums[1:]:
            if n > first_max:
                third_max = second_max
                second_max = first_max
                first_max = n

            elif (second_max is None or n > second_max) and n != first_max:
                third_max = second_max
                second_max = n

            elif (third_max is None or n > third_max) and n != first_max and n != second_max:
                third_max = n

        return third_max if third_max is not None else first_max

    def _brute_force_solution(self, nums: List[int]) -> int:
        nums_set = set(nums)
        new_nums = list(sorted(nums_set, reverse=True))
        if len(nums_set) < 3:
            return new_nums[0]
        return new_nums[2]

    def thirdMax(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/third-maximum-number/

        Given an integer array nums, return the third distinct maximum number in this array.
        If the third maximum does not exist, return the maximum number.


        Constraints:

        1 <= nums.length <= 104
        -231 <= nums[i] <= 231 - 1

        :param nums:
        :return:
        """
        return self._linear_solution(nums)

    def run_test(self):
        for i, (data, gt) in enumerate([
            # ([33,400,1, 30, 234], 33),
            # ([3,2,1], 1),
            # ([1,2], 2),
            # ([10], 10),
            # ([2,2,3,1], 1),
            # ([2,2,3,3,1,1,1], 1),
            # ([1, 2, -2147483648], -2147483648),
            ([3,3,4,3,4,3,0,3,3], 0),
        ]):
            pred = self.thirdMax(data)
            if pred != gt:
                raise RuntimeError(f'Failed to run {i+1}th test: {data} - {pred} - {gt}')
            else:
                logger.info(f'Succeeded to run {i+1}th test: {data} - {pred} - {gt}')
