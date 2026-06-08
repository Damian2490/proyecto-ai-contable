import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="ai_contable",
        user="postgres",
        password="damian90",
        host="localhost",
        port="5432"
    )