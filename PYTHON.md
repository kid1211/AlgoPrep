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

O(1) Union, and o(1) find
父亲表示法， 用哈希表记录每个节地那的父亲是谁，初始化的时候可以指向自己或者空 