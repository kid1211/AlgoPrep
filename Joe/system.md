# 系统设计

## W1

producer-consumer pattern
装一下redis
装一下rabbitq
装一下sql

MAU/2 约等于 DAU

## W2

cache + db
锁没有用因为多台机器
best practice: database先set再cache delete
因为用户系统更多是读多写少
