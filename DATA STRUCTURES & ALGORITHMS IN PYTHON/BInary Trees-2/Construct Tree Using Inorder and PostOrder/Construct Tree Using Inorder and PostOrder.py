For a given postorder and inorder traversal of a Binary Tree of type integer stored in an array/list, create the binary tree using the given two arrays/lists. You just need to construct the tree and return the root.
Note:
Assume that the Binary Tree contains only unique elements. 
Input Format:
The first line of input contains an integer N denoting the size of the list/array. It can also be said that N is the total number of nodes the binary tree would have.

The second line of input contains N integers, all separated by a single space. It represents the Postorder-traversal of the binary tree.

The third line of input contains N integers, all separated by a single space. It represents the inorder-traversal of the binary tree.
Output Format:
The given input tree will be printed in a level order fashion where each level will be printed on a new line. 
Elements on every level will be printed in a linear fashion. A single space will separate them.
Constraints:
1 <= N <= 10^4
Where N is the total number of nodes in the binary tree.

Time Limit: 1 sec
Sample Input 1:
7
4 5 2 6 7 3 1 
4 2 5 1 6 3 7 
Sample Output 1:
1 
2 3 
4 5 6 7 
Sample Input 2:
6
2 9 3 6 10 5 
2 6 3 9 5 10 
Sample Output 2:
5 
6 10 
2 3 
9 





import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def buildTreePostOrder(postorder, inorder):
    if len(postorder) == 0:
        return None

    rootData = postorder[len(postorder) - 1]
    root = BinaryTreeNode(rootData)
    rootIndex = -1

    for i in range(0, len(inorder)):
        if inorder[i] == rootData:
            rootIndex = i
            break
    if rootIndex == -1:
        return None

    leftInorder = inorder[:rootIndex]
    rightInorder = inorder[rootIndex + 1:]

    x = len(leftInorder)
    leftPostorder = postorder[:x]
    rightPostorder = postorder[x:len(postorder) - 1]

    root.left = buildTreePostOrder(
        leftPostorder, leftInorder)    # Where to call recursion?
    root.right = buildTreePostOrder(rightPostorder, rightInorder)

    return root


def printLevelATNewLine(root):
    # Given a binary tree, print the level order traversal. Make sure each level
    # start in new line.
    if root == None:
        return
    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)
    while not inputQ.empty():
        while not inputQ.empty():
            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left != None:
                outputQ.put(curr.left)
            if curr.right != None:
                outputQ.put(curr.right)
        print()
        inputQ, outputQ = outputQ, inputQ


# Main
n = int(input())
postOrder = [int(i) for i in input().strip().split()]
inorder = [int(i) for i in input().strip().split()]
root = buildTreePostOrder(postOrder, inorder)
printLevelATNewLine(root)

