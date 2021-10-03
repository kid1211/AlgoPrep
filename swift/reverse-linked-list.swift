import Foundation
// Add any extra import statements you may need here


// Add any helper functions you may need here


class Node {
  var data: Int
  var nextNode: Node?
    
  init(data: Int, next: Node? = nil) {
    self.data = data
    self.nextNode = next
  }
}

private extension Node {
  func reverse() -> Node {
    // Write your code here
    var current: Node? = self
    var prevNode: Node?
    
    while current != nil {
      /*
        reversing:
        [NONON]next should point to current (next.next = current) 
        update current next, (current.next = previous) [also update prev]
        
        In my loop, i shoudl only myself!!!!
      */
      let nextNode = current!.nextNode
      current!.nextNode = prevNode
      prevNode = current
      
      // move to next iteration
      current = nextNode
    }
    
    return prevNode!

  }
}

// self is head










// These are the tests we use to determine if the solution is correct.
// You can add your own at the bottom.

struct NodeView: IteratorProtocol {
  var node: Node?
  mutating func next() -> Int? {
    defer { node = node?.nextNode }
    return node?.data
  }
}
 
extension Node: Sequence {
  typealias Element = Int
  func makeIterator() -> NodeView {
    return NodeView(node: self)
  }
}

private extension Node {
  static func from(array: [Int]) -> Node {
    var array = array
    var tail = Node(data: array.removeLast())
    for num in array.reversed() {
      tail = Node(data: num, next: tail)
    }
    return tail
  }
}

extension Node: Equatable {
  static func == (lhs: Node, rhs: Node) -> Bool {
    return Array(lhs) == Array(rhs)
  }
}

var testCaseNumber = 1

func check(_ expectedHead: Node, matches outputHead: Node) {
  let rightTick = "\u{2713}"
  let wrongTick = "\u{2717}"
    
  if expectedHead == outputHead {
    print("\(rightTick) Test #\(testCaseNumber)")
  } else {
    print("\(wrongTick) Test #\(testCaseNumber) Expected: \(Array(expectedHead)) Your output: \(Array(outputHead))")
  }
  testCaseNumber += 1
}

let head1 = Node.from(array: [1, 2, 8, 9, 12, 16])
let expected1 = Node.from(array: [1, 8, 2, 9, 16, 12])
let output1 = head1.reverse()
check(expected1, matches: output1)

let head2 = Node.from(array: [2, 18, 24, 3, 5, 7, 9, 6, 12])
let expected2 = Node.from(array: [24, 18, 2, 3, 5, 7, 9, 12, 6])
let output2 = head2.reverse()
check(expected2, matches: output2)

// Add your tests here
