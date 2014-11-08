Path Finding In Python
======================

Path Finding Algorithms in Python

Those implemented in this repository are:

* Breadth First Search (both with and without cost)
* A*

File breakdown

* Graph.py
  * Class for constructing and querying the nodes in the graph
* FloodFill.py
  * The basic algorithm for navigating each node and it's neighbours
* BreadthFirstSimple.py
  * A breadth first implementation
  * Does not take into account the cost of navigating across each node
  * Assumes the cost of each node is equal
* BreadthFirstWithCost.py
  * A breadth first implementation
  * Allows us to assign a cost to each indiviual node
  * Higher cost means it is less efficient to navigate over that node
  * The algorithm then uses the cost to find the most efficient path
* AStarWithCost
  * Similar to breadth first
  * However also takes into account the distance between the start and goal nodes in each iteration
  * More performant means of calculating the path

Written using the below guides from Red Blob Games:

* [Grids and Graphs](http://www.redblobgames.com/pathfinding/grids/graphs.html)
* [Introduction to A*](http://www.redblobgames.com/pathfinding/a-star/introduction.html)
