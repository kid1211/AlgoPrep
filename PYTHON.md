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

## trapping water I
从左往右的最大值，和从右往左的最大值就能决定本格子有多少水