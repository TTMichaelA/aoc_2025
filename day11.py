import time
import queue

class Node:

    def __init__(self, edge_list, name):
        self.name = name
        self.edgelist = set()
        self.value = None
        self.svrvalue = None
        self.dac = None
        self.fft = None
        for edge in edge_list:
            self.edgelist.add(edge)
    
    def setval(self, val):
        self.value = val
    
    def getval(self):
        return self.value

    def setsvrval(self, val):
        self.value = val
    
    def getsvrval(self):
        return self.value

    def setdacval(self, val):
        self.value = val
    
    def getdacval(self):
        return self.value

    def setfftval(self, val):
        self.value = val
    
    def getfftval(self):
        return self.value

    def getedges(self):
        return self.edgelist

    def getname(self):
        return self.name

def build_graph():
    graph = {}
    with open("day11_input.py") as puzzle_input:
        for line in puzzle_input:
            line_split = line.split(": ")
            nodename = line_split[0]
            edgelist = line_split[1].strip("\n").split(" ")
            node = Node(edgelist, nodename)
            graph[nodename] = node
    graph["you"].setval(1)
    outnode = Node([], "out")
    graph["out"] = outnode
    return graph

def partone(graph):
    explored = set()
    bfs = queue.Queue()
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



if __name__ == "__main__":
    pi = build_graph()
    # print(pi)
    # print(pi["you"].getval())
    cnt = partone(pi)
    print(cnt)