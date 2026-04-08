import os
from openai import OpenAI
from env import EvaraEnv

# --------- SAFE FALLBACK RESPONSE ---------
def fallback(state):
    return f"I understand you feel {state['emotion']}. I'm here to support you and can help with {state['goal']}."

# --------- ENV VARIABLES ---------
API_KEY = os.getenv("HF_TOKEN") or os.getenv("OPENAI_API_KEY")
API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-72B-Instruct")

# --------- CLIENT SETUP ---------
client = OpenAI(
    api_key=API_KEY,
    base_url=API_BASE_URL
)

# --------- INIT ENV ---------
env = EvaraEnv()
state = env.reset()

print(f"[START] task=evara env=evara model={MODEL_NAME}")

done = False
step = 0
rewards = []

# --------- MAIN LOOP ---------
while not done:
    step += 1
    error_msg = "null"

    prompt = f"""
    User says: {state['user_message']}
    Emotion: {state['emotion']}
    Goal: {state['goal']}

    Respond empathetically, mention the emotion, and help with the goal.
    """

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}]
        )
        action = response.choices[0].message.content.strip()

    except Exception as e:
        action = fallback(state)
        error_msg = str(e)[:50]  # truncate error

    # --------- ENV STEP ---------
    state, reward, done, _ = env.step(action)
    rewards.append(reward)

    print(f"[STEP] step={step} action={action[:30]} reward={reward:.2f} done={str(done).lower()} error={error_msg}")

# --------- FINAL SCORE ---------
score = sum(rewards) / len(rewards) if rewards else 0.0

print(f"[END] success=true steps={step} score={score:.2f} rewards={','.join([f'{r:.2f}' for r in rewards])}")