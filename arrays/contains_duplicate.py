from typing import List

from log import logger


class Solution:
    def _set_solution(self, nums: List[int]) -> bool:
        # if nums:
        return len(nums) - len(set(nums)) > 0
        # return False

    def _sorting_solution(self, nums: List[int]) -> bool:
        nums.sort()
        if nums:
            current_n = nums[0]
            for n in nums[1:]:
                if current_n == n:
                    return True
                else:
                    current_n = n

        return False

    def _brute_force_solution(self, nums: List[int]) -> bool:
        hash_map = {}
        for n in nums:
            hash_map[n] = hash_map.get(n, 0) + 1
            if hash_map[n] == 2:
                return True

        return False

    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        https://leetcode.com/problems/contains-duplicate/

        Given an integer array nums, return true if any value appears at least twice in the array,
         and return false if every element is distinct.

        Constraints:

        1 <= nums.length <= 105
        -109 <= nums[i] <= 109

        :param nums:
        :return:
        """
        # return self._sorting_solution(nums)
        # return self._brute_force_solution(nums)
        return self._set_solution(nums)

    def run_test(self):
        for i, (data, gt) in enumerate([
            ([], False),
            ([1,2,3,1], True),
            ([1,2,3,4], False),
            ([1,1,1,3,3,4,3,2,4,2], True),
        ]):
            pred = self.containsDuplicate(data)
            if pred != gt:
                raise RuntimeError(f'Failed to run {i}th test: {data} - {pred} - {gt}')
            else:
                logger.info(f'Succeeded to run {i}th test: {data} - {pred} - {gt}')
