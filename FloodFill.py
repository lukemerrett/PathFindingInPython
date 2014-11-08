from Graph import *
import Queue

"""
  Construct the graph with a series of obstacles
  that can still be navigated around
  
  Source: http://www.redblobgames.com/pathfinding/a-star/introduction.html
"""
obstacles = [(0,1), (2,4), (2,5), (2,6), (2,7)]

graph = Graph(20, 10, obstacles)

"""
  Flood fill
  
  Navigates every node in the graph using it's neighbours
  until it has mapped the whole graph excluding any obstacles
"""

startNode = (0,2)

frontier = Queue.Queue()
frontier.put(startNode)
visited = {}
visited[startNode] = True

neighbours = graph.getNeighbours(startNode)

while not frontier.empty():
  current = frontier.get() # Get instead of peek, dequeues the item
  for neighbour in graph.getNeighbours(current):
    if neighbour not in visited:
      frontier.put(neighbour)
      visited[neighbour] = True