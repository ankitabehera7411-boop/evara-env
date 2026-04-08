def easy(action, emotion):
    return 1.0 if emotion in action else 0.0

def medium(action, goal):
    return 1.0 if goal in action else 0.0

def hard(action):
    score = 0
    for word in ["understand", "help", "feel"]:
        if word in action:
            score += 0.33
    return min(score, 1.0)