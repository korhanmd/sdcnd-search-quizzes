# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------

    visit_list = []
    visit_path = []
    path_list = []
    g = 0
    current_state = init
    visit_list.append(current_state)
    flag = False

    while flag == False:
        g += 1

        for i in range(4):
            neighbour_grid = [x + y for x, y in zip(current_state, delta[i])]
            neighbour_x = neighbour_grid[0]
            neighbour_y = neighbour_grid[1]
            if neighbour_x >= 0 \
            and neighbour_y >= 0 \
            and neighbour_x <= len(grid)-1 \
            and neighbour_y <= len(grid[0])-1 \
            and neighbour_grid not in visit_list \
            and grid[neighbour_x][neighbour_y] == 0:
                visit_list.append(neighbour_grid)
                path_list.append([g, neighbour_x, neighbour_y])
                if neighbour_x == len(grid)-1 and neighbour_y == len(grid[0])-1:
                    path = [g, neighbour_x, neighbour_y]
                    flag = True

        path_list.sort()

        if len(path_list) == 0:
            return 'fail'

        current_state = [path_list[0][1], path_list[0][2]]
        g = path_list[0][0]

        del path_list[0]

    return path

print search(grid, init, goal, cost)