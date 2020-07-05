# 系统设计

## W1

producer-consumer pattern
装一下redis
装一下rabbitq
装一下sql
装一下nosql 好友关系/newsfeed

MAU/2 约等于 DAU

- [design-twitter](https://www.lintcode.com/problem/design-twitter)

## W2

cache + db
锁没有用因为多台机器
best practice: database先set再cache delete
因为用户系统更多是读多写少

- cache aside 读多写少
- cache through 写多读少

- [friendship-service](https://www.lintcode.com/problem/friendship-service)
- [memcache](https://www.lintcode.com/problem/memcache)
- [mini-cassandra](https://www.lintcode.com/problem/mini-cassandra)
- [lfu-cache](https://www.lintcode.com/problem/lfu-cache)
- [lru-cache](https://www.lintcode.com/problem/lru-cache)

## W3

- [consistent-hashing](https://www.lintcode.com/problem/consistent-hashing)
- [load-balancer](https://www.lintcode.com/problem/load-balancer)
- [consistent-hashing-ii](https://www.lintcode.com/problem/consistent-hashing-ii)
- [web-logger](https://www.lintcode.com/problem/web-logger)
- [rate-limiter](https://www.lintcode.com/problem/rate-limiter)