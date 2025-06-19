from flask import Flask, request, jsonify
from ai_suggestions import suggest_schedule

app = Flask(__name__)

@app.route('/')
def hello():
    return "Backend is running!"

@app.route('/suggest', methods=['POST'])
def suggest():
    data = request.get_json()
    event_type = data.get('event_type', '')
    schedule = suggest_schedule(event_type)
    return jsonify({'schedule': schedule})

if __name__ == '__main__':
    app.run(debug=True)
