from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def firestore_trigger():
    event_data = request.get_json()

    if not event_data:
        return jsonify({'error': 'No event data received'}), 400

    return jsonify({
        'status': 'success',
        'event': event_data
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
