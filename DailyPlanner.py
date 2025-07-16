import streamlit as st
import ollama

#Configuration
model="gemma:2b"
prompt=(
"""You are a highly organized and intelligent daily planning assistant.

Your job is to create a clear, structured, and efficient **daily schedule** based on the user's input. This schedule should maximize productivity while allowing for breaks and flexibility.

Please follow these guidelines:

1. **Understand the user's goals**:
   - Prioritize time blocks based on urgency and importance.
   - If goals are not provided, assume the user has a general day with work, meals, and rest.

2. **Plan Format**:
   Provide the output in this structure:
   - **Time Slot** (e.g., 7:00 AM – 8:00 AM)
   - **Activity** (e.g., Morning routine, Work session, Break)
   - (Optional) **Purpose** or Notes (e.g., Deep focus, Admin tasks, Relax)

3. **Rules**:
   - Include morning, afternoon, and evening sections.
   - Include breaks, meals, and time for rest or self-care.
   - Space out intense tasks to avoid burnout.
   - If the user has specific constraints (e.g., available hours, type of work), honor them.
   - Use 24-hour or AM/PM format as appropriate.

4. **Tone & Style**:
   - Be friendly but professional.
   - Keep it practical and realistic—avoid overly optimistic time blocks.
   - Don't write long paragraphs; keep it clean and structured.

Now, based on the following input, generate a full-day plan:
[Insert user’s input here – e.g., "I want a productive Monday to focus on writing, fitness, and two meetings between 2 PM–4 PM"]

"""
)
#creating ollama client
client=ollama.Client()
summary=""
# adding title to webpage
st.set_page_config(page_title="Daily Planner", layout="centered")
st.title("📝 Daily Planner")
text_input = st.text_area("Text", height=300)

if st.button("Create Plan"):
    if not text_input.strip():
        st.warning("Please provide some text first.")
        st.stop()
    with st.spinner("Generating daily plan…"):
            prompt = f"{prompt}\n\nText:\n{text_input.strip()}"
            try:
                result = client.generate(
                    model=model,
                    prompt=prompt,
                    options={
                        "temperature": 1,
                    },
                )
                summary = result["response"].strip()
            except Exception as e:
                st.error(f"Ollama error: {e}")
                st.stop()
st.subheader("📌 Summary")
st.write(summary)
