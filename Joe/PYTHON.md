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

# filter kind of

```python

start_nodes = [n for n in graph if indegree[n] == 0]

```

<!-- intersection two arrays II
maximum subarray -->

# substring subarray, window -> 同向双指针

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

# Union Find

## 实现
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

# Trie

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

# 强化算法版第二课

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

## Stron-Game

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