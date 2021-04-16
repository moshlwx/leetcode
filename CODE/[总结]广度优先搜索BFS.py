'''

'''


def neighbor(cur):
    '''返回cur的邻居list
    '''
    pass
    return []


def bfs(root, target):
    from queue import Queue
    q = Queue()
    visted = set()
    q.put(root)
    depth = 0

    while not q.empty():
        q_size = q.qsize()

        for _ in range(q_size):
            cur = q.get()

            if cur == target:
                return depth

            for i in neighbor(cur):
                if i and i not in visted:
                    q.put(i)
                    visted.add(i)

        # 到这里时遍历完一层，深度增加
        depth += 1

    # 遍历完一遍后没有目标值，返回-1
    return - 1
