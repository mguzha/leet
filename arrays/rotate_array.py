from typing import List

from log import logger


class Solution:
    def _brute_force_solution(self, nums: List[int], k: int) -> None:
        """
        https://leetcode.com/problems/rotate-array/submissions/1062368088/
        https://stepik.org/lesson/561776/step/2?unit=555787
        https://stepik.org/lesson/356978/step/1?unit=341069

        :param nums:
        :param k:
        :return:
        """
        k = k % len(nums)
        if k != 0:
            tmp = nums[:-k]
            nums[:k] = nums[-k:]
            nums[k:] = tmp

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self._brute_force_solution(nums, k)

    def run_test(self):
        for i, (data, target, gt) in enumerate([
            ([1,2,3,4,5,6,7], 3, [5,6,7,1,2,3,4]),
            ([-1,-100,3,99], 2, [3,99,-1,-100]),
            ([1], 0, [1]),
            ([1, 2], 0, [1, 2]),
            ([1, 2], 3, [2, 1]),
            ([1, 2], 5, [2, 1]),
            ([1], 1, [1]),
        ]):
            self.rotate(data, target)
            if data != gt:
                raise RuntimeError(f'Failed to run {i}th test: {data} - {target} - {data} - {gt}')
            else:
                logger.info(f'Succeeded to run {i}th test: {data} - {target} - {data} - {gt}')