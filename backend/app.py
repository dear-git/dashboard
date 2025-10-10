
from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2
import os

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="your_database",
        user="your_username",
        password="your_password"
    )
    return conn

@app.route('/api/bms')
def get_bms_data():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM bms;')
        bms_data = cur.fetchall()
        cur.close()
        conn.close()

        # Convert data to a list of dictionaries
        columns = [desc[0] for desc in cur.description]
        data = [dict(zip(columns, row)) for row in bms_data]

        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/db-viewer')
def db_viewer():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM bms;')
        bms_data = cur.fetchall()
        cur.close()
        conn.close()

        # Get column names from cursor description
        columns = [desc[0] for desc in cur.description]

        # Generate HTML table
        html = '<html><head><title>BMS Data</title>'
        html += '<style>body{font-family: sans-serif; background-color: #f4f4f9; color: #333;} table{width: 100%; border-collapse: collapse; margin: 20px 0;} th, td{border: 1px solid #ddd; padding: 8px; text-align: left;} th{background-color: #4CAF50; color: white;}</style>'
        html += '</head><body>'
        html += '<h1>BMS Data</h1>'
        html += '<table>'
        html += '<tr>'
        for col in columns:
            html += f'<th>{col}</th>'
        html += '</tr>'

        for row in bms_data:
            html += '<tr>'
            for item in row:
                html += f'<td>{item}</td>'
            html += '</tr>'

        html += '</table>'
        html += '</body></html>'

        return html
    except Exception as e:
        return f"An error occurred: {e}"


if __name__ == '__main__':
    app.run(debug=True, port=5001)
