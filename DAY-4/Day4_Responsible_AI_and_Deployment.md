# 🌍 Day 4 — Responsible AI, Deployment & Final Submission

### 🎯 Goal

Today you’ll learn how to:

1. Secure your existing app (Gemini / CrewAI / Streamlit).
2. Add ethical + safety elements.
3. Document and publish it cleanly on GitHub.

---

## 🧩 1️⃣ Secure Your API Keys

**Never keep keys inside code.**

### ✅ Create `.env`

```ini
GOOGLE_API_KEY=YOUR_KEY_HERE
GEMINI_MODEL_NAME=gemini-1.5-flash
```

### ✅ Load it in code

```python
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
```

### ✅ Ignore secrets

```
# .gitignore
.env
__pycache__/
*.pyc
```

---

## ⚙️ 2️⃣ Add Ethical Guards & Disclaimers

### In Streamlit:

```python
st.caption("⚠️ AI-generated content. Verify before use. Do not enter personal or financial data.")
```

### Optional input filter:

```python
banned = ["password","otp","credit card","aadhaar"]
if any(w in user_prompt.lower() for w in banned):
    st.warning("Sensitive input detected – please remove it.")
    st.stop()
```

---

## 💬 3️⃣ Add Anonymous Feedback Logging

Keep logs local and safe (no names or emails).

```python
import time, json

feedback = st.text_area("Feedback (optional)")
if st.button("Submit Feedback"):
    record = {
        "ts": time.strftime("%Y-%m-%d %H:%M:%S"),
        "prompt_len": len(user_prompt),
        "feedback": feedback[:300]
    }
    with open("feedback_log.jsonl","a",encoding="utf-8") as f:
        f.write(json.dumps(record)+"\n")
    st.success("Thanks for helping improve this app responsibly!")
```

---

## 📘 4️⃣ Add a README.md

````markdown
# Responsible AI App

## What it does
Generates text or runs multi-agent CrewAI workflow.

## How to run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Responsible AI Practices
* API keys in `.env`
* AI disclaimer shown
* No sensitive data stored
* Local feedback logging
````

---

## 🚀 5️⃣ Push to GitHub Safely

```bash
git init
echo ".env" >> .gitignore
git add .
git commit -m "Secure API keys + disclaimer + feedback + README"
git branch -M main
git remote add origin https://github.com/<username>/<repo>.git
git push -u origin main
```

✅ Do not upload `.env`.

---

## 📊 6️⃣ Optional Deploy Links

* **Streamlit Cloud:** add API keys as Secrets.
* **Hugging Face Spaces:** set Environment Variables safely.

---

## 🧾 7️⃣ Final Checklist

| ✅ Item     | Description                              |
| :--------- | :--------------------------------------- |
| Secrets    | In `.env`, ignored in git                |
| Disclaimer | Visible in app                           |
| Feedback   | Works without collecting personal data   |
| README     | Clear instructions + responsibility note |
| Repo       | Clean structure + 1 commit               |
| Optional   | Public deploy link                       |

---

## 🧠 Evaluation Rubric

| Area                                       | Weight |
| ------------------------------------------ | ------ |
| Security & Privacy Practices               | 25 %   |
| Functional App                             | 30 %   |
| Responsible Design (Disclaimer + Feedback) | 20 %   |
| Documentation (README)                     | 15 %   |
| Clean Repo & Commit                        | 10 %   |

---

## 🏠 Homework

1. Write 150 words: “What Responsible AI means to me.”
2. Note deployment steps and issues you fixed.
3. Add 2–3 test outputs in README under “Sample Results.”

---

### 🌟 End of Day 4 — Responsible AI & Final Deployment

> “Great engineers don’t just build AI that works — they build AI that can be trusted.” 💚
