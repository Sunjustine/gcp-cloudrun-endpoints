from flask import Flask, request

app = Flask(__name__)

@app.route('/scheduler-trigger', methods=['POST'])
def scheduler_trigger():
    # Print out the details of the Cloud Scheduler job
    scheduler_details = request.get_json()
    print(f"Scheduler Triggered with details: {scheduler_details}")
    return "Job received", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
