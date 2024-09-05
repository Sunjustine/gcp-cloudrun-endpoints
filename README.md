Test Assignment: Junior DevOps Engineer
Objective: This test assignment is designed to evaluate your practical skills in cloud deployment, automation, and managing environments. You will create and deploy endpoints using Google Cloud Run, and set up GitHub Actions to streamline deployment processes.

Task Overview:

1. Create and Deploy Endpoints to Google Cloud Run. Deploy must be via terraform

a) HTTPS Trigger:

Write an endpoint that is triggered via HTTPS.
When triggered, print the details of the HTTPS request.
b) Firestore Trigger:

Write an endpoint that is triggered by changes in a Firestore collection.
When triggered, print the details of the Firestore event.
c) Scheduler Trigger:

Write an endpoint that is triggered by Google Cloud Scheduler.
When triggered, print the details of the scheduled job.
Requirements:

Deploy these endpoints to Google Cloud Run.
Ensure that each endpoint correctly handles its respective trigger and logs the trigger details.
2. Create a GitHub Action for Deployment to Google Container Registry (GCR):

Write a GitHub Action that automates the deployment of code to Google Container Registry.
Ensure that the action is easy to use, with clear documentation and minimal input parameters.
The action should handle building, tagging, and pushing the Docker image to GCR.
3. Create a GitHub Action to Add a New GCP Project as a GitHub Environment:

Write a GitHub Action that facilitates the addition of a new GCP project as a GitHub environment.
The action should prompt for minimal input, such as the environment's name and project ID.
Upon execution, this action should:
Create a new GitHub environment with the specified name.
Define and set the necessary GitHub secrets/variables for deploying to Google Cloud Run.
Allow future deployments to the new GCP project using the action from Task 2.
Considerations:

Minimize the number of input parameters required for each GitHub Action.
Ensure both actions are user-friendly, with clear and concise instructions.
For the second GitHub Action, ensure that all necessary secrets/variables are set up automatically to enable seamless deployment to the new environment.

Deliverables:

Links to the deployed endpoints on Google Cloud Run.
GitHub repository with:
The code for the endpoints.
The two GitHub Actions with instructions on how to use them.
