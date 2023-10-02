from typing import List

from log import logger


class Solution:
    def _brute_force_solution(self, nums: List[int], target: int) -> int:
        # fast track conditions
        if len(nums) == 0:
            return 1
        elif target <= nums[0]:
            return 0
        elif target == nums[-1]:
            return len(nums) - 1
        elif target > nums[-1]:
            return len(nums)

        initial_middle_idx = len(nums) // 2
        n_counter = 0

        while True:
            n_counter += 1

            if len(nums) == 1:
                if nums[0] >= target:
                    return initial_middle_idx
                return initial_middle_idx + 1

            middle_idx = len(nums) // 2

            if target == nums[middle_idx]:
                return initial_middle_idx + (middle_idx if n_counter > 1 else 0)

            elif target < nums[middle_idx]:
                # go left
                nums = nums[:middle_idx]
                initial_middle_idx = initial_middle_idx if n_counter > 1 else initial_middle_idx - middle_idx  # max(, 0)

            elif target > nums[middle_idx]:
                # go right
                nums = nums[middle_idx:]
                initial_middle_idx += middle_idx if n_counter > 1 else 0

    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        https://leetcode.com/problems/search-insert-position/

        Given a sorted array of distinct integers and a target value, return the index if the target is found.
        If not, return the index where it would be if it were inserted in order.

        You must write an algorithm with O(log n) runtime complexity.

        :param nums:
        :param target:
        :return:
        """
        return self._brute_force_solution(nums, target)

    def run_test(self):
        for i, (data, target, gt) in enumerate([
            ([1], 5, 1),
            ([5], 1, 0),
            ([1], 1, 0),
            ([1, 2, 3], 0, 0),
            ([1, 2, 3], 4, 3),
            ([1, 2], 3, 2),
            ([1, 3], 2, 1),
            ([1, 2], 0, 0),
            ([1,3,5,6], 5, 2),
            ([1,3,5,6], 2, 1),
            ([1,3,5,6], 7, 4),
            ([1, 30, 31, 40, 50, 55, 69], 70, 7),
            ([1, 30, 31, 40, 50, 55, 69], 33, 3),
            ([1, 30, 32, 40, 50, 55, 69], 31, 2),
            ([10, 30, 32, 40, 50, 55, 69], 1, 0),
            ([10, 30, 32, 40, 50, 55, 69], 19, 1),
            ([10, 13, 14, 15, 16, 17, 18, 19, 30, 32, 40, 50, 55, 69], 12, 1),
            ([10, 13, 14, 15, 16, 17, 18, 19, 30, 32, 40, 50, 55, 69], 20, 8),
            ([1, 4, 6, 7, 8, 9], 6, 2),
        ]):
            pred = self.searchInsert(data, target)
            if pred != gt:
                raise RuntimeError(f'Failed to run {i}th test: {data} - {target} - {pred} - {gt}')
            else:
                logger.info(f'Succeeded to run {i}th test: {data} - {target} - {pred} - {gt}')
