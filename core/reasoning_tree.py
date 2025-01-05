class ReasoningTree:
    def __init__(self):
        self.tree = {}

    def add_node(self, parent_node, child_node):
        if parent_node not in self.tree:
            self.tree[parent_node] = []
        self.tree[parent_node].append(child_node)

    def get_children(self, node):
        return self.tree.get(node, [])

    def validate_tree(self):
        # Implement validation logic here
        pass
