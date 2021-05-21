'''
矩阵中，方块内最大和对应的不同组合数
'''



class Solution:
    def sensors_num_category(self, sensors, cnt: int) -> int:
        m = len(sensors)
        n = len(sensors[0])
        res = []
        max_sum = 0

        for i in range(m-cnt+1):
            for j in range(n-cnt+1):
                cur_sum = 0
                cnt_list = []
                # cnt*cnt内求sum
                for cnt_i in range(cnt):
                    for cnt_j in range(cnt):
                        cnt_list.append(sensors[i+cnt_i][j+cnt_j])
                # print(i, j, cnt_list)
                cur_sum = sum(cnt_list)
                if cur_sum > max_sum:
                    res = cnt_list
                    max_sum = cur_sum
                elif cur_sum == max_sum:
                    res.extend(cnt_list.copy())
        # print(res)
        return len(set(res))

path = [2, 1, 1, 1]
path_sum = sum(path)
cur_sum = 0

for i, p in enumerate(path):
    if path_sum-p==cur_sum:
        print(i, p)
        break
    cur_sum += p