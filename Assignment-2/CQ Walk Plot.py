import random
import numpy as np
import matplotlib.pyplot as plt

def one_walk (n_steps):
    
    position = 0
    
    for _ in range(n_steps):
        step  = random.choice([-1, 1])
        position += step
    return position

def many_walks(n_walks, n_steps):
    
    positions = np.empty(n_walks)
    
    for x in range(n_walks):
        positions[x] = one_walk(n_steps)
    
    plt.hist(positions, bins=20, edgecolor="black")
    plt.xlabel("Final position")
    plt.ylabel("Frequency")
    plt.title(f"Positions After {n_steps} Steps ({n_walks} times)")
    plt.show()

    return positions

positions = many_walks(n_walks = 10000, n_steps=1000)