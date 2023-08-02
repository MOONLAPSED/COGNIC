from flask import Flask, request, jsonify
from repl_server import execute_code
from error_handling import handle_error

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute():
    code_snippet = request.json.get('code', '')
    try:
        result = execute_code(code_snippet)
        return jsonify({'output': result, 'error': None})
    except Exception as e:
        error_message = handle_error(e)
        return jsonify({'output': None, 'error': error_message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)