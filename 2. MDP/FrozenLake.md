Frozen Lake

![Frozen lake image](image.png)

Action space: discrete(4)
Observation spzce; discrete (16)
import: gym.make("FrozenLake-v1")

Frozen lake involves crossing a frozen lake from Start(S) to Goal(G) without falling into any Holes(H) by walking over the Frozen(F) lake. The agent may not always move in the intended direction due to the slippery nature of the frozen lake.

Action space;
The agent takes a 1-element vector for actions. The action space is (dir), where dir decides direction to move in which can be:

0: LEFT
1: DOWN
2: RIGHT
3: UP

Observation spzce;
The observation is a value representing the agent’s current position as current_row * nrows + current_col (where both the row and col start at 0). For example, the goal position in the 4x4 map can be calculated as follows: 3 * 4 + 3 = 15. The number of possible observations is dependent on the size of the map. For example, the 4x4 map has 16 possible observations.

Rewards
Reward schedule:

Reach goal(G): +1
Reach hole(H): 0
Reach frozen(F): 0

Argument

gym.make('FrozenLake-v1', desc=None, map_name="4x4", is_slippery=True)

desc: Used to specify custom map for frozen lake.