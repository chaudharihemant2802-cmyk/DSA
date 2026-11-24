from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)
        return root

    def level_order(self, root):
        if root is None:
            print("Tree is empty.")
            return

        queue = deque([root])
        level = 0
        while queue:
            level_size = len(queue)
            level_nodes = []
            for _ in range(level_size):
                current = queue.popleft()
                level_nodes.append(str(current.data))
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            print(f"Level {level}: {' '.join(level_nodes)}")
            level += 1

    def height(self, root):
        if root is None:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

    def print_leaves(self, root):
        if root is None:
            return
        if root.left is None and root.right is None:
            print(root.data, end=" ")
            return
        self.print_leaves(root.left)
        self.print_leaves(root.right)


if __name__ == "__main__":
    bst = BST()

    elements = list(map(int, input("Enter elements for original BST (space-separated): ").split()))
    for val in elements:
        bst.root = bst.insert(bst.root, val)

    print("\n--- Original BST (Level-wise) ---")
    bst.level_order(bst.root)

    new_val = int(input("\nEnter a new element to insert into the BST: "))
    bst.root = bst.insert(bst.root, new_val)

    print("\n--- New BST after Insertion (Level-wise) ---")
    bst.level_order(bst.root)

    print(f"\nHeight of the BST (in nodes): {bst.height(bst.root)}")

    print("Leaf nodes: ", end="")
    bst.print_leaves(bst.root)
    print()
