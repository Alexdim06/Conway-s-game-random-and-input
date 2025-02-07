import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Шанс клетки 50 на 50
def initialize_grid(size):
    return np.random.choice([0, 1], size*size, p=[0.5, 0.5]).reshape(size, size)

# Ъпдейт клетки
def update_grid(grid):
    new_grid = grid.copy()
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            # страни
            total = int((
                            grid[i, (j-1)%grid.shape[1]] +  # ляво
                            grid[i, (j+1)%grid.shape[1]] +  # дясно
                            grid[(i-1)%grid.shape[0], j] +  # горе
                            grid[(i+1)%grid.shape[0], j] +  # долу
                            grid[(i-1)%grid.shape[0], (j-1)%grid.shape[1]] +  # горе-ляво
                            grid[(i-1)%grid.shape[0], (j+1)%grid.shape[1]] +  # горе-дясно
                            grid[(i+1)%grid.shape[0], (j-1)%grid.shape[1]] +  # долу-ляво
                            grid[(i+1)%grid.shape[0], (j+1)%grid.shape[1]]    # долу-дясно
                        ))
            # форумла на играта
            if grid[i, j] == 1:
                if (total < 2) or (total > 3):
                    new_grid[i, j] = 0
            else:
                if total == 3:
                    new_grid[i, j] = 1
    return new_grid

# Анимация
def animate(i, img, grid):
    new_grid = update_grid(grid)
    img.set_data(new_grid)
    grid[:] = new_grid[:]
    return img,

# Старт
def main():
    size = 50
    grid = initialize_grid(size)
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, animate, fargs=(img, grid), frames=60, interval=200, save_count=50)
    plt.show()

if __name__ == "__main__":
    main()