import numpy as np


class Maze:
    def __init__(self, size):
        try:
            self.width, self.height = size
        except Exception as e:
            raise Exception(
                "Expected a Tuple, got a non iterable object") from e
        else:
            self.cellsize = 25
            self.wallsize = 10
            self.cellcolor = 255
            self.wallcolor = 0
            self.currentcolor = 180

            self._makeCells()

    # Make an array with all of the cells
    def _makeCells(self):
        walls = {'N': True, 'E': True, 'S': True, 'W': True}

        self.cells = []

        for x in range(self.width):
            column = []
            for y in range(self.height):
                cell = {'x': x, 'y': y,
                        'visited': False,
                        'neighbours': [],
                        'walls': walls.copy()}

                # Get Neighbours
                if (y):
                    neighbour = column[y - 1]
                    cell['neighbours'].append(neighbour)
                    neighbour['neighbours'].append(cell)
                if (x):
                    neighbour = self.cells[x - 1][y]
                    cell['neighbours'].append(neighbour)
                    neighbour['neighbours'].append(cell)

                column.append(cell)
            self.cells.append(column)

        # for column in self.cells:
        #     for cell in column:
        #         cell['neighbours'].extend(
        #             self._getNeighbours(cell['x'], cell['y']))

    # Print cell positions for debugging
    def _printCells(self):
        cells = [["({},{})".format(cell['x'], cell['y'])
                  for cell in column] for column in self.cells]

        text = []
        for sentence in cells:
            text.append(' '.join(sentence))

        print('\n'.join(text))

    # Get Neighbours ***Deprecated***
    # def _getNeighbours(self, x, y):
    #     neighbours = []
    #
    #     # Check if they exists
    #     if (x > 0):                 # Left Neighbour
    #         neighbours.append(self.cells[x - 1][y])
    #     if (x < self.width - 1):    # Right Neighbour
    #         neighbours.append(self.cells[x + 1][y])
    #     if (y > 0):                 # Top Neighbour
    #         neighbours.append(self.cells[x][y - 1])
    #     if (y < self.height - 1):    # Bottom Neighbour
    #         neighbours.append(self.cells[x][y + 1])
    #
    #     return neighbours

    # Remove Walls between cells
    def removeWalls(self, cellA, cellB):    # , tb=None):
        xdiff = cellA['x'] - cellB['x']
        ydiff = cellA['y'] - cellB['y']

        Check if adjacent
        samecell = xdiff == ydiff == 0
        not_adjacent1 = abs(xdiff) > 1 or abs(ydiff) > 1
        not_adjacent2 = (xdiff != 0) and (ydiff != 0)

        if (not_adjacent1 or not_adjacent2):
            # Traceback for debbugging purposes
            # if (tb is not None):
            #     string = [str(x) for x in tb[0]]
            #     neighbours = '\n'.join(string)
            #
            #     string = [str(x) for x in tb[1]]
            #     not_visited = '\n'.join(string)
            #
            #     print("Neighbours:\n{}\n\nNot Visited:\n{}".format(
            #         neighbours, not_visited))

            print("\n\nCellA: {}\nCellB: {}\n".format(cellA, cellB))
            raise Exception("Cells not adjacent, can't remove walls")

        elif (samecell):
            raise Exception("Same cell, can't remove walls")

        if (ydiff == 0):
            if (xdiff == 1):
                cellA['walls']['E'] = False
                cellB['walls']['W'] = False
            elif (xdiff == -1):
                cellA['walls']['W'] = False
                cellB['walls']['E'] = False

        elif (xdiff == 0):
            if (ydiff == 1):
                cellA['walls']['N'] = False
                cellB['walls']['S'] = False
            elif (ydiff == -1):
                cellA['walls']['S'] = False
                cellB['walls']['N'] = False

    # Make an image of the Maze
    def draw(self, current=None):
        scale = self.cellsize + self.wallsize

        imgWidth = self.width * scale + self.wallsize
        imgHeight = self.height * scale + self.wallsize

        # ### Numpy Array images are in the (y,x) format
        image = np.empty((imgHeight, imgWidth), dtype=np.uint8)
        image.fill(self.wallcolor)

        for column in self.cells:
            for cell in column:
                imgX = cell['x'] * scale + self.wallsize
                imgY = cell['y'] * scale + self.wallsize

                # Draw cell in image
                if (cell['visited']):
                    image[imgY:imgY + self.cellsize,
                          imgX:imgX + self.cellsize].fill(self.cellcolor)
                else:
                    image[imgY:imgY + self.cellsize,
                          imgX:imgX + self.cellsize].fill(self.cellcolor // 4)

                # Draw walls/corridors in image
                if (not cell['walls']['N']):
                    wallX = imgX
                    wallY = imgY - self.wallsize

                    image[wallY:imgY,
                          wallX:wallX + self.cellsize].fill(self.cellcolor)

                if (not cell['walls']['E']):
                    wallX = imgX - self.wallsize
                    wallY = imgY

                    image[wallY:wallY + self.cellsize,
                          wallX:imgX].fill(self.cellcolor)

        if (current is not None):
            imgX = current['x'] * scale + self.wallsize
            imgY = current['y'] * scale + self.wallsize

            image[imgY:imgY + self.cellsize,
                  imgX:imgX + self.cellsize].fill(self.currentcolor)

        # print(self.cells[-1][-1])

        return image
