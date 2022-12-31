from typing import List


def search(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    if len(nums) == 1:
        return 0 if nums[0] == target else -1
    if target < nums[0] and target > nums[-1]:
        return -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif left == right:
            return -1
        elif left + 1 == right:
            if target == nums[left]:
                return left
            elif target == nums[right]:
                return right
            else:
                return -1
        elif nums[mid] > target:
            if nums[mid] > nums[right]:
                if target > nums[left]:
                    right = mid - 1
                elif target < nums[left]:
                    left = mid + 1
                else:
                    return left
            elif nums[mid] < nums[right]:
                right = mid - 1

        elif nums[mid] < target:

            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                if nums[right] > target:
                    left = mid + 1
                elif nums[right] < target:
                    right = mid - 1
                else:
                    return right
    return -1


print(search([4, 5, 6, 7, 0, 1, 2], 0))
