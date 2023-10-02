from typing import List

from log import logger


class Solution:
    def _brute_force_solution(self, nums: List[int]) -> int:
        n_major_threshold = len(nums) // 2
        res = {}
        for n in nums:
            if n in res:
                res[n] += 1
            else:
                res[n] = 0

            if res[n] >= n_major_threshold:
                return n
        else:
            return len(nums)

    def majorityElement(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/majority-element/

        Given an array nums of size n, return the majority element.

        The majority element is the element that appears more than ⌊n / 2⌋ times.
        You may assume that the majority element always exists in the array.

        Constraints:

        n == nums.length
        1 <= n <= 5 * 104
        -109 <= nums[i] <= 109

        :param nums:
        :param target:
        :return:
        """
        return self._brute_force_solution(nums)

    def run_test(self):
        for i, (data, gt) in enumerate([
            ([], 0),
            ([3, 2, 3], 3),
            ([2, 2, 1, 1, 1, 2, 2], 2),
        ]):
            pred = self.majorityElement(data)
            if pred != gt:
                raise RuntimeError(f'Failed to run {i}th test: {data} - {pred} - {gt}')
            else:
                logger.info(f'Succeeded to run {i}th test: {data} - {pred} - {gt}')
