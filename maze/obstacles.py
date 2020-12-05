# -------------------------------------------------------------------------------------------------
#
# TODO: Please replace this placeholder code with your solution for Toy Robot 4, and work from there.
#
# -------------------------------------------------------------------------------------------------

import random


def create_random_obstacles():
    """
    Creates obstacles at random places within the maze, basically generate a maze
    """
    pass


def get_obstacles():
    list_of_obstacles = {}
    index = 0
    for x in range(-102*2, 100*2, 4*2):
        for y in range(-206*2, 200*2, 4*2):
            horizontal = [x+4*2, y]
            vertical = [x, y+4*2]
            
            index = index + 1
            list_of_obstacles[index] = horizontal
            list_of_obstacles[index] = vertical
    print(list_of_obstacles)

    return list_of_obstacles



list_of_obstacles = get_obstacles()

def is_position_blocked(input_x, input_y):
    """
    checks if the robot can go to that position
    """
    
    global list_of_obstacles 

    for i in list_of_obstacles: 
        for destination_x in range(i[0], i[0]+(4*2)):
            for destination_y in range(i[1], i[1]+(4*2)):
                if (input_x, input_y) == (destination_x, destination_y):
                    return True
    return False


def is_path_blocked(x1,y1, x2, y2):
    """
    checks if the robot can pass through that position
    """
    
    if y1 == y2:
        if x1 < x2:
            for i in range(x1, x2):
                if is_position_blocked(i, y2) == True:
                    return True
        else:
            for i in range(x1, x2, -1):
                if is_position_blocked(i,y2) == True:
                    return True
    if x1 == x2:
        if y1 < y2:
            for i in range(y1, y2):
                if is_position_blocked(x2, i) == True:
                    return True
        else:
            for i in range(y1, y2, -1):
                if is_position_blocked(x2, i) == True:
                    return True
    return False


def print_obstacles():
    """
    prints the position of where the obstacles are placed.
    """
    
    # global list_of_obstacles
    
    # if len(list_of_obstacles) > 0:
    #     print('There are some obstacles:')
    #     for (a,b) in list_of_obstacles:
    #         print(f"- At position {a},{b} (to {a + 4},{b + 4}")
    pass
