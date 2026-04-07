from envs.study_env import StudyEnv
import random

def easy_task():
    env = StudyEnv()
    env.reset()
    total_reward = 0

    for _ in range(20):
        action = random.randint(0, 3)
        _, reward, done, _ = env.step(action)
        total_reward += reward
        if done:
            break

    return round(total_reward / 20, 2)


def medium_task():
    env = StudyEnv()
    env.reset()
    total_reward = 0

    for _ in range(30):
        action = random.randint(0, 3)
        _, reward, done, _ = env.step(action)
        total_reward += reward
        if done:
            break

    return round(total_reward / 30, 2)


def hard_task():
    env = StudyEnv()
    env.reset()
    total_reward = 0

    for _ in range(50):
        action = random.randint(0, 3)
        _, reward, done, _ = env.step(action)
        total_reward += reward
        if done:
            break

    return round(total_reward / 50, 2)