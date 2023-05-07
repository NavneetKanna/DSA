from collections import deque

class BinaryTree:
    def __init__(self, value) -> None:
        self.value = value
        self.left_node = None
        self.right_node = None
    
    def insert_left_node(self, value):
        if self.left_node is None:
            self.left_node = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left_node = self.left_node
            self.left_node = new_node
    
    def insert_right_node(self, value):
        if self.right_node is None:
            self.right_node = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right_node = self.right_node
            self.right_node = new_node
    
    # These are recursion implementation, hence, does not use stack
    # Root, Left, Right
    def dfs_pre(self):
        result = ""

        result += str(self.value) + " "

        if self.left_node:
            result += self.left_node.dfs_pre()
        
        if self.right_node:
            result += self.right_node.dfs_pre()

        return result

    # Left, Root, Right
    def dfs_in(self):
        result = ""

        if self.left_node:
            result += self.left_node.dfs_in()
        
        result += str(self.value) + " "

        if self.right_node:
            result += self.right_node.dfs_in()

        return result
        
    # Left, Right, Root
    def dfs_post(self):
        result = ""

        if self.left_node:
            result += self.left_node.dfs_post()
        
        if self.right_node:
            result += self.right_node.dfs_post()
        
        result += str(self.value) + " "

        return result

    # This is a non-recursive preorder implementation which uses stack
    def dfs(self):
        stack = deque()
        result = []

        stack.append(self)

        while stack:
            visited = stack.pop()

            result.append(visited.value)

            if visited.right_node:
                stack.append(visited.right_node)
            if visited.left_node:
                stack.append(visited.left_node)
            
        print(result)

    def bfs(self):
        queue = deque()
        result = []

        queue.append(self)

        while queue:
            visited = queue.popleft()

            result.append(visited.value)

            if visited.left_node:
                queue.append(visited.left_node)
            if visited.right_node:
                queue.append(visited.right_node)

        print(result)


#         1
#        /  \
#       2    5
#      / \  / \
#     3   4 6  7
if __name__ == "__main__":
    a_node = BinaryTree(1)
    a_node.insert_left_node(2)
    a_node.insert_right_node(5)

    b_node = a_node.left_node
    b_node.insert_left_node(3)
    b_node.insert_right_node(4)

    c_node = a_node.right_node
    c_node.insert_left_node(6)
    c_node.insert_right_node(7)

    d_node = b_node.right_node
    e_node = c_node.left_node
    f_node = c_node.right_node

    print("BFS using queue")
    a_node.bfs()
    print("DFS using stack")
    a_node.dfs()
    print("DFS using pre")
    print(a_node.dfs_pre())
    print("DFS using in")
    print(a_node.dfs_in())
    print("DFS using post")
    print(a_node.dfs_post())
    
