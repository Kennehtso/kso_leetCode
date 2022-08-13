from collections import deque
r_dfs_iter = []
r_dfs_recur = []
r_bfs = []
def dfs_iter(graph,chk, src)-> None:
    stk = [src]
    while stk:
        cur = stk.pop()
        if cur in chk: continue
        else:
            chk.add(cur)
            r_dfs_iter.append(cur)
            for neighbour in graph[cur]:
                stk.append(neighbour)

def dfs_recur(graph, chk, src)-> None:
    if src in chk: return
    chk.add(src)  
    r_dfs_recur.append(src)
    for neighbour in graph[src]:
        dfs_recur(graph, chk, neighbour)

def bfs(graph, chk, src)-> None:
    dq = deque([src])
    while dq:
        cur = dq.popleft()
        if cur in chk: continue
        else:
            chk.add(cur)
            r_bfs.append(cur)
            for neighbour in graph[cur]:
                dq.append(neighbour)

def hasPath_dfs_recur(graph, chk, src, target):
    if src == target: return True
    if src in chk: return
    chk.add(src)  

    for neighbour in graph[src]:
        if hasPath_dfs_recur(graph, chk, neighbour, target):
            return True
    return False


def hasPath_bfs(graph, chk, src, target):
    dq = deque([src])
    while dq:
        cur = dq.popleft()
        if cur in chk: continue
        else:
            chk.add(cur)
            if cur == target: return True
            else:
                for neighbour in graph[cur]:
                    dq += [neighbour]
    return False

def edges_to_adjacency(edges):
    adjacency_list = {}
    for cur in edges:
        a, b = cur[0], cur[1]
        if a not in adjacency_list: adjacency_list[a] = [b]
        else: adjacency_list[a].append(b)
        if b not in adjacency_list: adjacency_list[b] = [a]
        else: adjacency_list[b].append(a)
    return adjacency_list

def matrix_get_neighbours(matrix, target):
    target_row, target_col = target
    len_row, len_col = len(matrix), len(matrix[0])
    row_4_dir, col_4_dir =  [-1, 0, 1, 0],  [0, 1, 0, -1]
    neighbours = []
    for idx in range(len(row_4_dir)):
        cur_row = target_row + row_4_dir[idx]
        cur_col = target_col + col_4_dir[idx]
        if 0 <= cur_row < len_row and 0 <= cur_col < len_col:
            neighbours.append((cur_row, cur_col))
    return neighbours

def view_neighbours(neighbours, matrix, target):
    row, col = target
    print("matrix(%s[%s])'s neighbours are:"%(matrix[row][col], target))
    r1, r2 = "", ""
    for n in neighbours:
        r , c = n
        v = matrix[r][c]
        r1 += str(n) + ","
        r2 += str(v) + ","
    print("[%s]"%(r1))
    print("[%s]"%(r2))
    
graph = {
    'a':['b','c'],
    'b':['d','a'],
    'c':['e'],
    'd':['f'],
    'e':[],
    'f':[],
    'h':[],
}

edges = [
    ['i','j'],
    ['k','i'],
    ['m','k'],
    ['k','l'],
    ['o','n'],
]

matrix = [
    [1, 3, 5],
    [2, 4, 6],
    [7, 8, 9]
]

print('dfs_iter: ') 
dfs_iter(graph, set(), 'a')
print(r_dfs_iter)  #a,c,e,b,d,f

print('dfs_recur: ') 
dfs_recur(graph, set(), 'a') 
print(r_dfs_recur) #a,b,d,f,c,e

print('bfs: ')
bfs(graph, set(), 'a') 
print(r_bfs) #a,b,c,d,e,f

start = 'a'
end = 'f'
# True
print("hasPath_dfs_recur: from %s to %s: %s"%(start, end, hasPath_dfs_recur(graph, set(), start, end)))

# True
print("hasPath_bfs: from %s to %s: %s"%(start, end, hasPath_bfs(graph, set(), start, end)))

print(edges)
print(edges_to_adjacency(edges))

print('get neighbours for matrix 2x array to adjacency list')
print(matrix)
target = (0,2)
view_neighbours(matrix_get_neighbours(matrix, target), matrix, target)