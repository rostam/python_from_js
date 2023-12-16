from flask import Flask, request, jsonify, render_template
import sys
from io import StringIO
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/run_python', methods=['POST'])
def run_python():
    data = request.get_json()
    code = data['code']

    # Capture the output of the code execution
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    try:
        exec(code)
        result = redirected_output.getvalue()
    except Exception as e:
        result = str(e)
    finally:
        sys.stdout = old_stdout

    return jsonify({'output': result})


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
