# Authored By = Nazanin Zarei - Shadmehr Salehi - Foozhan Fahimzade
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

# Get the initial state of the cells from the user
initial_state = np.array(eval(input("Enter the initial state of the cells as a 2D array of 0 (dead cells) & 1 (living cells): ")))

# Get the size of the initial state
initial_state_size = initial_state.shape

# Determine the size of the board based on the maximum dimension of the initial state
board_size = max(initial_state_size)

# Get the number of iterations from the user
num_iterations = int(input("Enter the number of iterations: "))

# Create a board of zeros with the appropriate size
board = np.zeros((board_size, board_size))

# Fill in the board with the initial state
board[0:initial_state_size[0], 0:initial_state_size[1]] = initial_state

# Define the function to update the state of the cells at each iteration
def update(state):
    # Create a copy of the current state of the cells
    new_state = state.copy()

    # Loop over each cell in the board
    for i in range(board_size):
        for j in range(board_size):
            # Compute the number of neighboring cells that are alive
            num_alive_neighbors = np.sum(state[max(0, i-1):min(board_size, i+2), max(0, j-1):min(board_size, j+2)]) - state[i, j]

            # Apply the rules of the Game of Life to determine the new state of the cell
            if state[i, j] == 1 and (num_alive_neighbors < 2 or num_alive_neighbors > 3):
                new_state[i, j] = 0
            elif state[i, j] == 0 and num_alive_neighbors == 3:
                new_state[i, j] = 1

    # Update the state of the cells
    state[:] = new_state[:]

    # Return the updated state
    return state

# Create a figure to display the simulation
fig = plt.figure()

# Define the animation function
def animate(iteration):
    # Update the state of the cells
    update(board)

    # Clear the previous plot
    plt.clf()

    # Create a new plot of the updated state of the cells
    plt.imshow(board, cmap='gray')

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_iterations, interval=500)

# Show the animation
plt.show()
