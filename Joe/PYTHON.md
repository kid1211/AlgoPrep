# Python notes

## HashSet

[Tutorial](https://www.w3schools.com/python/python_sets.asp)

```python
# Init
newSet = set()

# add
newSet.add('yo')

# check if contains
print( 'yo' in newSet )

# remove will throw error, discard won't
newSet.remove('yo')
newSet.discard('yo2')
```

## Char and Int Conversion

```python
char = chr(97)
integer = ord('a')
```

## String Manipulation

```python
"WAT".isupper() #true
'wat'.islower() #true
"WAT".lower() #wat
"wat".upper() # WAT

# filter space and other things
''.join(e for e in string if e.isalnum())
# filter anything but alphabet
''.join(e for e in string if e.isalpha())
```

## Integers

```python
max = sys.maxsize
min = -sys.maxsize - 1
```

## Hashset is just Dict

## Binary search - ooxx

左边是o右边是×，题目简化成为判断什么是o什么是x

1:24 video 2 -> ooxx境界
1:35 video 2 -> 画图具象化

## Mod in math

foolowing apply to '+', '-', '*'

(a + b) %c = a % c + b % c

## 有向的图和没有方向的图

因为没有方向的图有可能会形成一个换所以需要visited hash map 

## filter kind of

```python

start_nodes = [n for n in graph if indegree[n] == 0]

```

<!-- intersection two arrays II
maximum subarray -->

## substring subarray, window -> 同向双指针

同向双指针基本上都是o(n)，因为j不回头
i - j > s, 然后 i + 1 - k > s, 那么j和k什么关系？ k肯定比i大 不然那就包含了
同样的需要寄到心里面去 i - j的所有指 是 （j - i + 1)!

模板
```python
j = 0
for i in range(n):
    while j < n and 当前subarray 不满足条件:
        j += 1 # 拓展当前subarray
    
    if 当前满足条件:
        # 全局打擂台， 看看是不是最优秀的
    # 将numsi] 移出array，其实就是喜剧for loop

```

