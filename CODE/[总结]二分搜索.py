'''
二分搜索的基本、左右边界的找法，
基本都是在二分搜索的基础上修改初始化、终止条件、边界值
'''


def binary_search(nums: list, target: int):
    left = 0
    right = len(nums) - 1

    while left <= right:
        # use // to get int result, revode error when nums[mid]
        mid = left + (right-left)//2

        if nums[mid] < target:  # target in right half
            left = mid + 1
        elif nums[mid] > target:  # in left half
            right = mid - 1
        else:  # nums[mid] == target
            return mid
    # no return after loop, return -1
    return -1


def binary_left_bound(nums: list, target: int):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right-left)//2

        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            right = mid - 1  # 区别点：nums[mid] == target时不返回，锁定左侧边界，更新右边界

    # 检查越界、目标值不存在的情况，返回默认值
    if left >= len(nums) or nums[left] != target:
        return -1
    return left


def binary_right_bound(nums: list, target: int):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right-left)//2

        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid - 1  # 区别点：nums[mid] == target时不返回，锁定右侧边界，更新左边界

    # 检查越界、目标值不存在的情况，返回默认值
    if right < 0 or nums[right] != target:
        return -1
    return right
