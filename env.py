import random

class EvaraEnv:

    def __init__(self):
        self.step_count = 0
        self.max_steps = 5

    def reset(self):
        self.step_count = 0
        self.state = {
            "user_message": "I feel tired and lost",
            "emotion": random.choice(["sad", "happy", "anxious"]),
            "goal": random.choice(["advice", "talk", "motivation"])
        }
        return self.state

    def step(self, action):
        self.step_count += 1
        reward = 0.0
        done = False

        action = action.lower()

        if self.state["emotion"] in action:
            reward += 0.4

        if self.state["goal"] in action:
            reward += 0.3

        if any(w in action for w in ["understand", "feel", "help"]):
            reward += 0.3

        if self.step_count >= self.max_steps:
            done = True

        return self.state, round(reward, 2), done, {}

    def state(self):
        return self.state