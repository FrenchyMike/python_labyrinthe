# Maze game in Python

## Context of development

*Comments in program are in french, sorry for english speaker :'(*

This program was designed through a tutorial from [Openclassroom](https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python])
This is my second program in Python, so I'm sure it could be improve a lot.
Thank for your interest. Hope you will enjoy it !

If you want to visit [my first project](https://gitlab.com/FrenchyMike/python_pendu).

The main difference with the first program is that the maze game 
uses object programmation.

## How the program is structured

This program is composed of:

* 3 python files:

  * classe.py: contains class, attributes and methods
  * fonction.py: contains others function for global rpogram running
  * main_maze.py: the main program, gathers class and fonction scripts

* 2 folders:

  * maps: contains maze maps into txt file __avoid to modify them___
  * savings: to register the games __screenshot of the current__

## Rules of the game

To run this program, please download sources and run maze_run.py. 
You are symbolized by the cross 'X' and you have to reach the exit, symbolized 
by 'U', 'O' represents walls and dot '.' are gates.

To move through the maze you have to input an number of steps and a direction.
Steps are integer and direction are cardinal points:

* n: north
* s: south
* e: east
* o: west (from _ouest_ in french)
