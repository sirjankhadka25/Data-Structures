class Binary_Search_TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def add_child(self, data):
        # Do not insert duplicates
        if data == self.data:
            return

        # Go left
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = Binary_Search_TreeNode(data)
        # Go right
        else:  # data > self.data
            if self.right:
                self.right.add_child(data)
            else:
                self.right = Binary_Search_TreeNode(data)

    def in_order_traversal(self):
        elements = []
        # left
        if self.left:
            elements += self.left.in_order_traversal()
        # root
        elements.append(self.data)
        # right
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    # OPTIONAL BUT VERY USEFUL FOR TESTS:

    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        else:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            # Node to delete found
            # Case 1: no child
            if self.left is None and self.right is None:
                return None
            # Case 2: one child
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            # Case 3: two children
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self


def build_tree(elements):
    root = Binary_Search_TreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root


# Example usage
if __name__ == "__main__":
    nums = [50, 30, 70, 20, 40, 60, 80]
    bst = build_tree(nums)
    print("In-order:", bst.in_order_traversal())  # should be sorted

    print("Search 40:", bst.search(40))
    print("Search 100:", bst.search(100))

    bst = bst.delete(70)
    print("After deleting 70:", bst.in_order_traversal())
