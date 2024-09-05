from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    request_data = {
        "method": request.method,
        "headers": dict(request.headers),
        "args": request.args.to_dict(),
        "form_data": request.form.to_dict(),
    }

    # Attempt to load JSON data if Content-Type is application/json
    if request.content_type == 'application/json':
        try:
            request_data["json"] = request.get_json()
        except Exception as e:
            request_data["json_error"] = str(e)
    else:
        request_data["json"] = None

    return jsonify(request_data), 200

@app.route('/hello', methods=['GET'])
def say_hello():
    return "<p>Hello world!</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
