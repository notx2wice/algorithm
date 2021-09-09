# !/usr/bin/python3

def solution(k, num, links):
    start_k = len(num)
    leafs = set()
    r_link = [-1 for _ in range(len(num))]
    idx = 0
    for link in links:
        if link[0] == -1 and link[1] == -1 :
            leafs.add(idx)
        if link[0] != -1 :
            r_link[link[0]] = idx
        if link[1] != -1:
            r_link[link[1]] = idx       
        idx+=1

    # print(leafs)
    while start_k != k :
        #find minimum
        min_idx = -1
        min_sum = 2000000000
        for end in leafs:
            if num[ r_link[end] ] + num[end] < min_sum :
                min_idx = end
                min_sum = num[ r_link[end] ] + num[end]
        # del and update 
        num[ r_link[min_idx] ] = min_sum
        if links[ r_link[min_idx] ][0] == -1 :
            links[ r_link[min_idx] ][1] = -1
            leafs.add(r_link[min_idx])
        elif  links[ r_link[min_idx] ][1] == -1:
            links[ r_link[min_idx] ][0] = -1
            leafs.add(r_link[min_idx])
        else :
            if links[ r_link[min_idx] ][0] == min_idx:
                links[ r_link[min_idx] ][0] = -1
            else :
                links[ r_link[min_idx] ][1] = -1 
        # print(min_idx)
        leafs.remove(min_idx)
        num[min_idx] = -1
        #collect
        start_k -= 1
    answer = max(num)
    return answer

k = 3

num = [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1]

links = [[-1, -1], [-1, -1], [-1, -1], [-1, -1],
        [8, 5], [2, 10], [3, 0], [6, 1], 
        [11, -1], [7, 4], [-1, -1], [-1, -1]]

print( solution(k, num, links) )