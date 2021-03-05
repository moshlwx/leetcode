'''又名回溯算法
# 基本流程
递归尝试所有选择

# 适用场景
1. 全排列

'''


def dfs(path: list, choose: list):

    # 判断返回
    if len(path) == len(target) or not choose:  # 或其他满足条件
        res.append(path)
        return

    # 递归尝试所有选择
    for c in choose:
        path.append(c)
        dfs(path, choose-c)
        path.pop()


target = [1, 2, 3, 4]
res = []
choose = [1, 23, 4]
dfs([], choose)
print(res)