- [kth-largest-in-n-arrays](https://www.lintcode.com/problem/kth-largest-in-n-arrays)
  - not sorted 
    - quick selected 非在线版本
    - 在线版本 heap
  - sorted 
    - k merge (heap) - not the best k比较小
    - 二分答案 k比较大

## Union Find

O(1) Union, and o(1) find
父亲表示法， 用哈希表记录每个节地那的父亲是谁，初始化的时候可以指向自己或者空 

```python
def find(self, node):
  while self.father[node] != node:
    node = self.father[node]
```

上面的问题是 做不到o1的查询 所以每次查询的时候要做路径压缩

```python
# 递归
def find(self, node):
  if node == self.father[node]:
    return node
  
  self.father[node] = self.find(self.father[node])
  return self.father[node]

# 非递归 尽量非递归
def find(self, node):
  path = []
  while self.father[node] != node:
    path.append(node)
    node = self.father[node]

  for n in path:
    self.father[n] = node
  
  return node

# union
def union(self, a, b):
  self.father[self.find(a)] = self.find(b)

class UnionFind:
  def __init__(self, n):
    self.father = {}
    for i in range(1, n + 1):
      self.father[i] = i 
```

## minimm spanning tree
先把边排序，从小到大 看看边有没有连通，没有就连通
基本上连通的问题都是union find

## union find 特点

1. 合并两个集合
2. 查询某个元素所在集合
3. 判断两个元素是否在同一个集合
4. 获得某个集合的元素个数
5. 统计当前集合个数
6. 只能是无向图maybe

## Trie

```python
class TrieNode:
  def __init__(self):
    self.children = {}
    self.is_word = False

class Trie
  def __init(self):
    self.root = TrieNode()

  def insert(self, word):
    node = self.root
    # 有点牛逼 node和c一起同步往下走
    for c in word:
      if c not in node.children:
        node.children[c] = TrieNode()
      node = node.children[c]
    node.is_word = True
  
  def find(self, word):
    node = self.root
    for c in word:
      node = node.chldren.get(c)
      if node is None:
        return None
    return node

```

## Segmental Tree

start/end/sum/leftNode/rightNode

```python
class NumArray:

    def __init__(self, nums: List[int]):
        if not nums:
            return
        self.root = self.buildTree(nums, 0, len(nums) - 1)

    def update(self, i: int, val: int) -> None:
        self.updateDFS(self.root, i, val)

    def updateDFS(self, node, i, val):
        if not node:
            return

        start, end = node.start, node.end
        if start == end == i:
            node.sums = val
            return

        mid = (start + end) // 2

        if i <= mid:
            self.updateDFS(node.left, i, val)
        else:
            self.updateDFS(node.right, i, val)

        node.sums = node.left.sums + node.right.sums

    def sumRange(self, i: int, j: int) -> int:
        return self.sumRangeDFS(i, j, self.root)

    def sumRangeDFS(self, i, j, node):
        start, end = node.start, node.end
        if start == i and end == j:
            return node.sums

        mid = (start + end) // 2
        # check i and j both align on oneside
        # noted that mid is grounded it,  so i need to atleast
        # greater than start, think of i,j = 2, 3
        if j <= mid:
            return self.sumRangeDFS(i, j, node.left)
        elif i > mid:
            return self.sumRangeDFS(i, j, node.right)
        else:
            return self.sumRangeDFS(i, mid, node.left) + self.sumRangeDFS(mid + 1, j, node.right)

    def buildTree(self, nums, start, end):
        if start == end:
            return SegmentalTreeNode(start, end, nums[start])

        mid = (start + end) // 2
        left = self.buildTree(nums, start, mid)
        right = self.buildTree(nums, mid + 1, end)
        return SegmentalTreeNode(start, end, left.sums + right.sums, left, right)

    def printTree(self, node):
        if not node:
            return

        self.printTree(node.left)
        print(node)
        self.printTree(node.right)


class SegmentalTreeNode:
    def __init__(self, start, end, sums, left=None, right=None):
        self.start = start
        self.end = end
        self.sums = sums
        self.left = left
        self.right = right

    def __repr__(self):
        if self is None:
            return "Node is None"
        return f"<Node start:{self.start} end:{self.end} sums:{self.sums}>"
```

## 强化算法版第二课

## heap + hashmap

## trapping water

第一层: 看左右最高值
第二层: 双指针记录最高值，然后靠近矮的可以确定
第三层： 2d的

## trapping water II

1. constructed a ring with all the outer most element
2. find the lowest in the ring
3. compare it with the inner ring, if it is smaller, shrink the ring on this part
4. else you get your water, then move on

## maximum rectangle 2D

- 一行一行来看
- 每一行都对上的书字加起来 
- maximum submax, 也是 把三维的图变成一维

## max tree

```pythong
class Solution:
  def maxTree(self, A):
    if not A:
      return None
    
    nodes = [TreeNode(num) for num in A + [sys.maxsize]]
    stack = []

    for index, num in enumerate(A + [sys.maxsize]):
      while stack and A[stack[-1]] < num:
      top = stack.pop()
      left = A[stack[-1]] if stack else sys.maxsize

      if left < num:
        nodes[stack[-1]].right = nodes[top]
      else:
        nodes[index].left = nodes[top]
      stack.append(index)
    
    # sys.maxsize's left child is the maximum number
    return nodes[-1].left
```

## 有序哈希表 - LRU Cache

collections.OrderedDict

## Sliding Window mediium

红黑树！！！ pythong！！tree map
1. 维护两个堆
2. 小的那一半做一个最大堆， 大的那一半用一个最小堆 红黑树

## sliding window maximum

1. 红黑树
2. min stack 类似的方法，， 用deque
3. deque是双向链表实现的

## min stack

vs heap? pop不一样
 
两个stack， 一个是实际数据，另一个是当时的最小值

## sweep line

1. 事件往往是以区间的形式存在
2. 区间两端代表事件的开始和结束
3. 需要排序

扫描线的要点， 将起点和终点打散排序
[[1,3], [2,4]] -> [[1, start], [2, start], [3, end],[4,end]]
1. break down之后排序
2. start+1,end-1, 就好了
4. start/end可以有个小技巧用-1 和1 帮助排序

## heap

- siftup 我比我的父亲要小
- siftdown 我比我的儿子要小

## red-black tree

need to do mind map
hash-heap implmentation -> TheSkylineProblem

## find peak element II

1. 中间的地方找到peak 然后走下去 （去的那方向继续二分）
2. 交替二分

## +1 <=

记得总结， 二分法是+1， quick sort是<=

## 二分答案

```python
# 1 确定答案的范围
start, end = 答案可能的值域范围

while start + 1 < end:
  # 猜答案
  mid = (start + end) // 2

  # 3. 检测答案
  if should_be_smaller(mid): 
    end = mid #4. 调账范围
  else:
    start = mid #4. 调整范围

# 最后简则start 和end

偏小先检查start
偏大的先检查end
```

## find the duplicate number

1. 快慢指针，想象里面的数字是next index 肯定有环
2. first number that smaller_than_or_equal_to(number) > number   nlogn

## maximum average subarray

思路是让他套一下 看看怎么样
1. sliding window 让他符合一个什么条件，这个题目没有
2. prefix sum、
3. average的问题可以总体减去平均值，然后sum=0

## 滚动数组

- house robber I/II
- Maximal Square I/ii

- fibonacci
  - 传统1: f[i] = f[i-1] + f[i -2]
  - 传统2: c = a+b; a = b; b = c
  - 新方法: f[i%3] = f[(i-1)%3] + f[(i-2)%3]

## 记忆化搜索

- longest continous increasing subsequence
- coin in a line i/ii/iii
- 什么时候用记忆化搜索？
- 状态转移特别麻烦，不是顺序性的
- 初始化状态不是很容易找到
- 缺点
  - 耗费更多的空间，无法使用滚动数组优化
  - 地柜深度可能会很深

## 其他类型的动态规划

- 矩阵形
- 博弈形
- 区间型

## 动态规划的4点要素

- 状态 state
  - 最优解/maximum/minimum
  - Yes/No
  - Count(*)
- 方程 function
- 初始化 initialization 
-. 答案 answer

## house robber

- 序列性动态规划
- state
  - f[i] 表示前i个房子中，偷盗的最大价值
- function
  - f[i] = 1. A[i-1] + max(f[i-2]...f[i])偷到地i个房子
  -        2. f[i-1]不都地i个房子
  - 总结为 f[i] = max(f[i-1], f[i-2] + A[i-1])
- init 通常比数组要大1
  - f[0] = 0
  - f[i] = A[0]
- anser
  - f[n]

## maximal square

- 矩阵类型的题目
  - 正方形用右下角作为定位角
  - 长方形用左上角和右下角作为定位角
- state: f[i][j] 表示已i,j 为右下角的正方形的最大边长
- function: f[i][j] = min(f[i-1][j], f[i][j-1], f[i-1][j-1]) + 1 if matrix[i][j] == 1 else 0
- init: f[0][i] = matrix[0][i]  f[i][0] = matrix[i][0]
- ans: max(f[i][j])
- function Optimal: i % 2, j doesn't
- f[i][j] = min(f[(i-1)%2][j], f[i%2][j-1], f[(i-1)%2][j-1]) + 1 if matrix[i][j] == 1 else 0
- f[0][i] = matrix[0][i] \\\\   f[i%2][0] = matrix[i][0]

## 动态规划的视线方式

- 循环（从小岛大递推）
- 记忆化搜索（从大到小的搜索）
  - 画搜索树
  - 万金油

## 博弈类dp

- state: 先手是否能获胜/能够获胜获得的最大利益
- function: 循环美剧先手的策略可能性
- initialization: 最极限、最小的状态下的先手的值
- answer: 整个问题先手是否可能获胜
- notes: 先思考最小的状态，然后思考打的状态往小的递推，非常适合记忆化搜索

## coins in line II

- reverse step
- look at answer

## coins in line III

- state
  - dp[i][j]现在地i道第j的硬币，先手可以最多取走的硬币总价值
- function
  - sum[i][j] 表示到第i到第j的硬币价值总和
  - dp[i][j] = max(sum[i][j]-dp[i+1][j], sum[i][j] - dp[i][j-1])
  - //或者携程 dp[i][j] = sum[i][j] - min(dp[i+1][j], dp[i][j-1 ])
- initialize
  - dp[i][j] = coins[i]
- answer
  - dp[0][n-1]

- 动态规划右边的值要比左边的先计算，所以顺序就看这个

## 动态规划下

- 区间类dp
  - stone game
  - burst ballons
  - scramble string *
- 匹配类dp
  - longest common subsequence
  - edit distance
  -k edit distance
  - distinct subquence
  - interleaving string
- 背包类dp
  - backpack i
  - backpack ii
  - k sum

## 区间类dp

1. 求一段区间的解 max/min/count
2. 转移方程通过区间更新
3. 大区间的值依赖于小区间

## Stone-Game

- state: dp[i][j] 表示ith到jth石子合并到一起的最小花费
- function: 
  - 预处理 sum[i][j], 表示ith到jth所有价值和
  - dp[i][j] = min(dp[i][k] + dp[k+1][j] + sum[i][j])对于所有k处于 {i, j - 1}
- initialize for each i dp[i][i] = 0
- answer dp[0][n-1]

## 区间动态规划的三种实现方式

1. 先循环区间长度，再循环起点位置 - hard to remember  
2. 起点倒过来循环，重点正过来循环
3. 记忆化搜索

目的：先计算小区间,在计算大区间

```python
# 1
for length in range(2, n + 1):
  for i in range(n - length + 1):
    j = i + length - 1
    # now we get (i, j)

# 2
for i in range(n - 1, -1, -1):
  for j in range(i, n):
    # now we get (i, j)

# 3
def memo_search(self, A, i, j, range_sum, memo):
  if i == j:
    return 0
  
  if (i, j) in memo:
    return memo[(i, j)]
  
  score = sys.maxsize
  for k in range(i, j):
    left = self.memo_search(A, i, k, range_sum, memo)
    right = self.memo_search(A, k + 1, j, range_sum, memo)
    score = min(score, left + right + range_sum[i][j])

  memo[(i, j)] = score
  return score
```

## 四边形不等式 w6 30:00

- stone game
- copy book

## Burst Ballons - Interval

从大到小，吹最后一个球的时候是确定的 那个乘以两个1，那就倒退

- state  dp[i][j] 表示把ith到jth个气球打包的最大价值
- function
  - k 属于i,j 表示第k号气球最后打包
  - score = arr[i -1 ] * arr[k] * arr[j + 1]
  - dp[i][j] = max(dp[i][k-1] + dp[k+1][j] + score)
- intiatization dp[i][i] = arr[i-1] * arr[i] * arr[i+1]
- answer: dp[0][n-1]

上面的太麻烦了 进阶到下面的

- 讲两端加上 1
- state: dp[i][j] 表示把(i+1)th到(j-1)th气球打包，剩下i,j的最大收益
- function:
  - 对于所有k属于 {i+1, j -1}, 表示kth气球最后打包
  - score = arr[i] * arr[k] * arr[j]
  - dp[i][j] = max(dp[i][k] + dp[k][j] + score)
- initialization: dp[i][i] = 0
- answer: dp[0][n-1]

## Scramble String 还有动归四讲

## 匹配性动态规划 

- state: f[i][j] 代表了第一个sequence 的前i个数字/字符, 配上第二个sequnce的前j个
- function: f[i][j] = 研究第i个和第j个的匹配关系（上， 左，左上， 三个状态)
- initialization : f[i][0] 和 f[0][j]
- answer f[n][m] min/max/数目/存在关系
  - n + 1 或 m + 1， 记得考虑空字符串
