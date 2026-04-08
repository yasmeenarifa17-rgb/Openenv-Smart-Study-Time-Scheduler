from flask import Flask, request, jsonify
from envs.study_env import StudyEnv

app = Flask(__name__)
env = StudyEnv()

@app.route("/")
def home():
    return "Study Scheduler Environment Running"

@app.route("/reset", methods=["POST"])
def reset():
    obs = env.reset()
    return jsonify({"observation": obs})

@app.route("/step", methods=["POST"])
def step():
    data = request.json
    action = data.get("action", 0)

    obs, reward, done, _ = env.step(action)

    return jsonify({
        "observation": obs,
        "reward": float(reward),
        "done": bool(done)
    })

@app.route("/state", methods=["GET"])
def state():
    return jsonify(env.state())

# ✅ ADD THIS (VERY IMPORTANT)
def main():
    app.run(host="0.0.0.0", port=7860)

# ✅ ADD THIS (REQUIRED)
if __name__ == "__main__":
    main()
