
# app/llm.py

def get_sql_query(question):
    """
    Simulates the LLM output by returning a dummy SQL query based on the input question.
    """
    dummy_mapping = {
        "what is my total sales": "SELECT SUM(sales) FROM orders;",
        "top 5 products": "SELECT product_name FROM products ORDER BY sales DESC LIMIT 5;",
        "how many customers": "SELECT COUNT(*) FROM customers;",
        "average order value": "SELECT AVG(order_value) FROM orders;",
        "most active customer": "SELECT customer_id FROM orders GROUP BY customer_id ORDER BY COUNT(*) DESC LIMIT 1;"
    }

    # Normalize and match input
    question_lower = question.strip().lower()

    for key in dummy_mapping:
        if key in question_lower:
            return dummy_mapping[key]

    # Default fallback
    return "SELECT 'No matching dummy SQL found';"


# from flask import Flask, request, jsonify, render_template
# def get_sql_query(question):
#     # Your model logic (OpenAI or Gemini) goes here
#     ...

# from app.db import query_database
# from app.utils import format_response

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/ask", methods=["POST"])
# def ask_web():
#     question = request.form["question"]
#     sql = get_sql_query(question)
#     result = query_database(sql)
#     answer = format_response(question, result)
#     return render_template("index.html", sql=sql, answer=answer)

# @app.route("/api/ask", methods=["POST"])
# def ask_api():
#     question = request.json.get("question")
#     sql = get_sql_query(question)
#     result = query_database(sql)
#     response = format_response(question, result)
#     return jsonify({"question": question, "sql": sql, "answer": response})



# # app/llm.py
# import os
# import google.generativeai as genai
# from dotenv import load_dotenv

# load_dotenv()
# print("Gemini API Key:", os.getenv("GEMINI_API_KEY"))  

# model = genai.GenerativeModel("gemini-1.5-pro")

# def get_sql_query(question):
#     prompt = f"""
# You are a SQL expert. The following tables exist:

# 1. AdSales(product_id, ad_spend, clicks, impressions)
# 2. TotalSales(product_id, total_sales, units_sold)
# 3. Eligibility(product_id, is_eligible)

# Convert the question to an SQL query.

# Question: {question}
# SQL:"""

#     response = model.generate_content(prompt)
#     return response.text.strip()
