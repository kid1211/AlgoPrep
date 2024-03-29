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

## W4

- [tiny-url](https://www.lintcode.com/problem/tiny-url/description?_from=ladder&&fromId=75)
- [tiny-url-ii](https://www.lintcode.com/problem/tiny-url-ii/description?_from=ladder&&fromId=75)

## W5

- [geohash-ii](https://www.lintcode.com/problem/geohash-ii/description?_from=ladder&&fromId=75)
- [geohash](https://www.lintcode.com/problem/geohash/description?_from=ladder&&fromId=75)
- [mini-uber](https://www.lintcode.com/problem/mini-uber/description?_from=ladder&&fromId=75)
- [mini-yelp](https://www.lintcode.com/problem/mini-yelp/description?_from=ladder&&fromId=75)

## W6

- [pub-sub-patter](https://www.lintcode.com/problem/pub-sub-pattern/description?_from=ladder&&fromId=75)

## W7

- [heart-beat](https://www.lintcode.com/problem/heart-beat/description?_from=ladder&&fromId=75)
- [gfs-client](https://www.lintcode.com/problem/gfs-client/description?_from=ladder&&fromId=75)

## W8

- [standard-bloom-filter](https://www.lintcode.com/problem/standard-bloom-filter/description?_from=ladder&&fromId=75)
- [counting-bloom-filter](https://www.lintcode.com/problem/counting-bloom-filter/description?_from=ladder&&fromId=75)
- [merge-k-sorted-arrays](https://www.lintcode.com/problem/merge-k-sorted-arrays/?_from=ladder&&fromId=75)

## W9

- [sort-integers-map-reduce](https://www.lintcode.com/problem/sort-integers-map-reduce/description?_from=ladder&&fromId=75)
- [top-k-frequent-words-map-reduce](https://www.lintcode.com/problem/top-k-frequent-words-map-reduce/description?_from=ladder&&fr)
- [n-gram-map-reduce](https://www.lintcode.com/problem/n-gram-map-reduce/description?_from=ladder&&fromId=75)
- [inverted-index-map-reduce](https://www.lintcode.com/problem/inverted-index-map-reduce/description?_from=ladder&&fromId=7)
- [anagram-map-reduce](https://www.lintcode.com/problem/anagram-map-reduce/description?_from=ladder&&fromId=75)
- [word-count-map-reduce](https://www.lintcode.com/problem/word-count-map-reduce/description?_from=ladder&&fromId=75)
- [inverted-index](https://www.lintcode.com/problem/inverted-index/description?_from=ladder&&fromId=75)
- [sparse-matrix-multiplication](https://www.lintcode.com/problem/sparse-matrix-multiplication/description?_from=ladder&&fromI)

## W10

- [google-suggestion-map-reduce](https://www.lintcode.com/problem/google-suggestion-map-reduce/description?_from=ladder&&fromI)
- [inverted-index](https://www.lintcode.com/problem/inverted-index/description?_from=ladder&&fromId=75)
- [implement-trie-prefix-tree](https://www.lintcode.com/problem/implement-trie-prefix-tree/description?_from=ladder&&fromId=)
- [typeahead](https://www.lintcode.com/problem/typeahead/description?_from=ladder&&fromId=75)
- [web-crawler](https://www.lintcode.com/problem/web-crawler/description?_from=ladder&&fromId=75)
- [trie-service](https://www.lintcode.com/problem/trie-service/description?_from=ladder&&fromId=75)
- [url-parser](https://www.lintcode.com/problem/url-parser/description?_from=ladder&&fromId=75)
- [trie-serialization](https://www.lintcode.com/problem/trie-serialization/description?_from=ladder&&fromId=75)