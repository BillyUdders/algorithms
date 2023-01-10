import sys

import numpy as np
import pygame as pg

DEAD = 0
ALIVE = 200


def get_neighbors(i, j, old_state):
    # Get the nearest neighbors for current i, j from the old_state
    for outer_range in range(-1, 2):
        for inner_range in range(-1, 2):
            idx_1 = i + outer_range
            idx_2 = j + inner_range
            if (idx_1, idx_2) == (i, j):
                continue
            if 0 <= idx_1 < len(old_state) and 0 <= idx_2 < len(old_state[i]):
                yield old_state[idx_1][idx_2]


def update(old_state: np.array):
    # Clean state to update
    new_state = np.empty_like(old_state)

    # For every cell
    for i in range(len(old_state)):
        for j in range(len(old_state[i])):
            # Get neighbors then count how many are alive
            alive_count = list(get_neighbors(i, j, old_state)).count(ALIVE)
            # Apply the lifecycle rules for Conway's Game of Life
            current = old_state[i][j]
            if current == ALIVE:
                if alive_count == 2 or alive_count == 3:
                    current = ALIVE
                else:
                    current = DEAD
            else:
                if alive_count == 3:
                    current = ALIVE

            # Update the board
            new_state[i][j] = current

    return new_state


if __name__ == '__main__':
    scaling_factor = 5
    init_size = (100, 100)
    screen_size = tuple(scaling_factor * size for size in init_size)

    pg.init()
    display = pg.display.set_mode(screen_size)

    state = np.random.choice(a=[DEAD, ALIVE], size=init_size)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        state = update(state)
        surf = pg.surfarray.make_surface(state)
        display.blit(pg.transform.scale(surf, screen_size), (0, 0))
        pg.display.update()
