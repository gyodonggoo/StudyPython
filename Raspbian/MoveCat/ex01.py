num = 1
prev = 0
cur = 1
while num <10:
    next = cur + prev
    print("%2d %2d"% (num, next))
    prev = cur
    cur = next
    num += 1
