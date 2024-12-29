"""
Vertical or horizontal lines.
Run as: python vertical_or_horizontal_lines.py num_lines
Provide an integer instead of num_lines to draw that many lines.
"""

import matplotlib.pyplot as plt
import random
import sys

width, height = 10, 10

def draw_random_lines(num_lines=100):
    fig, ax = plt.subplots(figsize=(width, height))
    ax.axis('off')

    for _ in range(num_lines):
        is_vertical = random.choice([True, False])
        start = random.uniform(0, 1), random.uniform(0, 1)
        length = random.uniform(0.1, 1)

        if is_vertical:
            x = start[0]
            y_start = start[1]
            y_end = y_start + length if y_start + length <= 1 else 1
            ax.plot([x, x], [y_start, y_end], color=random_color(), linewidth=random.uniform(0.5, 3))
        else:
            y = start[1]
            x_start = start[0]
            x_end = x_start + length if x_start + length <= 1 else 1
            ax.plot([x_start, x_end], [y, y], color=random_color(), linewidth=random.uniform(0.5, 3))

    plt.show()

def random_color():
    return (random.random(), random.random(), random.random())

def main():
    if len(sys.argv) > 1:
        try:
            num_lines = int(sys.argv[1])
        except ValueError:
            print("Please provide an integer for the number of lines.")
            sys.exit(1)
    else:
        num_lines = 1000

    draw_random_lines(num_lines)

if __name__ == '__main__':
    main()