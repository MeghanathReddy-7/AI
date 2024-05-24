import numpy as np

n_states = 10
n_actions = 2
goal_state = 9
epochs = 1000
exploration_prob = 0.1
learning_rate = 0.1
discount_factor = 0.9

Q_table = np.zeros((n_states, n_actions))

for epoch in range(epochs):
    current_state = np.random.randint(0, n_states)

    while current_state != goal_state:
        if np.random.rand() < exploration_prob:
            action = np.random.randint(0, n_actions)
        else:
            action = np.argmax(Q_table[current_state])

        next_state = (current_state + 1) % n_states
        reward = 1 if next_state == goal_state else 0

        Q_table[current_state, action] += learning_rate * \
            (reward + discount_factor *
             np.max(Q_table[next_state]) - Q_table[current_state, action])

        current_state = next_state

print("Learned Q-table:")
print(Q_table)
