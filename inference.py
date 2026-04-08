from envs.study_env import StudyEnv
import random

def run_task(task_name):
    env = StudyEnv()
    obs = env.reset()

    done = False
    total_reward = 0
    step_count = 0

    print(f"[START] task={task_name}", flush=True)

    while not done:
        action = random.randint(0, 3)
        obs, reward, done, _ = env.step(action)

        step_count += 1
        total_reward += reward

        print(f"[STEP] step={step_count} reward={reward}", flush=True)

    print(f"[END] task={task_name} score={total_reward} steps={step_count}", flush=True)


if __name__ == "__main__":
    run_task("easy")
    run_task("medium")
    run_task("hard")
