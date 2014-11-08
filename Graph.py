"""
  Data structure for a node:
    __all_nodes[0][0] = X coord
    __all_nodes[0][1] = Y coord
"""

"""
  Constructs a graph of nodes and edges 
  including obstacles that cannot be moved through.
  
  Source: http://www.redblobgames.com/pathfinding/grids/graphs.html
"""
class Graph:
  __all_nodes = []
  __movement_costs = {}
  
  """
    Graph with obstacles; movement only permitted around them.
    obstacles is an array of x,y coords, eg: [(0, 1), (0, 3)]
    obstacles is nullable, if you don't provide it no obstacles are placed
  """
  def __init__(self, xSize, ySize, obstacles = []):
    self.__constructGrid(xSize, ySize)
    for obstacle in obstacles:
      self.__all_nodes.remove(obstacle)
    
  """
    Constructs a grid of nodes using the provided x and y size.
  """
  def __constructGrid(self, xSize, ySize):
    for x in range(xSize):
      for y in range(ySize):
	self.__all_nodes.append((x, y))
	self.__movement_costs[(x, y)] = 1 # Default all costs to 1
  
  """
    Finds out all the edges for each node based on whether they can be moved into
  """
  def getNeighbours(self, node):
    # I can move up, down, left or right, but not diagonally
    directions = [(1 ,0), (0, 1), (-1, 0), (0, -1)]
    neighbours = []
    for direction in directions:
      neighbour = (node[0] + direction[0], node[1] + direction[1])
      if neighbour in self.__all_nodes:
	neighbours.append(neighbour)
    return neighbours
  
  """
    Gets the current cost of the node, the higher the cost the less efficient 
    it is to move through that node 
  """
  def getCost(self, node):
    return self.__movement_costs[node]
  
  """
    Sets the current cost of the node, the higher the cost the less efficient 
    it is to move through that node
  """
  def setCost(self, node, newCost):
    self.__movement_costs[node] = newCost
  
  """
    Defines how close 2 nodes are together
  """
  def heuristic(self, a, b):
    # Manhattan distance on a square grid
    return abs(a[0] - b[0]) + abs(a[1] - b[1])



