# 🤖 Day 3 — From Generators to Agents  
### Theme: *"When AI starts to think, plan, and act"*

---

## 🌟 Welcome to Day 3!

In Day 1, we taught AI to **write**.  
In Day 2, we taught AI to **see**.  
Today, we’ll teach AI to **act** — to think, plan, and complete tasks like a real assistant.

This is where we move from **models** to **agents** — from just generating content to making decisions.

---

## 🧠 What Is an AI Agent?

Imagine you have a **smart helper** that can:
- Think step by step 🪜  
- Decide what to do next 🧭  
- Use tools like Google Search or APIs 🧰  
- Remember what it learned 🧠  
- Work toward a goal 🎯  

That’s what an **AI Agent** does!

While normal AI (like ChatGPT) gives answers when asked,  
**Agents** can *plan* actions, *choose* tools, and *execute* steps automatically.

---

### 💬 Example

Let’s say you ask:

> “Summarize the latest news about space exploration.”

A **normal model** will just generate text.  
But an **agentic AI** might:
1. Search the web for recent news 🕵️‍♀️  
2. Summarize each article 📰  
3. Combine them into one report 📄  

That’s not just answering — that’s **thinking and acting**.

---

## ⚙️ AI Model vs AI Agent

| 💬 **Model** | 🧠 **Agent** |
|--------------|--------------|
| Gives you a single reply | Performs multiple steps |
| Has no memory | Remembers past context |
| Follows your prompt only | Plans and executes goals |
| Needs your help | Works autonomously |

---

## 🔍 How Agents Work (Visual)

```

Human → Agent → Tools → Output
↖ Memory ↗

````

The **agent** is like a brain that uses:
- **Tools** (APIs, searches)
- **Memory** (to recall context)
- **Logic** (to plan tasks)
- **Goals** (to stay focused)

---

## 💡 Key Concepts in Agentic AI

| Concept | Meaning | Example |
|----------|----------|----------|
| 🪜 **Reasoning** | Thinking step-by-step | “First find data, then summarize.” |
| 🧠 **Memory** | Storing and recalling past info | “Remember my name is Sarika.” |
| 🧰 **Tool Use** | Using external systems | “Search online for answers.” |
| 🎯 **Goal Orientation** | Staying focused on tasks | “Finish report before replying.” |

---

## 💻 Hands-On Project: **Multi-Agent Crew with Gemini**

Today, we’ll build a small **CrewAI project** with three agents:  
1. 🕵️‍♀️ Researcher — finds facts  
2. ✍️ Writer — creates readable content  
3. 🧑‍💼 Editor — polishes the final result  

These agents will *talk to each other* to produce one beautiful final output.

---

## 🧩 Code Setup

### 🧰 Step 1: Install Requirements
```bash
pip install crewai langchain langchain-google-genai duckduckgo-search python-dotenv streamlit
````

### 📦 Step 2: Create `.env` file

```ini
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
GEMINI_MODEL_NAME=gemini-1.5-flash
```

---

## 🧠 Step 3: CrewAI Code Example

```python
from crewai import Agent, Task, Crew, Process
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import DuckDuckGoSearchRun
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)
search_tool = DuckDuckGoSearchRun()

# Define Agents
researcher = Agent(
    role="Research Assistant",
    goal="Find the latest AI news and summarize it clearly.",
    backstory="An AI who loves exploring new technology updates for students.",
    llm=llm,
    tools=[search_tool]
)

writer = Agent(
    role="Content Writer",
    goal="Turn research summaries into friendly articles for college students.",
    backstory="Writes like a friend who explains tough concepts simply.",
    llm=llm
)

editor = Agent(
    role="Editor",
    goal="Polish and organize the article for clarity and flow.",
    backstory="An editor who fixes grammar and adds '3 key takeaways.'",
    llm=llm
)

# Define Tasks
task1 = Task(
    description="Research the latest AI news and summarize in 200 words with sources.",
    expected_output="A 200-word summary with 2–3 sources.",
    agent=researcher
)

task2 = Task(
    description="Use the summary to write a student-friendly blog with emojis and subheadings.",
    expected_output="A clear blog-style article for students.",
    agent=writer
)

task3 = Task(
    description="Edit and polish the article for readability and grammar.",
    expected_output="A final polished article ready to post.",
    agent=editor
)

# Run the Crew
crew = Crew(
    agents=[researcher, writer, editor],
    tasks=[task1, task2, task3],
    process=Process.sequential,
    memory=True
)

result = crew.kickoff(inputs={"topic": "Generative AI in Education"})
print(result)
```

---

## 🧠 What’s Happening Here

1. **The Researcher** searches for recent AI news.
2. **The Writer** turns the summary into a fun, readable blog post.
3. **The Editor** checks grammar, flow, and adds key takeaways.
4. They **work together automatically** — no extra prompts needed!

---

## 🪄 Optional: Streamlit Interface

You can also make a front-end for it:

```bash
streamlit run app.py
```

Then students can enter their topic (like *“AI in Healthcare”*) and watch the agents collaborate live.

---

## 🔍 Variations You Can Try

| Idea             | Description                                |
| ---------------- | ------------------------------------------ |
| 🧾 Research Bot  | Finds AI papers and writes summaries       |
| 🎓 Study Planner | Builds a daily learning schedule           |
| 💬 Chat Tutor    | Answers questions using a context document |
| 📊 Report Maker  | Reads PDFs and makes 1-page summaries      |
| 🖼️ Image Agent  | Uses Gemini Vision for multimodal analysis |

---

## 💬 Reflection Questions

Ask students:

* How is this different from a normal chatbot?
* Why do we give each agent a role and goal?
* How could this system be used in real life?

---

## 🌍 Real-World Uses of Agentic AI

| Field          | Example Use                                 |
| -------------- | ------------------------------------------- |
| 🌐 Business    | Customer service chatbots that take actions |
| 📚 Education   | Study planner bots or auto-grading agents   |
| 💻 Engineering | Debugging and code-review agents            |
| 📰 Media       | Automated research and report generation    |
| 🏥 Healthcare  | Symptom-checking and scheduling assistants  |

---

## 🏁 Wrap-Up — What You Learned

✨ AI models can now act like **agents**.
🧩 Agents can **plan, reason, and collaborate**.
💻 CrewAI helps us **build multi-agent systems** easily.
⚙️ Gemini makes each agent **intelligent and creative**.

> **Models create. Agents decide. Engineers connect them.**

Tomorrow, we’ll explore how to connect these agents to **real-world APIs and data** to make them truly autonomous. 🚀

---

## 📚 References & Resources

| Topic                       | Link                                                                                                     |
| :-------------------------- | :------------------------------------------------------------------------------------------------------- |
| CrewAI Docs                 | [https://docs.crewai.com](https://docs.crewai.com)                                                       |
| Gemini API                  | [https://ai.google.dev](https://ai.google.dev)                                                           |
| LangChain Hub               | [https://www.langchain.com](https://www.langchain.com)                                                   |
| Hugging Face Hub            | [https://huggingface.co/models](https://huggingface.co/models)                                           |
| Agents Intro (by LangChain) | [https://python.langchain.com/docs/use_cases/agents](https://python.langchain.com/docs/use_cases/agents) |

---

✅ **End of Day 3 — From Generators to Agents**
