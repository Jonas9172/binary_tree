结队编程答案：

n = int(input())
level = list(map(int, input().split()))

class Node:
    def __init__(self, index, value):
        self.index = index
        self.value = value
        self.left_node = None
        self.right_node = None
        self.left_child_count = 0

def insertNode(root, node, rsc):
    if root is None:
        return node
    if node.value < root.value:
        root.left_child_count += 1
        root.left_node = insertNode(root.left_node, node, rsc)
    else:
        rsc[node.index] += root.left_child_count + 1
        root.right_node = insertNode(root.right_node, node, rsc)
    return root


def getResult():
    root = None
    right_smaller_count = [0] * n
    for i in range(n - 1, -1, -1):
        root  = insertNode(root, Node(i, level[i]), right_smaller_count)

    root = None
    left_smaller_count = [0] * n
    level.reverse()
    for i in range(n - 1, -1, -1):
        root  = insertNode(root, Node(i, level[i]), left_smaller_count)
    left_smaller_count.reverse()

    total = 0
    for i in range(n):
        rs = right_smaller_count[i]
        rl = n - i - 1 - rs
        ls = left_smaller_count[i]
        ll = i - ls
        total += ll * rs + ls * rl
    return total

print(getResult())
