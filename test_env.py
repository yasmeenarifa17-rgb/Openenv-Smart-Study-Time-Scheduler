from envs.study_env import StudyEnv
import random

env = StudyEnv()
obs = env.reset()

done = False
total_reward = 0

print("Simulation Start\n")

while not done:
    action = random.randint(0, 3)
    obs, reward, done, _ = env.step(action)
    total_reward += reward

    print(f"Action: {action}, State: {obs}, Reward: {reward}")

print("\nFinished")
print("Total Reward:", total_reward)