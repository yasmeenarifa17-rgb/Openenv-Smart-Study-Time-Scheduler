from envs.study_env import StudyEnv
import random

def run_task():
    env = StudyEnv()
    obs = env.reset()

    done = False
    total_reward = 0

    while not done:
        action = random.randint(0, 3)
        obs, reward, done, _ = env.step(action)
        total_reward += reward

    return total_reward


if __name__ == "__main__":
    print("START")

    easy = run_task()
    print("Easy:", easy)

    medium = run_task()
    print("Medium:", medium)

    hard = run_task()
    print("Hard:", hard)

    print("END")
