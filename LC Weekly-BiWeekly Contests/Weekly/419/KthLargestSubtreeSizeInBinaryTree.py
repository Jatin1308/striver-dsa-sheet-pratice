class TreeNode:

    def __init__(self,val=0,left=None,right=None) -> None:
        self.val = val
        self.left = left
        self.right = right



def arrayToTree(arr):

    if not arr:
        return None
    
    root = TreeNode(arr[0])

    queue = [root]

    i = 1

    while i<len(arr):
        current = queue.pop(0)

        # Left Child
        if current:
            if i<len(arr) and arr[i] is not None:
                current.left = TreeNode(arr[i])
            queue.append(current.left)
            i+=1

            # rigth child

            if i < len(arr)  and arr[i] is not None:
                current.right = TreeNode(arr[i])
            queue.append(current.right)
            i+=1

    return root


def KthLargestPerfectSubtree(root,k):

    perfectSubTreeSizes = []

    def postOrder(node):

        if not node:
            return (True,0)  #(isPerfect, depth)
        
        leftPerfect, leftDepth = postOrder(node.left)
        rightPerfect,rightDepth = postOrder(node.right)

        if leftPerfect and rightPerfect and leftDepth == rightDepth:

            subtreeSize = (2**(leftDepth+1))-1
            perfectSubTreeSizes.append(subtreeSize)

            return (True, leftDepth+1)
        else:
            return (False,0)
    
    postOrder(root)

    perfectSubTreeSizes.sort(reverse=True)


    if len(perfectSubTreeSizes)>=k:
        return perfectSubTreeSizes[k-1]
    
    else:
        return -1
    

# [5,3,6,5,2,5,7,1,8,null,null,6,8], k = 2

root  = arrayToTree([5,3,6,5,2,5,7,1,8,None,None,6,8])

print(KthLargestPerfectSubtree(root,2))


