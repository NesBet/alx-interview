#!/usr/bin/python3
'''Calculating Island Perimeter'''


def island_perimeter(grid):
    '''Returns the perimeter of the island described in grid'''
    counter = 0
    grid_max = len(grid) - 1  # Index of the last list.
    lst_max = len(grid[0]) - 1  # Index of the last square

    for lst_idx, lst in enumerate(grid):
        for land_idx, land in enumerate(lst):
            if land == 1:
                # left and right
                if land_idx == 0:
                    counter += 1

                    if lst[land_idx + 1] == 0:
                        counter += 1
                elif land_idx == lst_max:
                    if lst[land_idx - 1] == 0:
                        counter += 1

                    counter += 1
                else:
                    # Left
                    if lst[land_idx - 1] == 0:
                        counter += 1

                    # Right
                    if lst[land_idx + 1] == 0:
                        counter += 1

                if lst_idx == 0:
                    counter += 1

                    # Under side
                    if grid[lst_idx + 1][land_idx] == 0:
                        counter += 1
                elif lst_idx == grid_max:
                    # Upper side
                    if grid[lst_idx - 1][land_idx] == 0:
                        counter += 1

                    counter += 1
                else:
                    # Upper side
                    if grid[lst_idx - 1][land_idx] == 0:
                        counter += 1

                    # Under side
                    if grid[lst_idx + 1][land_idx] == 0:
                        counter += 1

    return counter
