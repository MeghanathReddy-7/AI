import numpy as np

# Parameters
gamma = 0.9  # Discount factor
num_states = 10  # Number of states
num_actions = 2  # Number of actions

# Initialize Q-Table with zeros
Q = np.zeros((num_states, num_actions))

# Define the reward function and transition probabilities
def reward(state, action):
    return np.random.rand()

def next_state(state, action):
    return (state + action) % num_states

def bellman_update(state, action, reward, next_state):
    best_next_action = np.argmax(Q[next_state, :])
    Q[state, action] = reward + gamma * Q[next_state, best_next_action]

# Example of a training loop with Bellman update
for episode in range(1000):
    state = np.random.randint(num_states)
    while True:
        action = np.random.randint(num_actions)
        next_s = next_state(state, action)
        r = reward(state, action)
        bellman_update(state, action, r, next_s)
        state = next_s
        if state == 0:  # Example stopping condition
            break

print("Q-Table after applying Bellman updates:")
print(Q)
