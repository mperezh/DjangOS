
from copy import copy


def fifo(request, start):
    s = 0                     # initialize to 0
    position = start            # set current position = start
    order = list()              # creates empty list of name order
    order.append(start)         # adds Start to end of list order
    for i in request:           # i is the current element in the list(first loop i = 95)
        s += abs(i-position)  # sum = sum + (distance of current position from next position)
        position = i            # set position new position (i)
        order.append(i)         # Add i to the end of the list order
    return order, s


def scan(request, start):
    n = len(request)
    order = list()
    request_tmp = copy(request)
    request_tmp.sort()
    if start != 0 and start < request_tmp[n-1]:
        request_tmp.append(0)
    p = len(request_tmp)

    i = start - 1
    order.append(start)
    while i >= 0:
        for j in range(0,p):
            if request_tmp[j] == i:
                order.append(i)
        i -= 1

    k = start + 1
    while k < 200:
        for l in range(0,n):
            if request[l] == k:
                order.append(k)
        k += 1

    s = 0
    for p in range(0, len(order) - 1):
        s += abs(order[p] - order[p+1])
    return order, s


def cscan(request, start):
    n = len(request)
    order = list()
    request_tmp = copy(request)
    request_tmp.sort()
    if start != 0 and start < request_tmp[n-1]:
        request_tmp.append(0)
    p = len(request_tmp)

    i = start - 1
    order.append(start)
    while i >= 0:
        for j in range(0, p):
            if request_tmp[j] == i:
                order.append(i)
        i -= 1

    k = 199
    while k > start:
        if k == 199:
            order.append(k)
        for l in range(0, n):
            if request[l] == k:
                order.append(k)
        k -= 1

    s = 0
    sorted_req = copy(order)
    sorted_req.sort()
    for p in range(0, len(order) - 1):
        if order[p] != sorted_req[0]:
            s += abs(order[p] - order[p+1])
    return order, s
