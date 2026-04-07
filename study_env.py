from pydantic import BaseModel
import gymnasium as gym
from gymnasium import spaces
import numpy as np
import random

# Typed models
class Observation(BaseModel):
    fatigue: int
    progress_a: int
    progress_b: int
    progress_c: int

class StudyEnv(gym.Env):
    def __init__(self):
        super().__init__()

        self.action_space = spaces.Discrete(4)

        self.observation_space = spaces.Box(
            low=0, high=100, shape=(4,), dtype=np.int32
        )

        self.reset()

    def reset(self):
        self.fatigue = 10
        self.progress = [0, 0, 0]
        return Observation(
            fatigue=self.fatigue,
            progress_a=self.progress[0],
            progress_b=self.progress[1],
            progress_c=self.progress[2]
        )

    def step(self, action):
        reward = 0

        # Increase fatigue if studying
        if action in [0, 1, 2]:
            self.fatigue += 10
            self.progress[action] += 5
            reward += 0.3

        elif action == 3:  # break
            self.fatigue = max(0, self.fatigue - 15)
            reward += 0.5

        # Penalty if too tired
        if self.fatigue > 70:
            reward -= 0.5

        if self.fatigue > 90:
            reward -= 1

        done = self.fatigue >= 100 or sum(self.progress) >= 150

        obs = Observation(
            fatigue=self.fatigue,
            progress_a=self.progress[0],
            progress_b=self.progress[1],
            progress_c=self.progress[2]
        )

        return obs, reward, done, {}

    def state(self):
        return {
            "fatigue": self.fatigue,
            "progress": self.progress
        }