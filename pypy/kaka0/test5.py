import queue

def solution(info, edges):
    answer = 0
    new_link = [[] for _ in range(20)]
    node_now = [[0,1]]

    can_go = set()
    for x in edges:
        new_link[x[0]].append(x[1])
    print(new_link)
    
    for x in node_now:
        for x in new_link[x[0]]:
            if x[1] + 

    return answer

if __name__ == "__main__":
    info = [0,0,1,1,1,0,1,0,1,0,1,1]
    edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]

    print(solution(info, edges))