# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        st = "("
        if root:
            st = st + str(root.val) + self.serialize(root.left) + self.serialize(root.right)
        st = st + ")"
        return st

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        print(data)
    
        def deserial(ind):
            if data[ind+1] == ')':
                return None, ind+2
            
            l_node = ind + 1

            while data[l_node] != '(':
                l_node += 1

            node = TreeNode(int(data[ind+1: l_node]))
            node.left, r_node = deserial(l_node)
            node.right, n = deserial(r_node)

            return node, n+1
        
        root, _ = deserial(0)
        return root

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))