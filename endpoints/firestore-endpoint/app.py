from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_firestore_event():
    try:
        event_data = request.json
        print("Received Firestore event data:")
        print(event_data)

        # Process the event data as needed
        if event_data.get('after'):
            print("Document was created or updated:", event_data['after'])
        if event_data.get('before') and not event_data.get('after'):
            print("Document was deleted:", event_data['before'])

        return jsonify({"message": "Event data received successfully"}), 200
    except Exception as e:
        print(f"Error handling Firestore event: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
