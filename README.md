# 🌿 Evara — Emotion-Aware Reinforcement Learning Environment

Evara is an AI-powered emotional intelligence environment that models user emotional states and adapts responses dynamically using reinforcement learning principles. It is designed as a lightweight, deployable system for experimenting with emotion-driven AI behavior.

---

## ✨ Overview

Unlike traditional chatbots, Evara focuses on:

- Understanding user emotional state  
- Maintaining emotional memory across interactions  
- Adapting responses based on feedback signals  
- Simulating an RL-style environment for emotional intelligence  

---

## 🧠 Key Features

- 💬 Emotion-aware interaction loop (input → state → response → reward)
- 🔁 Reinforcement learning-style feedback system
- 🧩 Custom OpenAI-compatible environment design
- 📊 State tracking for emotional progression
- 🐳 Fully containerized using Docker
- 🚀 Deployment-ready architecture (Hugging Face Spaces compatible)

---

## 🏗️ System Architecture

```

User Input
↓
Emotion Parser
↓
State Manager (Emotion Memory)
↓
LLM Response Generator
↓
Reward Evaluator
↓
Updated Emotional State

````

---

## ⚙️ Installation

### 1. Clone repository

```bash
git clone https://github.com/your-username/evara-env.git
cd evara-env
````

---

### 2. Create virtual environment

```bash
python -m venv venv

# Mac/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🐳 Run with Docker

### Build image

```bash
docker build -t evara .
```

### Run container

```bash
docker run -p 7860:7860 evara
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_api_key_here
API_BASE_URL=https://router.huggingface.co/v1
```

---

## 🚀 Usage

Once running, you can interact with the environment:

```python
from evara_env import EvaraEnv

env = EvaraEnv()

state = env.reset()
print(state)

next_state, reward, done, info = env.step("I feel stressed today")
print(next_state)
```

---

## 📦 Project Structure

```
evara-env/
│
├── app.py
├── evara_env.py
├── reward.py
├── requirements.txt
├── Dockerfile
├── README.md
│
└── utils/
    ├── emotion.py
    └── memory.py
```

---

## 📊 Reward System (Concept)

Evara uses a simple feedback-based reward model:

* Positive emotional improvement → +reward
* Negative emotional escalation → -reward
* Stable emotional balance → neutral reward

---

## 🌱 Future Improvements

* 📈 Emotional trend visualization dashboard
* 🧠 Long-term memory using vector database
* 🎭 Multi-personality response modes
* 📱 Web UI for real-time interaction
* 🧪 Advanced reinforcement learning reward tuning

---

## 👩‍💻 Author

Built by **Ankita Behera**

---

## 📜 License

This project is open-source and free to use for educational and research purposes.

