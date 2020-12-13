/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init() { self.val = 0; self.left = nil; self.right = nil; }
 *     public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
 *     public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
 *         self.val = val
 *         self.left = left
 *         self.right = right
 *     }
 * }
 */

class BSTIterator {
    private var sorted:[Int] = []
    private var idx = -1
    
    init(_ root: TreeNode?) {
        mapValToArray(root)
        print(sorted)
    }
    
    private func mapValToArray(_ root: TreeNode?) {
        guard let root = root else { return }
        mapValToArray(root.left)
        sorted.append(root.val)
        mapValToArray(root.right)
    }
    
    func next() -> Int {
        idx += 1
        return sorted[idx]
    }
    
    func hasNext() -> Bool {
        return idx < sorted.count - 1
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * let obj = BSTIterator(root)
 * let ret_1: Int = obj.next()
 * let ret_2: Bool = obj.hasNext()
 */

// # Your BSTIterator object will be instantiated and called as such:
// # obj = BSTIterator(root)
// # param_1 = obj.next()
// # param_2 = obj.hasNext()