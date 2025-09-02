import os
import psycopg2
from flask import Flask

app = Flask(__name__)

def get_db_connection():
    """Establishes a connection to the database."""
    try:
        conn = psycopg2.connect(
            host=os.environ.get('DB_HOST'),
            database=os.environ.get('DB_NAME'),
            user=os.environ.get('DB_USER'),
            password=os.environ.get('DB_PASS')
        )
        return conn
    except Exception as e:
        # Return the exception to be displayed on the webpage
        return e

@app.route('/')
def index():
    """Main route to check database connection status."""
    conn_or_error = get_db_connection()
    
    # Check if the connection function returned a connection object or an error
    if isinstance(conn_or_error, Exception):
        # We got an error
        return f"<h1>Connection Failed</h1><p>{conn_or_error}</p>"
    else:
        # We got a connection
        conn_or_error.close()
        return "<h1>Connection Successful!</h1><p>Successfully connected to the PostgreSQL database.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
