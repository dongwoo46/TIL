# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        graph = {}
        self.buildGraph(root, None, graph)

        queue = [(target, 0)]
        visited = set([target])
        res = []

        while queue:
            node, dist = queue.pop(0)

            if dist == k:
                res.append(node.val)

            if dist > k:
                break

            for neigh in graph[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    queue.append((neigh, dist + 1))

        return res

    def buildGraph(self, node, parent, graph):
        if not node: return

        if node not in graph:
            graph[node] = []

        if parent:
            graph[node].append(parent)
            graph[parent].append(node)

        self.buildGraph(node.left, node, graph)
        self.buildGraph(node.right, node, graph)


root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

solution = Solution()
target_node = root.left
k_distance = 2
result = solution.distanceK(root, target_node, k_distance)

# 결과 출력
print(result)

