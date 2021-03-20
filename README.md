# AStar Pathfinder Visualizer
A* Pathfinding visualizer - 1/5/2021
## [What is the A* Search Algorithm?](https://en.wikipedia.org/wiki/A*_search_algorithm)
> *A\* Pathfinder is an informed search algorithm, or a best-first search, meaning that is is forumlated in terms of weighted graphs: starting from a specific starting node of a graph, it aims to find a path to the given goal node having the smallest cost (least distance travelled, shortest time, etc.). It does this by maintaining a tree of paths originating at the start node and extending those paths one edge at a time until its termination criterion is satisfied.*
## How to use
-> Run `main.py` (make sure you have [pygame](https://www.pygame.org/wiki/about) installed) 

-> Click on two points to define start and end points

-> Click and drag to draw out obstacles

-> Space to watch the algorithm find the shortest path!

-> Hit "v" before running the program to watch the algorithm in action!

-> Hit "c" to clear the grid


Demo:

https://user-images.githubusercontent.com/75106472/111888550-c5b6ea00-899a-11eb-9c91-bf70bb4e85c2.mp4



(Might add more features like timer and find shortest path between multiple sets of points...)

*Fixed a bug where when drawing obstacles, if you tried drawing an obstacle of the edge of the screen, it would error out*
