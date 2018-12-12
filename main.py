import generator_algorithms
import solving_algorithms
import time
import maze
import cv2
import sys


def main():
    colormap = None     # cv2.COLORMAP_HOT

    m = maze.Maze((40, 20))
    # m.cellsize = 1
    # m.wallsize = 1

    generator_algorithms.recursive_backtracker(
        m, colormap=colormap, speed=None)

    return m.draw()
    # if colormap is not None:
    #     img = cv2.applyColorMap(img, colormap)


if __name__ == '__main__':
    t0 = time.perf_counter()
    img = main()
    print("Took: {}".format(time.perf_counter() - t0))

    cv2.imshow('maze', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
