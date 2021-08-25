# Maze-Solver
This is a simple maze solver project based on A* algorithm, and there is also basic GUI implementation.<br>
#### Modules used
- Simpleai (simplesearch,astar)
- tkinter
## Explanation
A* algorithm is based on finding the best suited path by using heuristic approach.<br>
f(n)=g(n)+h(n)<br>
where,<br>
g(n): Actual cost from start.<br>
h(n): Estimation cost from n to goal node.<br>
### Mazesolver
1. By inheriting simplesearch class, we override some of it's member function.
    * Updating Actions with all possible moves
    * Updating Result with new state by provided action
    * Updating Is_goal with destination
    * Updating Heuristic with euclidean distance 
    * Updating cost with diagonal and edge movements
2. Then calling astar search for finding the best suited path
### GUI
With a little bit of OOP concept, The current board and solved board is displayed using tkinter.<br><br>
![image](image\maze_developed.png)
![image](image\mazesolved.png)

Feel free to provide your valuable inputs.
# Thank you