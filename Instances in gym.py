import gym
from gym import envs

# list all environments
all_envs = list(envs.registry.values())

# print environments ID and names
for env_spec in all_envs:
    print(env_spec.id)
