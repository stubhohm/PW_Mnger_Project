from flask import Flask
from pw_manager import main

app = Flask(__name__)
@app.route('/')

def index():
    main()

if __name__ == '__main__':
    app.run(debug=True)