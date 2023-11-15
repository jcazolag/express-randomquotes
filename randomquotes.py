from flask import Flask, jsonify
import os
import random

app = Flask(__name__)

phrases = [
    "1. Get ready to be inspired…", 
    "2. See rejection as redirection.",
    "3. There is beauty in simplicity.",
    "4. You can’t be late until you show up.",
    "5. Maybe life is testing you. Don’t give up.",
    "6. Impossible is just an opinion.",
    "7. Alone or not you gonna walk forward.",
]


@app.route('/')
def get_random_quote():
    phrase = random.choice(phrases)
    container_id = os.uname()[1]
    return f"{phrase} - Container Id: {container_id}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

