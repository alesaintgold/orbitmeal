import json
import os
from flask import Flask, render_template

app = Flask(__name__)


def load_collection_data(filename):
    filepath = os.path.join(app.root_path, 'collections', filename)
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {filepath}")
        return None


@app.route('/')
def index():
    collection_data = load_collection_data('recipes.json')
    if collection_data:
        return render_template('index.html', data=collection_data)
    else:
        return "Failed to load collection data."


if __name__ == '__main__':
    app.run(debug=True)
