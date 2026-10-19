
class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    def __init__(self):
        self.root = None

    def insert(self, parent_name, name, side):
        if side not in ("left", "right"):
            raise ValueError("Side must be 'left' or 'right'.")

        if self.root is None:
            raise ValueError("The tree is empty.")

        def find_parent(node):
            if node is None:
                return None
            if node.name == parent_name:
                return node

            found = find_parent(node.left)
            if found is not None:
                return found

            return find_parent(node.right)

        parent = find_parent(self.root)

        if parent is None:
            raise ValueError("Parent doctor was not found.")

        if getattr(parent, side) is not None:
            raise ValueError("That position is already occupied.")

        setattr(parent, side, DoctorNode(name))

    def preorder(self, node):
        if node is None:
            return []
        return (
            [node.name]
            + self.preorder(node.left)
            + self.preorder(node.right)
        )

    def inorder(self, node):
        if node is None:
            return []
        return (
            self.inorder(node.left)
            + [node.name]
            + self.inorder(node.right)
        )

    def postorder(self, node):
        if node is None:
            return []
        return (
            self.postorder(node.left)
            + self.postorder(node.right)
            + [node.name]
        )


if __name__ == "__main__":
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")

    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")

    print("Preorder:", tree.preorder(tree.root))
    print("Inorder:", tree.inorder(tree.root))
    print("Postorder:", tree.postorder(tree.root))
