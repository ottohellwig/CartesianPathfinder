# Coordinate-Distance-Calculator #
Coordinate Distance Calculator is an interactive notebook which calculates the distance and optimal path from a set of Cartesian coordinates. The Python functions enable users to find the closest point from the starting coordinate, calculate the distance between multiple coordinates, and determine the best path. 

* Simple and **modular Python code** which can be repurposed
* Can calculate distance between **multiple Cartesian coordinates**
* Determines the **best path** based on the shortest overrall distance required
* Can **graphically represent** optimised path



## Guide ##

To use the Coordinate Distance Calculator, input your desired values into the **distance**, **find_closest**, **path_distance** and or **best_path** function. 

#### Distance ####
``` 
# Insert desired coordinates, P1/P2 being 1 set and P3/P4 being another set of coordinates.

distance((P1, P2), (P3, P4))
```

#### Find Closest ####
```
# The first coordinate is considered the starting point, the function will find the closest coordinate to that point.

find_closest((StartingP1, StartingP2), [(P1, P2), (P3, P4), (P5, P6), (P7, P8)])
```

#### Path Distance ####
```
# Insert desired coordinates into P1/P2, etc.

path_distance([(P1, P2), (P3, P4), (P5, P6)])
```
#### Best Path ####
```
# Insert desired coordinates into P1/P2, etc.

points = [(P1, P2), (P3, P4), (P5, P6), (P7, P8), (P9, P10)]

path = best_path(points)
print(path)
```
#### Graphical Representation ####
```
# This will graphically represent the best path, you can replace "path" with another function to see that function.

matplotlib.pyplot.plot(*zip(*path))
```

If values are null the function will not produce a result. Do not alter the function which is being called, as the calculations may not function as intended. The explanation behind each function is featured in the notebook.

## Planned Features ##

* Move from a Jupyter-based interactive notebook to a designed user interface
* Integrate Dijkstra's algorithm and A*  Search algorithm for the best path function
* Build a front-end platform for user input 
