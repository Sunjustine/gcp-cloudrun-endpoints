# You need to create scheduler job that triggers the Cloud Run service
# to test that all works properly. There is the example bellow:
#
#
# gcloud scheduler jobs create http my-scheduler-job \
#   --schedule "*/5 * * * *" \
#   --http-method POST \
#   --uri https://[YOUR_CLOUD_RUN_URL] \
#   --message-body '{"message": "Hello from Cloud Scheduler!"}' \
#   --time-zone "America/Los_Angeles"


from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def scheduler_trigger():
    # Print out the details of the Cloud Scheduler job
    scheduler_details = request.get_json()
    print(f"Scheduler Triggered with details: {scheduler_details}")
    return "Job received", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
