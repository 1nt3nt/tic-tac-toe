# tic-tac-toe
It is an offline tic tac toe game wtih pygame.
So far, it only supports some basic playgames, such as play, quit.
In the future, I am going to add setting function, which will support resolution, music volumn and piece shapes.

## To compile this program, there are several enviroment needs to be done
### 1. update your python version to/above 3.10
a. 
    `
        Because in this program, there is a feature only supported by python 3.10+, such as match-case
    `
    <br />
b.
    For Mac:
    `
        brew upgrade python3
    `
    <br />
c.
    For Windows:
    `
        Go to python website install the latest version, then uninstall old version
    ` [Download Python](https://www.python.org/)
### 2. Install pygame library
a. For Mac: `python3 -m pip install -U pygame --user` <br />
b. To test if it works: `python3 -m pygame.examples.aliens`<br />
c. For Windows `py -m pip install -U pygame --user` <br />
d. To test if it works: `py -m pygame.examples.aliens`<br />
e. For more information, please see [Pygame](https://www.pygame.org/wiki/GettingStarted)