- n = s1.length()
- m = s2.length()
- 阶梯技巧花矩阵,填写矩阵

## longest common subsequence

- state: f[i][j] 表示前i个字符配上钱j个字符的lcs的长度
- function: f[i][j] = max(f[i-1][j], f[i][j -1], f[i -1][j -1] + 1) // a[i-1] == b[j-1]
  - max(f[i-1][j], f[i][j -1]) // a[i-1] != B[j-1]
- initialize: f[i][0] = f[0][j] = 0
- answer: f[n][m]

## edit distance

• state: f[i][j]表示A的前i个字符最少要用几次编辑可以变成B的前j个字符
• function: f[i][j] = MIN(f[i-1][j]+1, f[i][j-1]+1, f[i-1][j-1]) // A[i - 1] == B[j - 1]
• = MIN(f[i-1][j]+1, f[i][j-1]+1, f[i-1][j-1]+1) // A[i - 1] != B[j - 1]
• initialize: f[i][0] = i, f[0][j] = j
• answer: f[n][m]

## Distinct Subsequence

• state: f[i][j] 表示 S的前i个字符中选取T的前j个字符，有多少种方案
• function: f[i][j] = f[i - 1][j] + f[i - 1][j - 1] // S[i-1] == T[j-1]
• = f[i - 1][j] // S[i-1] != T[j-1]
• initialize: f[i][0] = 1, f[0][j] = 0 (j > 0)
• answer: f[n][m] (n = sizeof(S), m = sizeof(T))

