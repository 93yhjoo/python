import numpy as np
import gym
import matplotlib.pyplot as plt
from gym.envs.registration import register
import random as pr
"""값이 같을 경우 랜덤한  방향으로 가라"""


def rargmax(vector):
    m=np.amax(vector)
    indices=np.nonzero(vector == m)[0]
    return pr.choice(indices)


register(
    id='FrozenLake-v3',
    entry_point='gym.envs.toy_text:FrozenLakeEnv',
    kwargs={'map_name': '4x4',
            'is_slippery': False}
)

env = gym.make('FrozenLake-v3')
"""Q라는 테이블을 만드는데 2천번 돈다."""
Q=np.zeros([env.observation_space.n,env.action_space.n])
num_episodes=2000
rList=[]
for i in range(num_episodes):
    state=env.reset()
    rAll=0
    done=False

    while not done:
        action=rargmax(Q[state,:])
        new_state, reward, done,_=env.step(action)
        Q[state,action]=reward+np.max(Q[new_state,:])
        rAll+=reward
        state=new_state

    rList.append(rAll)


print('success rate:'+str(sum(rList)/num_episodes))
print('Final Q-table value')
print('Left Down Right up')
print(Q)
plt.bar(range(len(rList)),rList,color='blue')
plt.show()