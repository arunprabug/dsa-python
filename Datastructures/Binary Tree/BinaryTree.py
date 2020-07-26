class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order_traversal(self, root):
        if(root is None):
            return

        print(root.data)
        self.pre_order_traversal(root)
        self.pre_order_traversal(root)

    def iter_pre_order_traversal(self, root):
        if(root is None):
            return

        stack = []
        stack.append(root)

        while(len(stack) > 0):
            temp = stack.pop()
            print(temp.data)
            if(temp.right is not None):
                stack.append(temp.right)
            if(temp.left is not None):
                stack.append(temp.left)

    def in_order_traversal(self, root):
        if(root is None):
            return

        self.in_order_traversal(root)
        self.in_order_traversal(root)
        print(root.data)

    def level_order_traversal(self, root):
        if(root is None):
            return

        queue = [root]
        while(len(queue) > 0):
            temp = queue.pop()
            print(temp.data)
            if(temp.left is not None):
                queue.add(0, temp.left)
            if(temp.right is not None):
                queue.add(0, temp.right)

    def iter_in_order_traversal(self, root):
        if(root is None):
            return

        stack = []
        temp = root

        while(len(stack) > 0 or temp is not None):
            if(temp is not None):
                stack.append(temp)
                temp = temp.left
            else:
                temp = stack.pop()
                print(temp.data)
                temp = temp.right

    def iter_post_order_traversal(self, root):
        if(root is None):
            return

        stack = []
        temp = root
        recentlyPopped = None

        while(len(stack) > 0 or temp is not None):
            if(temp is not None):
                stack.append(temp)
                temp = temp.left
            else:
                stackRight = stack[len(stack)-1].right
                if(stackRight is not None and stackRight is not recentlyPopped):
                    temp = stack[len(stack)-1].right
                    stack.append(temp)
                    temp = temp.left
                else:
                    recentlyPopped = stack.pop()
                    print(recentlyPopped.data)


tree = BinaryTree()
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)

tree.root = node1
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node5.left = node6
node3.right = node7
node7.right = node8

tree.iter_post_order_traversal(tree.root)
