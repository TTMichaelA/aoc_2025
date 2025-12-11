import time
import queue

class Node:

    def __init__(self, edge_list, name):
        self.name = name
        self.edgelist = set()
        self.value = 0
        self.dist = 0
        for edge in edge_list:
            self.edgelist.add(edge)
    
    def setval(self, val):
        self.value = val
    
    def getval(self):
        return self.value

    def getname(self):
        return self.name

    def getedges(self):
        return self.edgelist

    def getdist(self):
        return self.dist
    
    def setdist(self, dist):
        self.dist = dist

def build_graph():
    graph = {}
    with open("day11_input.py") as puzzle_input:
        for line in puzzle_input:
            line_split = line.split(": ")
            nodename = line_split[0]
            edgelist = line_split[1].strip("\n").split(" ")
            node = Node(edgelist, nodename)
            graph[nodename] = node
    if "you" in graph.keys():
        graph["you"].setval(1)
    if "svr" in graph.keys():
        graph["svr"].setval(1)
    outnode = Node([], "out")
    graph["out"] = outnode
    return graph

def partone(graph):
    explored = set()
    bfs = queue.PriorityQueue()
    bfs.put("you")
    while not bfs.empty():
        nextup = bfs.get()
        next = graph[nextup]
        nname = next.getname()
        if nname in explored:
            continue
        explored.add(nname)
        nval = next.getval()
        for edge in next.getedges():
            currval = graph[edge].getval()
            if not currval:
                graph[edge].setval(nval)
            else:    
                graph[edge].setval(nval + currval)
            
            bfs.put(edge)

    return graph["out"].getval()

def parttwo_get_dist(graph, start, tgt):
    explored = set()
    max_dist = 0
    bfs = queue.Queue()
    bfs.put((0, start))
    graph[start].setval(1)
    while not bfs.empty():
        nextup = bfs.get()
        curr = graph[nextup[1]]
        cname = curr.getname()
        cdist = curr.getdist()
        if (cdist, cname) in explored:
            continue
        explored.add((cdist, cname))

        if cname == tgt:
            continue
        
        cval = curr.getval()

        # print(f"Node {cname} is {cdist} from {start} with {cval} paths")

        for edge in curr.getedges():
            eval = graph[edge].getval() + cval
            edist = max(graph[edge].getdist(), cdist+1)
            if edist > max_dist:
                max_dist = edist
            nnode = graph[edge]
            nnode.setval(eval)
            nnode.setdist(edist)
            
            bfs.put((edist,edge))
    
    return max_dist

def part_two_set_val(graph, max_dist, start, tgt, cnt):
    for k,v in graph.items():
        v.setval(0)
    graph[start].setval(cnt)    
    for i in range(max_dist+1):
        for k,v in graph.items():
            if v.getdist() == i:
                val = v.getval()
                # print(f"node {k} at dist {i} has {val} paths")
                for e in v.getedges():
                    if e == 'ohl':
                        pass
                    graph[e].setval(graph[e].getval() + val)
    return graph[tgt].getval()





if __name__ == "__main__":
    pi = build_graph()
    pi2 = build_graph()
    pi3 = build_graph()
    # print(pi)
    # print(pi["you"].getval())
    # cnt = partone(pi)
    max_dist = parttwo_get_dist(pi, "svr", "out")
    cnt1 = part_two_set_val(pi, 38, "svr", "fft", 1)
    print(cnt1)
    cnt2 = part_two_set_val(pi, 38, "fft", "dac", 1)
    print(cnt2)
    cnt3 = part_two_set_val(pi, 38, "dac", "out", 1)
    print(cnt3)
    # dac_cnt = parttwo(pi2, "fft", "dac")
    # out_cnt = parttwo(pi3, "dac", "out")
    # print(fft_cnt)
    # print(dac_cnt)
    # print(out_cnt)
    print(cnt1 * cnt2 * cnt3)