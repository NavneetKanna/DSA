
class BinarySearchTree:
    def __init__(self, value) -> None:
        self.value = value
        self.left_node = None
        self.right_node = None

    def insert(self, val):
        if val < self.value:
            if self.left_node:
                self.left_node.insert(val)
            else:
                self.left_node = BinarySearchTree(val)
        else:
            if self.right_node:
                self.right_node.insert(val)
            else:
                self.right_node = BinarySearchTree(val)

    # Root, Left, Right
    def dfs_pre(self):
        result = ""

        result += str(self.value) + " "

        if self.left_node:
            result += self.left_node.dfs_pre()
        
        if self.right_node:
            result += self.right_node.dfs_pre()

        return result

    def search(self, key):
        if self is None or key == self.value:
            return self

        if key < self.value:
            if not self.left_node:
                return None
            return self.left_node.search(key)
        else:
            if not self.right_node:
                return None
            return self.right_node.search(key)

#         5
#       /   \
#      3     7
#     / \   / \
#    1   4 6   8
if __name__ == "__main__":
    bst = BinarySearchTree(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(1)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)

    print(bst.dfs_pre())

    found = bst.search(8)
    if found:
        print("Found")
    else:
        print("Not Found")