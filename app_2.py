import os
from app import create_app

app = create_app()

if __name__ == '__main__':
    print("Flask app is running")
    app.run(host='127.0.0.1',port=5000, debug=True)
