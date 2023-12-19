import sys
import os

#script_directory = os.path.dirname(os.path.realpath(__file__))
#sys.path.append(script_directory)

import gymnasium as gym 
#import gym
env = gym.make('CartPole-v0', render_mode='human')  # construct environment 
env.reset()  # reset a turn
for _ in range(1000):
    env.render()  # show images
    action = env.action_space.sample() # randomly select an action from spaces
    env.step(action) # apply the specific action in the brackets
env.close() # close the environment
