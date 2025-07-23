# 🛍️ GenAI Ecommerce Agent

## Live WebLink - https://genai-ecommerce-agent.onrender.com

A lightweight AI-powered web app that answers questions about your e-commerce data using natural language (like: “What is my total sales?”). It uses **OpenAI GPT** (or Google Gemini) to generate SQL from plain English, executes the query, and returns results from CSV data.

---

## 🚀 Features

- Natural Language to SQL
- Works with CSV datasets (`ad_sales.csv`, `total_sales.csv`, `eligibility.csv`)
- Supports OpenAI or Gemini LLMs
- Built with Flask + HTML/CSS frontend

---

## 📂 Project Structure

├── run.py

├── requirements.txt

├── app/

│ ├── init.py

│ ├── db.py

│ ├── llm.py

│ ├── main.py

│ ├── sql_executor.py

│ ├── utils.py

│ ├── static/

│ │ └── style.css

│ └── templates/

│ └── index.html

├── data/

│ ├── ad_sales.csv

│ ├── eligibility.csv

│ └── total_sales.csv



---

## ⚙️ Setup (Local)

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/genai-ecommerce-agent.git
cd genai-ecommerce-agent
