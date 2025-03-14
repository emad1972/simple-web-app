from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# Connect to PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        database="testdb",
        user="postgres",
        password="password",
        host="db", # Docker service name
        port="5432"
    )
    return conn

@app.route('/')
def home():
    return jsonify({"message": "Hello from Flask API!"})

@app.route('/data')
def data():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users;')
    users = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 

