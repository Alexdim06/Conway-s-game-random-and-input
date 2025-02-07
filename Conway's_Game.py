import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Инициализация на клетките - въвеждане на координатите на живите клетки
def initialize_grid(rows, cols):
    grid = np.zeros((rows, cols), dtype=int)
    print("Enter the coordinates of live cells (e.g., '1,1 2,3 4,5 ...'):")
    input_values = input().strip().split()
    for value in input_values:
        x, y = map(int, value.split(','))
        if 0 <= x < rows and 0 <= y < cols:
            grid[x, y] = 1
        else:
            print(f"Invalid coordinates: ({x}, {y})")
    return grid

# оновяване на клетките
def update_grid(grid):
    new_grid = grid.copy()
    rows, cols = grid.shape

    for i in range(rows):
        for j in range(cols):
            # калкулиране на съседите
            total = int((grid[i, (j-1)%cols] + grid[i, (j+1)%cols] + # ляво и дясно
                         grid[(i-1)%rows, j] + grid[(i+1)%rows, j] + # горе и долу
                         grid[(i-1)%rows, (j-1)%cols] + grid[(i-1)%rows, (j+1)%cols] + # горе-ляво и горе-дясно
                         grid[(i+1)%rows, (j-1)%cols] + grid[(i+1)%rows, (j+1)%cols])) # долу-ляво и долу-дясно
            # Правила на играта
            if grid[i, j] == 1:
                if total < 2 or total > 3:
                    new_grid[i, j] = 0
            else:
                if total == 3:
                    new_grid[i, j] = 1

    return new_grid

# анимация
def animate(i, img, grid):
    new_grid = update_grid(grid)
    img.set_data(new_grid)
    grid[:] = new_grid[:]
    return img,

# старт - опции за въвеждане на размерите на матрицата и скоростта на анимацията
def main():
    rows, cols = 30, 30
    grid = initialize_grid(rows, cols)
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, animate, fargs=(img, grid), frames=1, interval=1000, save_count=50)
    plt.show()

if __name__ == "__main__":
    main()