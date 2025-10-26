# 🧠 Day 1 — The Beginning of Generative AI

### Theme: "How Computers Learned to Imagine"

---

## 👋 Welcome!

Hey there!  
Today we start an exciting journey — teaching computers not just to *think*, but to *create*.

Imagine a robot that can write poems, draw pictures, and even make jokes.  
That's what **Generative AI** is all about.

---

## 🌟 What You'll Learn Today

By the end of Day 1, you'll know:

1. What AI, Machine Learning, and Deep Learning mean.  
2. How Generative AI is different from normal AI.  
3. How large language models (LLMs) make sentences.  
4. What "prompt engineering" means.  
5. How to build a small "Creative Text Generator" app using Gemini API and Streamlit.

---

## 🧙‍♂️ A Little Story

Long ago (well, 2012 😄), Google ran a big computer network that watched thousands of YouTube videos.  
Nobody told it what to look for — but it *learned* to recognize **cats** on its own! 🐱

That moment changed everything.  
Computers stopped being just calculators… they started becoming **learners**.  
And now — creators.

---

## 🧩 Before Generative AI — The "Old" AI

### What Normal AI Does

- Looks at data.  
- Finds patterns.  
- Makes predictions.

### Example

| Input | Output |
|--------|---------|
| House size, location, age | Predict price 🏠 |
| Email text | Predict "spam" or "not spam" 📩 |

It's smart, but… it doesn't *create* anything new.  
It can **recognize**, not **imagine**.

### Whiteboard Idea

```bash
Data → Model → Prediction
```

🤖 "I can tell you what this is,  
but I can't make something new."

---

## 🎨 Then Came Generative AI

Now computers can **create**:  
stories, songs, code, and images!

### Examples

| Input | Output |
|--------|--------|
| "Write a bedtime story about a robot." | A brand-new story 🪄 |
| "Draw a house on Mars." | An original picture 🏠🪐 |
| "Make a poem about friendship." | A cute little poem ❤️ |

### Whiteboard Idea

```bash
Prompt → Model → New Content
```

---

## 🔗 Want to See the Magic Inside?

Check out this amazing visual explainer:  
👉 **[The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)**  
It shows, step-by-step, how modern AI models (like Gemini or ChatGPT) understand language.

---

## ⚙️ How Large Language Models (LLMs) Write

LLMs don't "know" language like humans.  
They *guess* the next word, one by one, using math and probabilities.

### Example

```bash
I like eating ___
→ pizza (0.6)
→ rice  (0.3)
→ books (0.1)
```

So the model picks "pizza,"  
and now we have "I like eating pizza." 🍕

### Key Idea

- It repeats this again and again to make full sentences.  
- Billions of examples help it guess well.  

### Whiteboard Sketch

```bash
Word 1 → Attention → Word 2 → ... → Output
```

---

## 🧍‍♀️ AI vs Human Creativity

Let's compare!  
Ask a student to write a 2-line poem.  
Then ask Gemini to write one too.

Now guess which is which. 😄

### Whiteboard Words

```bash
Human = Emotion ❤️ | Context 🧠 | Imagination 🌈
AI = Pattern 📊 | Probability 🎲 | Speed ⚡
```

Both are amazing — but in different ways.

---

## ✍️ Prompt Engineering — Talking to AI

### What It Is

"Prompt Engineering" means giving AI clear, smart instructions.

It's like teaching your friend a game — the better you explain, the better they play.

### Types of Prompts

| Type | Example |
|------|----------|
| **Instruction** | "Write a poem about exams." |
| **Role based** | "You are a teacher; explain AI to a 10-year-old." |
| **Few-shot** | "Example: cat→animal. dog→animal. car→?" |
| **Chain-of-Thought** | "Let's reason step-by-step." |

### Whiteboard Loop

```bash
User → Model → Output
↑                ↓
Tweak Prompt ← Review
```

---

## 💻 Mini Project — Creative Text Generator

Let's build our first mini app!

```python
import streamlit as st
import google.generativeai as genai

# 1️⃣ Set up Gemini API Key
genai.configure(api_key="YOUR_API_KEY")

# 2️⃣ Choose model
model = genai.GenerativeModel("gemini-2.5-flash")

# 3️⃣ App Title
st.title("🎨 Creative Text Generator")

# 4️⃣ Add a System Prompt (persona)
system_prompt = st.text_area("System Prompt (Who the AI is)", "You are a friendly teacher.")

# 5️⃣ User Prompt (task)
prompt = st.text_area("Enter a prompt:")

# 6️⃣ Creativity control
temp = st.slider("Creativity", 0.1, 1.0, 0.7)

# 7️⃣ Generate output
if st.button("Generate"):
    full_prompt = f"{system_prompt}\n\nUser Request:\n{prompt}"
    response = model.generate_content(full_prompt, generation_config={"temperature": temp})
    st.write(response.text)
```

Run it with

```bash
streamlit run app.py
```

Try different **system prompts**:

| System Prompt          | Result                     |
| ---------------------- | -------------------------- |
| "You are a poet."      | Writes in rhymes           |
| "You are a scientist." | Uses facts and logic       |
| "You are a kid."       | Simple and funny sentences |

---

## 💡 Fun Mini Ideas

| Idea            | Example                                     |
| --------------- | ------------------------------------------- |
| Poem Maker      | "Write a poem about college life."          |
| Joke Bot        | "Tell a funny tech joke."                   |
| Study Buddy     | "Explain neural networks in 2 lines."       |
| Story Generator | "Tell a story about a robot and a student." |
| Compliment Bot  | "Say something nice about Sarika."          |

Each idea only changes the **system prompt**!

---

## 🧩 Quick Quiz

1. What's the difference between normal AI and Generative AI?
2. What does "temperature" control?
3. What does a system prompt do?
4. How do LLMs build sentences?

---

## 🏁 Wrap-Up

* AI used to predict — now it creates.
* Prompts are the language between us and AI.
* With Gemini API + Streamlit, you just built your first AI app!

Tomorrow → we'll teach AI to **see** 🎨 (images + multimodal generation).

---

## 📚 Helpful Links

* 🔗 **Illustrated Transformer:** [https://jalammar.github.io/illustrated-transformer/](https://jalammar.github.io/illustrated-transformer/)
* 📘 **Learn Prompting:** [https://learnprompting.org](https://learnprompting.org)
* 💻 **Gemini API Docs:** [https://ai.google.dev](https://ai.google.dev)
* 🎥 **YouTube:** Gemini for Developers (Google Developers Channel)

---

*"AI doesn't replace your creativity — it amplifies it."* 🚀
