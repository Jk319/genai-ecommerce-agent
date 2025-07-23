
from flask import render_template, request
from app.llm import get_sql_query
from app.sql_executor import execute_sql, generate_plot

@app.route('/ask', methods=['POST'])
def ask_web():
    question = request.form['question']
    sql = get_sql_query(question)
    df = execute_sql(sql)

    should_plot = any(word in question.lower() for word in ["graph", "plot", "visual", "chart"])
    image = generate_plot(df) if should_plot else None

    return render_template("index.html", result=df.to_html(), image=image)


# from flask import Flask, render_template, request
# from app.llm import get_sql_query
# from app.sql_executor import execute_sql

# app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def home():
#     return render_template('index.html', answer=None, sql=None)

# @app.route('/ask', methods=['POST'])
# def ask_web():
#     try:
#         question = request.form['question']
#         sql = get_sql_query(question)
#         answer = execute_sql(sql)
#         return render_template('index.html', answer=answer, sql=sql)
#     except Exception as e:
#         return render_template('index.html', answer=f"Error: {e}", sql=None)



# # app/main.py

# from flask import Flask, request, jsonify, render_template
# from app.db import query_database
# from app.llm import get_sql_query
# from app.utils import format_response

# app = Flask(__name__)

# @app.route("/", methods=["GET"])
# def home():

#     return render_template("index.html", answer=None, sql=None)

# @app.route("/ask", methods=["POST"])
# def ask_web():
#     question = request.form.get("question")
#     sql = get_sql_query(question)
#     result = query_database(sql)
#     response = format_response(question, result)
#     return render_template("index.html", answer=response, sql=sql)
