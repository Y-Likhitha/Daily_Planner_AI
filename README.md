# 📝 Daily Planner AI (Streamlit + Ollama)

An intelligent, AI-powered daily planner built using **Streamlit** and **Ollama** (with the **LLaMA2** or **Mistral** model). Just describe your day, and this assistant will generate a clean, productive, and personalized schedule to help you stay focused and balanced.

---

## 🚀 Features

- 🤖 Powered by LLaMA2 or Mistral via Ollama
- 🧠 Creates well-structured daily plans from natural language input
- ⏱️ Includes time blocks for work, meetings, meals, breaks, self-care, and rest
- ✍️ Accepts flexible or detailed user prompts
- 🖥️ User-friendly Streamlit interface with just one button click
- 🧩 Great for developers, students, remote workers, and productivity fans

---

## 🛠️ Tech Stack

| Component   | Description                    |
|------------|--------------------------------|
| `Streamlit`| For building the UI            |
| `Ollama`   | To run LLMs like LLaMA2 locally|
| `Python 3` | Core language used             |

---

## 📦 Installation

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/daily-planner-ai.git
cd daily-planner-ai
```

---

### 2. Create Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
---

### 2. Install Requirements

```bash
pip install streamlit ollama
```
---

### 4. Install & Run Ollama

Make sure Ollama is installed from https://ollama.com

```bash
ollama pull llama2  # Or use: ollama pull mistral
```

---

### ▶️ Run the App

```bash
streamlit run DailyPlanner.py
```
The app will open in your browser at http://localhost:8501

---

### ✍️ Example Prompt

Here’s a detailed example input you can paste into the app’s textbox to get a high-quality plan:
```bash
I need a highly productive and well-balanced schedule for my day (assume it's a weekday, Monday). Please plan a full day from 7:00 AM to 10:30 PM.

---

🧩 General Context:
- I work remotely from home.
- I am a software developer working on an AI project with tight deadlines.
- I also want to maintain physical health, manage stress, and have some personal time.
- I like starting with a calm morning routine and prefer deep focus work in the morning.

---

🎯 Key Goals (Ranked by Priority):
1. ✅ 3–4 hours of uninterrupted deep work on my AI coding task.
2. 🧑‍💻 Attend two important video meetings:
   - Team Standup at 11:00 AM (30 mins)
   - Client Presentation at 3:00 PM (1 hour)
3. 📥 Respond to emails and handle admin tasks (about 1 hour)
4. 🏋️ 1-hour gym session in the evening (between 6:00 PM and 8:00 PM)
5. 🍽️ Take proper meal breaks (breakfast, lunch, dinner)
6. 😌 Include at least 2 short breaks and 1 longer rest break
7. 🧘 Include 15–20 minutes of evening relaxation or mindfulness
8. 💤 Ensure I get at least 7 hours of sleep after the schedule ends

---

⚙️ Constraints & Preferences:
- I wake up at 7:00 AM and sleep around 10:30 PM
- Do deep work in the morning when I'm mentally sharp
- Avoid scheduling anything intense right after lunch
- Keep breaks short but regular (5–15 mins every 90–120 minutes)
- Meals should be spaced out (breakfast, lunch, dinner)
- No meetings or admin work before 10:30 AM
- Avoid back-to-back intense tasks
- Keep evenings lighter, with gym and relaxation
- Format in **12-hour AM/PM format**, starting from 7:00 AM

---

🧾 Output Format Instructions:
- Break the schedule into clearly marked **time blocks**
- Each block should contain:
   - 🕒 Time Slot (e.g., 8:00 AM – 9:30 AM)
   - 📌 Activity (e.g., Deep Work: Coding AI model)
   - 💬 Purpose / Notes (optional but helpful)
- Keep the tone clear, friendly, and professional
- Avoid overly optimistic or unrealistic stacking of tasks

---

Now please generate a realistic, cleanly structured daily plan based on the above. The plan should be balanced, productive, and human-friendly.
```

---

### 📸 Screenshot


<img width="1920" height="913" alt="Daily_Planner" src="https://github.com/user-attachments/assets/ff066b80-a57a-464c-a757-506f09262a6c" />

<img width="461" height="907" alt="Daily Planner" src="https://github.com/user-attachments/assets/9e6acd88-135b-49ea-bf19-db7d0758da23" />


---

### 🧾 File Structure
```bash
daily-planner-ai/
├── DailyPlanner.py         # Main Streamlit app file
├── README.md               # You are here
├── requirements.txt        # Python dependencies (optional)
```
---

### Built with 💻 Streamlit + 🦙 Ollama + 🧠 LLaMA2
