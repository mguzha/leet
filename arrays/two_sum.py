from typing import List

from log import logger


class Solution:
    def _brute_force_solution(self, nums: List[int], target: int) -> List[int]:
        """
        https://leetcode.com/problems/two-sum/submissions/1062209943/

        :param nums:
        :param target:
        :return:
        """
        for i, number_i in enumerate(nums):
            for j, number_j in enumerate(nums):
                if i == j:
                    continue
                if number_i + number_j == target:
                    return [i, j]

    def _improved_brute_force_solution(self, nums: List[int], target: int) -> List[int]:
        """
        https://leetcode.com/problems/two-sum/submissions/1062278489/

        :param nums:
        :param target:
        :return:
        """
        for i, number_i in enumerate(nums):
            for j, number_j in enumerate(nums[i + 1:]):
                # if i == j:
                #     continue
                if number_i + number_j == target:
                    return [i, i + 1 + j]

    def _sorted_solution(self, nums: List[int], target: int) -> List[int]:
        """
        :param nums:
        :param target:
        :return:
        """
        sorted_nums = sorted(nums)  # nlog(n)
        original_idx = sorted(range(len(nums)), key=lambda idx: nums[idx])  # nlog(n)

        for i, number_i in enumerate(nums):
            for j, number_j in enumerate(nums[i + 1:]):
                # if i == j:
                #     continue
                if number_i + number_j == target:
                    return [i, i + 1 + j]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        https://leetcode.com/problems/two-sum/
        https://stepik.org/lesson/561776/step/1?unit=555787
        https://stepik.org/lesson/356966/step/1?unit=341057

        Given an array of integers nums and an integer target,
        return INDICES of the two numbers such that they add up to target.

        You may assume that each input would have exactly one solution, and you may NOT use the same element twice.

        You can return the answer in any order.

        :param nums:
        :param target:
        :return:
        """
        # return self._brute_force_solution(nums, target)
        # return self._improved_brute_force_solution(nums, target)
        return self._sorted_solution(nums, target)

    def run_test(self):
        for i, (data, target, gt) in enumerate([
            ([2,4,1,93,2], 94, [2, 3]),
            ([2,7,11,15], 9, [0, 1]),
            ([3,2,4], 6, [1, 2]),
            ([3,3], 6, [0, 1]),
            ([1, 10, 11, 12, 13, 12, 9], 10, [0, 6]),
        ]):
            pred = self.twoSum(data, target)
            if len(set(pred) - set(gt)):
                raise RuntimeError(f'Failed to run {i}th test: {data} - {target} - {pred} - {gt}')
            else:
                logger.info(f'Succeeded to run {i}th test: {data} - {target} - {pred} - {gt}')