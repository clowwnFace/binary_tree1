class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self,root):
        self.root = Node(root)


    def pre_order (self, start , records):
        if start is not None:
            records.append(start.value)
            records = self.pre_order(start.left,records)
            records = self.pre_order(start.right , records)

        return records

tree = Tree(5)
tree.root.left = Node(3)
tree.root.right = Node(4)

print(tree.pre_order(tree.root , []))


