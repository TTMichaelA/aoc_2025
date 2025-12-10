import time
import queue

def build_input():
    union_find = []
    coords = {}
    with open("day8_input.txt") as puzzle_input:
        i = 0
        for line in puzzle_input:
            xyz = [int(x) for x in line.strip("\n").split(",")]
            coords[i] = xyz
            union_find.append(i)
            i += 1
    return coords, union_find

def euclid(c1, c2):
    x = c1[0] - c2[0]
    y = c1[1] - c2[1]
    z = c1[2] - c2[2]
    return (x ** 2 + y ** 2 + z ** 2) ** 0.5

def resolve_uf(distance_queue, cnt, union_find):
    for _ in range(cnt):
        shortest = distance_queue.get()
        # print(shortest)
        n1, n2 = shortest[1:]
        if union_find[n1] == union_find[n2]:
            continue
        else:
            curr = union_find[n1]
            join = union_find[n2]
            union_find = [curr if x == join else x for x in union_find]
            # print(get_counts(union_fiççnd))     
    return union_find

def get_counts(union_find):
    circuit_size = {}
    for x in union_find:
        if x not in circuit_size.keys():
            circuit_size[x] = 1
        else:
            circuit_size[x] += 1
    
    c_rank = sorted([-size for size in circuit_size.values()])
    if len(c_rank) == 2:
        return [-x for x in c_rank]
    return [-x for x in c_rank]

def partone(coords, cnt, union_find):
    pq = queue.PriorityQueue()
    for i in range(len(coords)):
        for k in range(i+1, len(coords)):
            dist = euclid(coords[i], coords[k])
            # print(dist, i, k)
            pq.put((dist, i, k))

    uf = resolve_uf(pq, cnt, union_find)

    circuit_size = {}
    for x in uf:
        if x not in circuit_size.keys():
            circuit_size[x] = 1
        else:
            circuit_size[x] += 1
    
    c_rank = get_counts(uf)

    # print(c_rank)
    return c_rank[0] * c_rank[1] * c_rank[2]
    
def resolve_uf2(distance_queue, union_find):
    while len(get_counts(union_find)) > 2:
        shortest = distance_queue.get()
        # print(shortest)
        n1, n2 = shortest[1:]
        if union_find[n1] == union_find[n2]:
            continue
        else:
            curr = union_find[n1]
            join = union_find[n2]
            union_find = [curr if x == join else x for x in union_find]
    
    while True:
        shortest = distance_queue.get()
        # print(shortest)
        n1, n2 = shortest[1:]
        if union_find[n1] == union_find[n2]:
            continue
        else:
            return n1, n2

def parttwo(coords, cnt, union_find):
    pq = queue.PriorityQueue()
    for i in range(len(coords)):
        for k in range(i+1, len(coords)):
            dist = euclid(coords[i], coords[k])
            # print(dist, i, k)
            pq.put((dist, i, k))

    n1, n2 = resolve_uf2(pq, union_find)

    # print(c_rank)
    return coords[n1][0] * coords[n2][0]

if __name__ == "__main__":
    start_time = time.perf_counter()
    
    co, uf = build_input()

    # print(co)
    # print(uf)
    cnt1 = partone(co, 1000, uf)

    x = parttwo(co, 40, uf)

    end_time = time.perf_counter()
    elapsed = end_time - start_time
    
    print(f"Part one answer is: {cnt1}")
    print(f"Part one answer is: {x}")
    print(f"Calculation time: {elapsed:.6f} seconds")
