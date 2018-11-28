# from profilestats import profile
import random
import cv2


# @profile(print_stats=12, dump_stats=True)
def recursive_backtracker(maze, colormap=cv2.COLORMAP_HOT, speed=33):
    numcells = maze.width * maze.height
    visited = 0

    # Step 1 Get Current
    current = maze.cells[0][0]
    current['visited'] = True
    visited += 1

    stack = []

    if speed is not None:
        img = maze.draw(current=current)

        if colormap is not None:
            img = cv2.applyColorMap(img, colormap)

        cv2.imshow('maze', img)
        cv2.waitKey(speed)

    # Step 2 Loop
    while(visited < numcells):
        # Step 2.1 Get Neighbours that haven't been visited
        not_visited = []
        for cell in current['neighbours']:
            if not cell['visited']:
                not_visited.append(cell)

        if (not_visited):
            # Step 2.1.1 Get a random neighbour
            if (len(not_visited) > 1):
                other = random.choice(not_visited)
            else:
                other = not_visited[0]

            # Step 2.1.2 Push current to stack
            stack.append(current)

            # Step 2.1.3 Remove Walls
            maze.removeWalls(current, other)

            # Step 2.1.4 New current
            current = None
            current = other
            current['visited'] = True

            visited += 1
        # Step 2.2 Get from Stack
        elif(stack):
            # Step 2.2.1 and 2.2.2 Get current from Stack
            current = stack.pop()
        else:
            print("Stack got to 0")
            break

        if speed is not None:
            img = maze.draw(current=current)

            if colormap is not None:
                img = cv2.applyColorMap(img, colormap)

            cv2.imshow('maze', img)
            cv2.waitKey(speed)
