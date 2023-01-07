import numpy as np
import pygame as pg

DEAD = 0
ALIVE = 200


def update(old_state: np.array):
    # Clean state to update
    new_state = np.empty_like(old_state)

    # For every cell
    for i in range(len(old_state)):
        for j in range(len(old_state[i])):
            # Dimensions for the Neighbors
            num_neighbor = 1
            left = max(0, i - num_neighbor)
            right = max(0, i + num_neighbor + 1)
            bottom = max(0, j - num_neighbor)
            top = max(0, j + num_neighbor + 1)

            # Slice out the neighbors, delete the center (current cell).
            current = old_state[i][j]
            n = old_state[left:right, bottom:top]
            n = np.delete(n, n.size // 2)
            l_count = np.count_nonzero(n == ALIVE)

            # Apply the lifecycle rules for Conway's Game of Life
            if current == ALIVE:
                if l_count == 2 or l_count == 3:
                    current = ALIVE
                else:
                    current = DEAD
            else:
                if l_count == 3:
                    current = ALIVE

            # Update the board
            new_state[i][j] = current

    return new_state


if __name__ == '__main__':
    scaling_factor = 5
    init_size = (200, 200)
    screen_size = (init_size[0] * scaling_factor, init_size[1] * scaling_factor)

    pg.init()
    display = pg.display.set_mode(screen_size)
    state = np.random.choice(a=[DEAD, ALIVE], size=init_size)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
        state = update(state)
        surf = pg.surfarray.make_surface(state)
        display.blit(pg.transform.scale(surf, screen_size), (0, 0))
        pg.display.update()
