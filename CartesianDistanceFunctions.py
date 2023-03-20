import math

# This function takes two points p1 and p2 and computes the distance between those two points.
# Each point is represented by a tuple containing the x and y coordinate of the point.
# For example (1,2) represents the point with an x coordinate of 1 and a y coordinate of 2.
# You can now call the distance function to determine the distance between 2 coordinates.


def distance(p1, p2):
    distance = math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))
    return distance

# This function takes a start point and a list of remaining points, and returns the remaining point
# that is closest to the start point the list of remaining points must contain at least one point.

def find_closest(start_point, remaining_points):
    current_shortest_path = float("inf")
    current_shortest_index = None
    for i in range (len(remaining_points)):
        distance_of_this_point = math.dist(start_point, remaining_points[i])
        if (distance_of_this_point < current_shortest_path):
            current_shortest_path = distance_of_this_point
            current_shortest_index = i
            
    return remaining_points[current_shortest_index]

# This function takes a list of points and returns the total distance of the path that results from
# traversing the points as ordered in the list the path must contain at least one point.

def path_distance(path) :
    total_distance = 0
    
    for i in range(len(path)-1):
        total_distance += distance(path[i], path[i+1])
        
    return total_distance

# The best_path function takes points and creates a new list, it then iterates through the closest points until terminating.

def best_path(points) :
    
    path = []
    starting_point = points[0]
    path.append(starting_point)
    
    points.remove(starting_point)
    remaining_points = points
    
    while (len(remaining_points) > 0):
        next_closest_point = find_closest(starting_point, remaining_points)
        remaining_points.remove(next_closest_point)
        path.append(next_closest_point)
        starting_point = next_closest_point
        
    return path
