import gym  

env = gym.make('CartPole-v0')  
env.reset()  
for _ in range(1000):
    env.render()

    done = False

    if done:
        env.reset()

    env.render()  
    action = env.action_space.sample() 
    observation, reward, done, info = env.step(action)
    print(observation)# an observation from four dimensions

env.close()    


# env.step has four return values: (observation, reward, done, info);
# observation: state information of the environment;
# reward: amount of reward achieved by the previous action;
# done: whether the episode if has ended; if yes, the environment should reset;
# info: diagnostic information useful for debugging.
