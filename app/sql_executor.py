# # app/sql_executor.py

# def execute_sql(query):
#     """
#     Dummy SQL executor.
#     Replace this with actual database interaction logic.
#     """
#     # For now, we just return a mock response based on the query
#     if query is None:
#         return "No SQL query generated"
#     return f"Simulated answer for query: {query}"

import matplotlib.pyplot as plt
import io
import base64

def generate_plot(df):
    plt.figure(figsize=(10, 5))
    df.plot(kind='bar', x=df.columns[0], y=df.columns[1])
    plt.tight_layout()
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    return "data:image/png;base64," + base64.b64encode(buffer.read()).decode()
