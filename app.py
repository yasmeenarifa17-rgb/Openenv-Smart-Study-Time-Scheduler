from flask import Flask, request, jsonify
from envs.study_env import StudyEnv

app = Flask(__name__)
env = StudyEnv()

@app.route("/")
def home():
    return "Study Scheduler Environment Running"

# ✅ RESET
@app.route("/reset", methods=["POST"])
def reset():
    obs = env.reset()

    if hasattr(obs, "__dict__"):
        obs = obs.__dict__

    return jsonify({"observation": obs})

# ✅ STEP
@app.route("/step", methods=["POST"])
def step():
    data = request.json
    action = data.get("action", 0)

    obs, reward, done, _ = env.step(action)

    if hasattr(obs, "__dict__"):
        obs = obs.__dict__

    return jsonify({
        "observation": obs,
        "reward": float(reward),
        "done": bool(done)
    })

# ✅ STATE
@app.route("/state", methods=["GET"])
def state():
    state = env.state()

    if hasattr(state, "__dict__"):
        state = state.__dict__

    return jsonify(state)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
