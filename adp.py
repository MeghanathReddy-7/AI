import numpy as np

# Parameters
num_states = 10   # Number of states
num_actions = 2   # Number of actions
gamma = 0.6       # Discount factor

# Initialize Value function
V = np.zeros(num_states)

def policy_evaluation(policy):
    for state in range(num_states):
        action = policy[state]
        next_state = (state + action) % num_states
        reward = np.random.rand()
        V[state] = reward + gamma * V[next_state]

def policy_improvement():
    policy = np.zeros(num_states, dtype=int)
    for state in range(num_states):
        q_values = np.zeros(num_actions)
        for action in range(num_actions):
            next_state = (state + action) % num_states
            reward = np.random.rand()
            q_values[action] = reward + gamma * V[next_state]
        policy[state] = np.argmax(q_values)
    return policy

policy = np.zeros(num_states, dtype=int)
for _ in range(100):  # Iteratively improve policy
    policy_evaluation(policy)
    policy = policy_improvement()

print("Final policy:", policy)
print("Value function:", V)
