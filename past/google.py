google self driving car

forward or backward, 
what time bus?
pull from command bus (acc/reverse) (double the speed every second)(brake to dead 0) (
[direct] changes)


AAAAA R AAA R A

  0    5   10   15   20   25   30   35
  |----+----+----+----+----+----+----+
A ->
A  -->
A    ---->
A        -------->
A                ----------------> (31)
R                                |
A                               <-
A                             <--
A                    (24) <----
R                         |
A                         -> (25)
  |----+----+----+----+----+----+----+
  0    5   10   15   20   25   30   35

f("AAAAARAAARA") == 25
f("A") == 1
f("AA") == 3
f("AAA") == 7 (1 + 2 + 4)
f("ARA") == 0 (1 + -1)
f("RA") == -1

def parseCommand(commands):
  noOfA = 0
  direction = 1 # -1 when reverse
  res = 0
  for cmd in command:
    if cmd == 'A':
      res += 2 ** noOfA * direction
      noOfA += 1
    else:
      direction *= -1
      noOfA = 0
  return res

---
google map (a, p)

g(25) == "AAAAARAAARA"
g(1) == "A"
g(3) == "AA"


# exact location

#  1  2  3  4  5  6  7   8
# 01 02 04 08 16 32 64 128 256 512  -- 2**(n-1)
# 01 03 07 15 31 63 127             -- 2**n - 1
g(25) -> 
g(25) + g(0) or 
g(24) + g(1) or 
g(3) + g()

def parseCommand2(distance):
  canadiates = []
  rolling = 0
  for i in range(distance):
    rolling += 2 ** i
    canadiates += [ (rolling, "A" * i) ]  # AA => 3
    canadiates += [ (-rolling, "R" + "A" * i) ] # RAA => -3
    
  #[ (1, "A"), (-1, "RA"), (4, "AA"), (4, "RAA") ]
  pass

parseCommand3(5) ->
  dfs(5, [], [])
  dfs(4, [1], [])
  dfs(3, [1, 1], [])
  dfs(2, [1, 1, 1], [])
  dfs(1, [1, 1, 1, 1], [])
  dfs(0, )
  

  # [3, -1, 3, -1, 3, -1, 3, -1, 3, ...]

# one exit crit
# only add the res if it is flping (dfs) <- 
#   [1] [2] [3] [4]
# [1] [-2] [-3] [-4]
# anser would finding the shortes step in the output <- optimal


5: AARRARRA -> [2, 1, 1]
5: AAARAARA -> [3, -2, 1]
5: AARAARA -> [2, -2, 1]

def parsCommand3(distance):
  MAX_NUMBER = 8 # guess game
  def dfs(distance, curr, res):
    if distance == 0:
      res += [curr]
      return
    
    if distance > 2** MAX_NUMBER or distance < -2** MAX_NUMBER:
      return
    
    for i in range(1, MAX_NUMBER):
      dfs(distance - 2** i - 1, curr + [i], res)
      dfs(distance + 2** i - 1, curr + [-i], res)
    
  
  res = []
  dfs(distance, [], res)
  
  output =[]
  for combination in res:
    oneAns = ""
    for step in combination:
      step = step if step > 0 else -step

    i => i * "A"
    -i => "R" + "A" * i
    output += [oneAns]
    
  # turn res: [interger] => command
  return res
 