## Interleaving String

state: f[i][j]表示s1的前i个字符和s2的前j个字符能否交替组成s3的前i+j个字符
• function: f[i][j] = (f[i-1][j] && (s1[i-1]==s3[i+j-1]) ||
• (f[i][j-1] && (s2[j-1]==s3[i+j-1])
• initialize: f[i][0] = (s1[0..i-1] == s3[0..i-1])
• f[0][j] = (s2[0..j-1] == s3[0..j-1])
• answer: f[n][m], n = sizeof(s1), m = sizeof(s2)

## 背包类dp

1. 用值作为dp维度
2. dp过程就是天蝎矩阵
3. 可以滚动数组优化

## backpack I

State:
• f[i][S] “前i”个物品，取出一些能否组成和为S
• Function:
• a[i-1] 是第i个物品下标是i-1
• f[i][S] = f[i-1][S - a[i-1]] or f[i-1][S]
• Intialize:
• f[i][0] = true; f[0][1..target] = false
• Answer:
• 检查所有的f[n][j]
• O(n*S) ， 滚动数组优化

## backpack II

• 状态 State
• f[i][j] 表示前i个物品当中选一些物品组成容量最多为j的最大价值 (小于等于j)
• 方程 Function
• f[i][j] = max(f[i-1][j], f[i-1][j-A[i-1]] + V[i-1]);
• 初始化 Intialization
• f[0][0]=0;
• 答案 Answer
• f[n][s]
• O(n*s)

## backpack IV

State:
• f[i][S] “前i”个物品，取出一些能否组成和为S
• Function:
• a[i-1] 是第i个物品下标是i-1
• k 是第i个物品选取的次数
• f[i][S] = f[i-1][S - k*a[i-1]] or f[i-1][S]
• Intialize:
• f[i][0] = true; f[0][1..target] = false
• Answer:
• 答案是f[n][S]

## k sum

• n个数，取k个数，组成和为target
• State:
• f[i][j][t]前i个数取j个数出来能否和为t
• Function:
• f[i][j][t] = f[i - 1][j - 1][t - a[i-1]] + f[i - 1][j][t]
• Intialization
• f[i][0][0] = 1
• Answer
• f[n][k][target]

## Minimum Adjustment Cost

• State:
• f[i][v] 前i个数，第i个数调整为v，满足相邻两数<=target，所需要的最小代价
• Function:
• f[i][v] = min(f[i-1][v’] + |A[i]-v|, |v-v’| <= target)
• Answer:
• f[n][a[n]-target~a[n]+target]
• O(n * A * T)

## summary dp

区间类DP问题
• 从大到小去思考
• 主要是通过记忆化来直观理解DP的思路
• 双序列类DP问题
• 二维数组
• 画出矩阵的表格，填写矩阵
• 背包DP问题
• 用值作为DP维度
• DP过程就是填写矩阵
• 可以滚动数组优化

## SubArray Sum

同向双指针 vs prefix sum

同向双指针可以想象为一个窗口，找一个方法让这个窗口越来越大
用prefix sum, 然后查某个东西相等，所以用hashmap
subarray-sum-closest: 最接近的用tree set 红黑树 比他小的最大的书比他大的最小堆额书
(tree set找的是值) vs (单调栈找的是位置)
这道题可以prefix sum 然后排个序和下表一起拍

## 考虑一下 关键字对应的算法

## continuous-subarray-sum

1. 本来知道的方法
2. 扫一遍，遇到前面的前缀和是负数就扔掉用自己从新来

## nlogn 方法

还可以可以是算出区别带着下标sort

## continuous-subarray-sum-ii

- 枚举中心线
- 复制一遍

## quick select

最差情况-> n*n

## wiggle sort I && II

I: 小的和大的换个位置 差不多这意思
II: 思考的是大的部分和小的部分可以倒序如果sorted， 那我们真的需要完全sorted吗？不需要的话就rainbow sort 分三个部分 

## heap

https://www.youtube.com/watch?v=t0Cq6tVNRBA

balanced binary tree (top to bottom, left to write to fill)

- Add
  - add to the first spot
  - sift up (check its father swap is smaller)
- remove
  - take the last value put it on root
  - sift down (swap wich the smallest children)

- represent heap in array
- (index - 2) // 2 is the parent
- index *2 + 1 is left child
- index *2 + 2 is the right child

## BitWise

<!-- need exactly one -->
0 ^ 0 = 0
0 ^ 1 = 1 need exactly 1
1 ^ 1 = 0

0 | 0 = 0
0 | 1 = 1 need one of it
1 | 1 = 1

0 & 0 = 0
0 & 1 = 0
1 & 1 = 1 need both

## tiny url

method 1: hash(md5) too many collision
method 2: random + check if exist  两个dblist存两条
method 3: sql only, require incremental id, turn it into values 只需要一个对应关系

```Java
int shortURLtoID(string shortURL) {
  int id = 0
  for (int i = 0; i < shortURL.length(); ++i>) {
    id = id * 62 + toBase62(shortURL.charAt(i));
  }
  return id;
}

String idToShortURL(int id) {
  String chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
  String short_url = "";
  while (id > 0) {
    short_url =chars.charAt(id % 62) + short_url;
    id = id / 62;
  }
  while (short_url.length() < 6) {
    short_url = "0"+ short_url;  
  }
  return short_url;
}
```

## tiny url - scale

sharding:
vertical肯定不行只有两个column
horizontal唯一

如果是一个long对应一个short:
用short作为sharding key? 不行,因为避免重复的时候需要查long有没有在,每次都要广播会bottleneck
用long作为sharding key? short2long会很慢,而且这个经常有, 但是没办法只能这么做

比较好的方法:

- 如果随机生成的算法
  - 两张表单一张long2short 一张存储short2long
  - 每个映射关系寸两份,则可以同时支持long2short and short2long的查询
- 如果使用base62的进制转换法
  - 这里有一个很严重的问题是,多台机器没有办法实现自增id, 一般只支持单带服务器的自增id

如果是一个long可以对应多个short:
用short作为sharding key? 可以
用long作为sharding key? short2long会很慢,而且这个经常有

比较好的方法:

- 使用cache缓存所有的long to short
- 在为一个long url创建short的时候, 如果cache miss则直接创建新的short url 即可
- sharding是啥? 这种情况下因为一个long好几个short所以肯定不是short作为primary key
- primary key是自增id,long为复合索引的第二索引

-下面有一个有没一点的方法

## 怎么解决全局自增id

- 一种方法: 有一台数据库专门做自增id
  - 不存储真是数据,也部分其他查询
  - 为了避免单点失效(single point failure) 可能需要多台数据库
- 另一种结局方法是用zookeeper
  - 但是使用全局自增id的方法并不是结局tiny的最佳方法
  - zookeerp可以看资料

## 基于base62的方法下的sharing key策略

- 使用hash(long_url) % 62 作为shardingkey
- 并将 hash(long_url) % 62 直接放到short url里面
- 如果原来的 shortkey是ab1234的话现在的shortkey是
  - hash(long_url) % 62 + AB1234
  - 如果hash(long_url) % 62 是 0 那就是0AB1234
- 这样可以同时通过short_url和long_url得到sharding key
- 确定数据库的机器商户木不能超过62   

比如说0AB1234, 去0机器 去找ab1234

还要优化?
- master slave的模式,因为多读少写是可以的,但是有时候还是会有不一致的问题
- 另一个就是按照网站分类的在不一样的服务器