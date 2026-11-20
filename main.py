# Application entry point. Run this file to start the web server

from backend import app

if __name__ == "__main__":
    # Open http://127.0.0.1:5000 after starting the server
    # Debug mode is intended for local development only
    app.run(host="127.0.0.1", port=5000, debug=True)