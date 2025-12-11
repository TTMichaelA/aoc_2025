import time
import queue

class Node:

    def __init__(self, edge_list, name):
        self.name = name
        self.edgelist = set()
        self.value = None
        self.dac = None
        self.fft = None
        self.both = None
        for edge in edge_list:
            self.edgelist.add(edge)
    
    def setval(self, val):
        self.value = val
    
    def getval(self):
        return self.value
    
    def getdac(self):
        return self.dac
    
    def setdac(self, dac):
        self.dac = dac

    def getfft(self):
        return self.fft
    
    def setfft(self, fft):
        self.fft = fft

    def getboth(self):
        return self.both
    
    def setboth(self, both):
        self.both = both

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
    if "you" in graph.keys():
        graph["you"].setval(1)
    if "svr" in graph.keys():
        graph["svr"].setval(1)
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

def parttwo(graph):
    explored = set()
    bfs = queue.Queue()
    bfs.put("svr")
    while not bfs.empty():
        nextup = bfs.get()
        next = graph[nextup]
        nname = next.getname()
        if nname in explored:
            continue
        explored.add(nname)
        nval = next.getval()
        
        if nname == "fft":
            next.setfft(nval)
        if nname == "dac":
            next.setdac(nval)
        ndac = next.getdac()
        nfft = next.getfft()
        nboth = next.getboth()
        
        if ndac and nfft:
            adj = min(ndac, nfft)
            if nboth:
                nboth += adj
            else:
                nboth = adj
            ndac -= adj
            nfft -= adj

        for edge in next.getedges():
            currval = graph[edge].getval()
            if not currval:
                graph[edge].setval(nval)
            else:    
                graph[edge].setval(nval + currval)
            currdac = graph[edge].getdac()
            if not currdac and ndac:
                graph[edge].setdac(ndac)
            elif currdac and ndac:
                graph[edge].setdac(currdac + ndac)
            
            currfft = graph[edge].getfft()
            if not currfft and nfft:
                graph[edge].setfft(nfft)
            elif currfft and nfft:
                graph[edge].setfft(currfft + nfft)

            currboth = graph[edge].getboth()
            if not currboth and nboth:
                graph[edge].setboth(nboth)
            elif currboth and nboth:
                graph[edge].setboth(currboth + nboth)
                


            bfs.put(edge)

    return graph["out"].getboth()

if __name__ == "__main__":
    pi = build_graph()
    # print(pi)
    # print(pi["you"].getval())
    # cnt = partone(pi)
    cnt = parttwo(pi)
    print(cnt)