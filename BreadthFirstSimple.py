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

"""
  Breadth first search
  
  Uses the flood fill mapping we've done previously but 
  now calculates the shorted path between the startNode and goalNode
  
  This implementation assumes each space has equal cost in movement
"""

startNode = (0,2)
goalNode = (4,1)

frontier = Queue.Queue()
frontier.put(startNode)
came_from = {}
came_from[startNode] = None #Python version of "null"



# Construct a map of all possible paths for the startNode across the map
while not frontier.empty():
  current = frontier.get() # Get instead of peek, dequeues the item
  
  # Early exit, we've found a valid path
  if current == goalNode:
    break
  
  for neighbour in graph.getNeighbours(current):
    if neighbour not in came_from:
      frontier.put(neighbour)
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
    else:
      resultingGrid += " . "
  resultingGrid +="\n"

print resultingGrid
