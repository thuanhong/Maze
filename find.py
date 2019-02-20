class node():
    def __init__(self, parent, position):
        self.parent = parent
        self.pos = position

def distance(cur, goal):
    return math.sqrt((goal[0] - cur[0])**2 - (goal[1] - cur[1])**2)

def find_path(maze, star, end):
    # declare start point vs end point
    start_node = node(None, start)
    end_node = node(None, end)

    # create two list emppty
    open_list = []
    closed_list = []

    open_list.append(start_node)
    # handle main
    while True:
        current_pos = open_list[0]
