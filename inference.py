from envs.study_env import StudyEnv
import random

def run_task(task_name):
    # Start block
    print(f"[START] task={task_name}", flush=True)

    # Example step
    step = 1
    reward = 0.5
    print(f"[STEP] step={step} reward={reward}", flush=True)

    # End block
    score = 0.95
    steps = step
    print(f"[END] task={task_name} score={score} steps={steps}", flush=True)


if __name__ == "__main__":
    # Replace "StudyScheduler" with your actual task name
    run_task("StudyScheduler")


   
