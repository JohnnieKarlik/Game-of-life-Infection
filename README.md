# Game-of-life-Infection
python implemantation of Conway’s Game of Life - https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

### standard rules:
  1. Any live cell with fewer than two live neighbors dies (under population).
  2. Any live cell with two or three live neighbors lives on to the next generation.
  3. Any live cell with more than three live neighbors dies (overpopulation).
  4. Any dead cell with exactly three live neighbors becomes a live cell (reproduction).

### infection rules:
  1. Any dead cell with a single live neighbor lives on to the next generation.
  2. Any live cell with no horizontal or vertical live neighbors dies.

## Instructions:
1. clone reposetory

run:

python game_of_life.py --width=<board width> --height=<board height> --infect_after=<infect after> --max_generations=<max generations> --seed=<seed>

for example:

python game_of_life.py --width=3 --height=3 --infect_after=3 --max_generations=6 --seed="0 0 0 1 1 1 0 0 0"

0 0 0 1 1 1 0 0 0

0 1 0 0 1 0 0 1 0

0 0 0 1 1 1 0 0 0

0 1 0 0 1 0 0 1 0

0 1 0 0 1 0 0 1 0

0 1 0 0 1 0 0 1 0

0 1 0 0 1 0 0 1 0

## Tests:
run: 

python tests.py
