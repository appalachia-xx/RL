import gymnasium as gym

# LunarLander-v2, where the agent controls a spaceship that needs to land safely
env = gym.make("LunarLander-v2", render_mode="human")


observation, info = env.reset()

for _ in range(1000):
    action = env.action_space.sample()  # sampled random actions, agent policy that uses the observation and info

    observation, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        observation, info = env.reset()

env.close()

# reset, the environment to get the first observation of the environment

# step, moving a robot or pressing a button on a games’ controller that causes a change 
# within the environment.

# As a result, the agent receives a new observation from the updated environment along with 
# a reward for taking the action. This reward could be for instance positive for destroying 
# an enemy or a negative reward for moving into lava.

# However, after some timesteps, the environment may end, this is called the terminal state. 
# For instance, the robot may have crashed, or the agent have succeeded in completing a task, 
# the environment will need to stop as the agent cannot continue. In gymnasium, if the environment
# has terminated, this is returned by step. Similarly, we may also want the environment to end 
# after a fixed number of timesteps, in this case, the environment issues a truncated signal. 
# If either of terminated or truncated are true then reset should be called next to restart the 
# environment.