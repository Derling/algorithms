# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 20:08:12 2017

@author: Derling
"""

class Node():
    # 1. Helper class for debugging
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def remove(self, value, parent):
        if value < self.value:
            if self.left: # if left child, may be in lower level
                return self.left.remove(value, self)
            else:
                return False
        elif value > self.value:
            if self.right: # if right child, may be in lower level
                return self.right.remove(value, self)
            else:
                return False # no right node, value not in lower level
        else: # we found the node with the value!
            ''' the node has both children, in which case we want to set the
                current value of the node to the next largest number, then 
                we want to remove that node with the value we just set it to'''
            if self.left and self.right:
                self.value = self.right.get_min() 
                self.right.remove(self.value, self)
            elif parent.left == self:
                parent.left = self.left if self.left else self.right
            elif parent.right == self:
                parent.right = self.left if self.left else self.right
            return True

    def get_max(self):
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

    def get_min(self):
        if not self.left:
            return self.value
        else:
            return self.left.get_min()

class BinarySearchTree():
    # 1. Implement a BST with insert and delete functions
    def __init__(self, root = None):
        self. root = root

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, current):
        if current.value > value:
            if current.left:
                self._insert(value, current.left)
            else:
                current.left = Node(value)
        else:
            if current.right:
                self._insert(value, current.right)
            else:
                current.right = Node(value)

    def delete(self, value):
        if not self.root:
            return None
        else:
            if self.root.value == value: # root has the value
                ''' dummy node method - root value gets changed and other node
                    with that value will get removed from tree then set root to
                    dummys left which is the new origin'''
                dummy = Node(0)
                dummy.left = self.root
                result = self.root.remove(value, dummy)
                self.root = dummy.left
                return result
            else:
                return self.root.remove(value, None)

    def get_min(self):
        if self.root:# if tree not empty get minimmum value in tree
            return self.root.get_min()

    def get_max(self):
        if self.root: # if tree not empty get maximum value in tree
            return self.root.get_max()
        
def breath_first_search(node):
    # 2. print a tree using BFS and DFS
    queue = [node]
    while queue:
        current = queue[0]
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
        print(current.value, end=' ')
        queue.pop(0)

def inorder_dfs(node):
    # in order depth first traversal - left, root, right
    if node:
        inorder_dfs(node.left)
        print(node.value, end=' ')
        inorder_dfs(node.right)
        
def preorder_dfs(node):
    # pre order depth first traversal - root, left, right
    if node:
        print(node.value, end=' ')
        preorder_dfs(node.left)
        preorder_dfs(node.right)
        
def postorder_dfs(node):
    # post order depth first traversal - left, right, root
    if node:
        postorder_dfs(node.left)
        postorder_dfs(node.right)
        print(node.value, end=' ')

def determine_bst(node):
    # 3. determine if a tree is a binary search tree
    if not node:
        return True
    if node.left and node.left.get_min() > node.value:
        # value of left child greater than current node
        return False
    if node.right and node.right.get_max() < node.value:
        # value of right child lesser than current node
        return False
    if not determine_bst(node.left) or not determine_bst(node.right):
        # sub trees are not binary search trees
        return False
    return True

def determine_bst_efficient(node):
    # 3. determine if a tree is a binary search tree
    def is_bst(node, min_i, max_i):
        # set a range for trees, if values of node
        if not node:
            return True
        if node.value < min_i or node.value > max_i:
            # node value not in range
            return False
        return (is_bst(node.left, min_i, node.value - 1) and
                is_bst(node.right, node.value + 1, max_i))
    return is_bst(node, node.get_min(), node.get_max())

def smallest_element(node):
    # 4. find the smallest element in a BST
    return node.get_min()

def determine_sum_tree(node):
    # 6. determine if a tree is a sum tree
    left_side, right_side = 0
    if not node or (not node.left and not node.right):
        return 1
    ls = sum_of_sub(node.left)
    rs = sum_of_sub(node.right)
    if (node.value == ls + rs) and (sum_of_sub(node.left) and
        sum_of_sub(node.right) != 0):
        return 1
    return 0

def sum_of_sub(node):
    # question 6 helper method
    if not node:
        return 0
    return sum_of_sub(node.left) + node.value + sum_of_sub(node.right)

if __name__ == '__main__':
    pass