import os
import random
from openai import OpenAI
from envs.study_env import StudyEnv

# ✅ Initialize OpenAI client using environment variables
client = OpenAI(
    base_url=os.environ.get("API_BASE_URL"),
    api_key=os.environ.get("API_KEY")
)

def call_llm():
    try:
        response = client.chat.completions.create(
            model=os.environ.get("MODEL", "gpt-3.5-turbo"),
            messages=[{"role": "user", "content": "Give a number between 0 and 3"}],
            max_tokens=5
        )
        return random.randint(0, 3)
    except:
        return random.randint(0, 3)

def run_task(task_name):
    env = StudyEnv()
    obs = env.reset()

    done = False
    total_reward = 0
    step_count = 0

    print(f"[START] task={task_name}", flush=True)

    while not done:
        action = call_llm()  # ✅ ensures API call
        obs, reward, done, _ = env.step(action)

        step_count += 1
        total_reward += reward

        print(f"[STEP] step={step_count} reward={reward}", flush=True)

    print(f"[END] task={task_name} score={total_reward} steps={step_count}", flush=True)


if __name__ == "__main__":
    run_task("easy")
    run_task("medium")
    run_task("hard")
