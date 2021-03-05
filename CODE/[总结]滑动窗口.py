'''
# 基本流程：
1. 移动右边界，更新窗口
2. while左边界需要收缩，收缩左边界，更新窗口
3. 窗口满足跳出条件，更新返回值

# 适用场景：
基础问题，给定来源字符串s，找到符合t目标的窗口，or符合t目标的最值
'''

def sliding_window(s: str, t: str):
    '''基础问题，给定来源字符串s，找到符合t目标的窗口，or符合t目标的最值
    '''
    # 利用python collections.Counter类型统计频次，更方便操作，正常可用数组或字典代替
    from collections import Counter

    left = 0
    right = 0
    window = Counter()
    # s_counter = Counter(s)
    # t_counter = Counter(t)
    valid_flag = False
    res = 0

    while right < len(s):
        # 暂存入窗口值，移动右边界
        c = s[right]
        right += 1

        # 更新窗口内数据
        window[c] += 1
        valid_flag = True if True else False

        while not valid_flag: # 当不满足限制时，更新左边界
            d = s[left]
            left += 1

            # 更新窗口内数据
            window[d] -= 1
            valid_flag = True if True else False
        
        # 窗口更新完毕，此时窗口内状态满足while条件的跳出值，常在这里更新返回值
        res = max(res, right - left)

    return res

