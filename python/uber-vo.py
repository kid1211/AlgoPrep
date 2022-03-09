//Write a function that will print a text version of the view hierarchy.

//We expect the text version to be well formatted


// .subview <-

///let input = """
// {"ribTree":{"treePayload":{"nodes":[{"id":"Root"},{"id":"Main"},{"id":"Mode"},{"id":"ForceUpgrade"},{"id":"UberHome"},{"id":"UberHomeHub"},{"id":"MapLayer<ModularMapInteractable, MapLayerControllable>"},{"id":"UberHomeHubItemWrapper"},{"id":"UberHomeHubItemWrapper"},{"id":"UberHomeHubItemWrapper"},{"id":"UberHomeHubItemWrapper"},{"id":"UberHomeTopRow"},{"id":"LocationEditorEntryContainer"},{"id":"DefaultAccelerators"},{"id":"Viewable<Interactable, ViewControllable>"},{"id":"DestinationPrompt"},{"id":"ScheduledRidesDestinationEntryAccessory"}],"children":[[1],[2,3],[4],[],[5,6],[7,8,9,10],[],[11],[12],[13],[14],[],[15],[],[],[16],[]]},"type":"treePayload"}}
// """

// ribTree
class Node {
    var val: String
    var children = [Node?]()
    init(_ val: String, _ children: [Node?] = []) { 
        self.val = val 
        self.children = children
    }
}
//>>DecorView
// ├── LinearLayout
// │   ├── ViewStub
// │   └── FrameLayout
// │       └── FitWindowsLinearLayout
// │           ├── ViewStubCompat
// │           └── ContentFrameLayout
// │               └── CoordinatorLayout
// │                   ├── AppBarLayout
// │                   │   └── Toolbar
// │                   │       ├── AppCompatTextView
// │                   │       └── ActionMenuView
// │                   │           └── OverflowMenuButton
// │                   ├── FloatingActionButton
// │                   └── ConstraintLayout
// │                       ├── AppCompatImageView
// │                       ├── AppCompatImageView
// │                       └── AppCompatTextView
// ├── View
// └── View

let test1 = Node(
    "DecorView", 
    [
        Node("LinearLayout", [
            
            Node("FrameLayout", [
                Node("FitWindowsLinearLayout",
                [
                    Node("ViewStubCompat"),
                    nil,
                    Node("ContentFrameLayout", [
                        Node("CoordinatorLayout", [
                            Node("AppBarLayout"),
                            Node("FloatingActionButton"),
                            Node("ConstraintLayout")
                        ])
                    ])
                ])
            ]),
            Node("ViewStub")
        ]),
        Node("View"),
        Node("View")
    ])
// FrameLayout -> 2
// \t\t|
func printOutTreeHierachy(_ root: Node?) -> String {
    var res = ""
    func dfs(_ node: Node?, _ depth: Int, _ isLastNode: Bool) {
        // TODO: think about nil
        guard let node = node else { return } //"\n" 
        
        if depth > 0 {
            for _ in 0...depth {
                // print(node.children.count == 0)
                
                res += "\t|"
            }
            res += isLastNode ? "└" : "|"
            res +=  "--"
        }
        
        res += node.val + "\n"
        
        for i in 0..<node.children.count {
            let isLastNode = i == node.children.count - 1
            dfs(node.children[i], depth + 1, isLastNode)   
        }
    }
    // TODO: DecorView start situation
    dfs(root, 0, true)
    return res
}

print(printOutTreeHierachy(test1))