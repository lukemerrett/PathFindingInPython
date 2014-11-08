from Graph import *
import Queue

"""
  Construct the graph with a series of obstacles that can still be navigated around
  
  Source: http://www.redblobgames.com/pathfinding/a-star/introduction.html
"""

xSize = 5
ySize = 10

obstacles = [(0,1), (2,4), (2,5), 
	     (2,6), (4,2), (4,3),
	     (2,0), (2,1), (2,2), 
	     (2,3)]

graph = Graph(xSize, ySize, obstacles)

higherCostingNodes = [(3,5), (3,6)]

for node in higherCostingNodes:
  graph.setCost(node, 5)

"""
  Breadth first search with Dijkstra's Algorithm
  
  Uses the flood fill mapping we've done previously but 
  now calculates the shorted path between the startNode and goalNode
  
  This implementation allows us to assign cost to each node
  so you can define which areas are more or less efficient to walk through
  
  Dijkstra's algorithm is then used to work out the optimal path through the nodes
"""

startNode = (0,2)
goalNode = (4,1)

frontier = Queue.PriorityQueue()
frontier.put(startNode, 0)
came_from = {}
cost_so_far = {}
came_from[startNode] = None #Python version of "null"
cost_so_far[startNode] = 0



# Construct a map of all possible paths for the startNode across the map
while not frontier.empty():
  current = frontier.get() # Get instead of peek, dequeues the item
  
  for neighbour in graph.getNeighbours(current):
    new_cost = cost_so_far[current] + graph.getCost(neighbour)
    if neighbour not in cost_so_far or new_cost < cost_so_far[neighbour]:
      cost_so_far[neighbour] = new_cost
      priority = new_cost
      frontier.put(neighbour, priority)
      came_from[neighbour] = current



# Create the path between the startNode and goalNode
currentNode = goalNode
path = [currentNode]
while currentNode != startNode:
  currentNode = came_from[currentNode]
  path.append(currentNode)


# Output the resulting path graphically to the command line
resultingGrid = "\n"

for x in range(xSize):
  for y in range(ySize):
    if (x,y) in obstacles:
      resultingGrid += " # "
    elif (x,y) == startNode:
      resultingGrid += " S "
    elif (x,y) == goalNode:
      resultingGrid += " G "
    elif (x,y) in path:
      resultingGrid += "---"
    elif (x,y) in higherCostingNodes:
      resultingGrid += "..."
    else:
      resultingGrid += " . "
  resultingGrid +="\n"

print resultingGrid
