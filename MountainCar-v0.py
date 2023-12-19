# import gym
# env = gym.make('MountainCar-v0')

# #observation space = Box([-1.2  -0.07], [0.6  0.07], (2,), float32)
# #observe numpy arrays of length 2, data type; float32
# print('observation space = {}'.format(env.observation_space))
# print('action space = {}'.format(env.action_space))
# print('observation range = {} ~ {}'.format(env.observation_space.low,
#         env.observation_space.high))

# # number of actions = 3, that is {0, 1, 2}
# # 0: left, 1:non action, 2:right
# print('number of actions = {}'.format(env.action_space.n))


import gym
import numpy as np


class SimpleAgent:
    def __init__(self, env):
        pass
    
    def decide(self, observation): # decision making function
        position, velocity = observation
        lb = min(-0.09 * (position + 0.25) ** 2 + 0.03,
                0.3 * (position + 0.9) ** 4 - 0.008)
        ub = -0.07 * (position + 0.38) ** 2 + 0.07
        if lb < velocity < ub:
            action = 2
        else:
            action = 0
        return action # return action number

    def learn(self, *args): # learning function
        pass #no RL agent -> cannot learn, only decide according to the mathematical formula
    

#train: False -- during testing, let agent remain unchanged 
#train: True -- during training, let agent train    
    
def play(env, agent, render=False, train=False):
    episode_reward = 0. # total rewrd
    observation = env.reset() # reset and start new episode
    while True: # continuously iterate, until finished
        if render: # if show images
            env.render() # show images
        action = agent.decide(observation)
        next_observation, reward, done, _ = env.step(action) # perform action
        episode_reward += reward # collect episode reward
        if train: # determine if train agent
            agent.learn(observation, action, reward, done) # learn
        if done: # episode finished, jump out of iterttion
            break
        observation = next_observation
    return episode_reward # return total reward


env = gym.make('MountainCar-v0')
env.seed(3) # random seed
agent = SimpleAgent(env)
print('observstion space = {}'.format(env.observation_space))
print('action space = {}'.format(env.action_space))
print('pbservation range = {} ~ {}'.format(env.observation_space.low,
        env.observation_space.high))
print('number of actions = {}'.format(env.action_space.n))

episode_reward = play(env, agent, render=True)
print('total reward = {}'.format(episode_reward))

episode_rewards = [play(env, agent) for _ in range(100)]
print('average reward = {}'.format(np.mean(episode_rewards)))