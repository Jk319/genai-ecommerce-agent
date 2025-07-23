import sqlite3
import pandas as pd
import os

DB_PATH = os.path.join("database", "ecommerce.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    ad = pd.read_csv("data/ad_sales.csv")
    total = pd.read_csv("data/total_sales.csv")
    eligible = pd.read_csv("data/eligibility.csv")
    ad.to_sql("AdSales", conn, if_exists="replace", index=False)
    total.to_sql("TotalSales", conn, if_exists="replace", index=False)
    eligible.to_sql("Eligibility", conn, if_exists="replace", index=False)
    conn.close()


def query_database(sql):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
    except Exception as e:
        result = f"Error: {e}"
    conn.close()
    return result
