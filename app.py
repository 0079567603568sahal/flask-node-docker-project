from flask import Flask, request, jsonify
import os
import psycopg2

app = Flask(__name__)

# Root route
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Backend is running!"})

# API data route
@app.route("/api/data", methods=["GET"])
def get_data():
    return jsonify({"message": "Backend is working", "status": "success"})

# Submit data route
@app.route("/submit", methods=["POST"])
def submit_form():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    return jsonify({"message": f"Received {name} with email {email}"})

# Database health check
@app.route("/db-check", methods=["GET"])
def db_check():
    try:
        conn = psycopg2.connect(
            host="db",  # Docker service name
            database=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            port=5432
        )
        cur = conn.cursor()
        cur.execute("SELECT version();")
        db_version = cur.fetchone()[0]
        cur.close()
        conn.close()
        return jsonify({"db_version": db_version})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
