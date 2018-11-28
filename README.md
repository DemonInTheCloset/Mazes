# Mazes

A python implementation of different maze generating and maze solving algorithms. Inspired by @CodingTrain and @shiffman.

 - [Maze Object](#Maze-Object)
   - [Variables](#Variables)
   - [Functions](#Functions)
 - [Generator Algorithms](#Generator-Algorithms)
   - [Recursive Backtracker](#Recursive-Backtracker)
 - [Solving Algorithms [WIP]](#Solving-Algorithms-[WIP])

## Maze Object

 - [Variables](#Variables)
    - [Cells Array](#Cells-Array)
    - [Image Format](#Image-Format)
      - [Size](#Size)
      - [Color](#Color)
 - [Functions](#Functions)
   - [removeWalls(cellA, cellB)](#removeWalls(cellA,-cellB))
   - [draw(current=None)](#draw(current=None))
   - [_printCells()](#_printCells())
   - [_makeCells()](#_makeCells())

A maze object is declared as:
```
import maze

m = maze.Maze((width, height))
```
* * *

### Variables

The Maze object contains the following variables:
 - cells
 - width
 - height
 - cellsize
 - wallsize
 - cellcolor
 - wallcolor
 - currentcolor

#### Cells Array

The `cells` array can be accessed and contains `width` lists with `height` cell elements.
The cells are arranged in the array in the `[x][y]` format

#### Image Format

##### Size

`cellsize`      : Defines the size of each cell in pixels, the default is 25
`wallsize`      : Defines the width of each wall in pixels, the default is 10

##### Color

`cellcolor`     : Defines the color of each cell in grayscale, the default is 255
`wallcolor`     : Defines the color of each wall in grayscale, the default is 0
`currentcolor`  : Defines the color of the highlighted current cell in grayscale, the default is 180

* * *

### Functions

The Maze object contains the following functions:
 - removeWalls(cellA, cellB)
 - draw(current=None)
 - _printCells()
 - _makeCells()
 
#### removeWalls(cellA, cellB)
 
Takes as an input two cells and removes the walls between them. Raises an exception if the cells are the same or if they aren't adjecent to eachother.
 
#### draw(current=None)
 
Returns a black and white image of the maze (numpy array of uint8), it optionally highlights the current cell.
 
#### _printCells()
 
Prints cell position data for debugging purposses, shouldn't be used.

#### _makeCells()
 
Initializes the cells array inside the Maze, should only be used by the Maze object itself upon initialization, very costly function.

## Generator Algorithms

 - [Recursive Backtracker](#Recursive-Backtracker)

* * *

### Recursive Backtracker

Usage:
`recursive_bactracker(maze, colormap=cv2.COLORMAP_HOT, speed=33)`

By default it takes a `colormap` to highlight the unvisited cells and the `current` cell, if set to `None` it will be rendered in grayscale.
By default it sets the animation `speed` to 30 FPS (waits 33 ms between frames).
 - if `speed` is set to 0, the code will wait for a keypress between each frame.
 - if `speed` is set to `None`, the frames won't render.

## Solving Algorithms [WIP]
