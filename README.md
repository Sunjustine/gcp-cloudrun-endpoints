# gcp-cloudrun-endpoints
This test assignment is designed to evaluate my practical skills in cloud deployment, automation, and managing environments. I've created and deployed the endpoints using Google Cloud Run, and set up GitHub Actions to streamline deployment processes.

## General steps:
1. [Workflow: Deploy to Google Container Registry and Firestore Functions](#step1)
2. [Workflow 2: Add GCP Project as GitHub Environment](#step2)


### <a name='step1'></a>Workflow: Deploy to Google Container Registry and Firestore Functions
This workflow automates the process of building Docker images, pushing them to Google Container Registry (GCR), deploying Firestore Functions to Firebase, and deploying infrastructure using Terraform. It triggers on every push to the main branch.

**Prerequisites**
Navigate to **Settings > Secrets and variables > Actions** and add the following secrets:
- **Google Cloud Service Account Key:** Ensure that you have a service account key JSON file with the necessary permissions `roles/storage.admin` and `roles/cloudfunctions.admin`. This key should be added as a GitHub secret under the name **GCP_SA_KEY**.
- **Firebase CI Token:** Generate a Firebase token using firebase login:ci and store it as a GitHub secret under the name **FIREBASE_TOKEN**.
- **GCP Project ID:** Add your Google Cloud project ID as a GitHub secret under the name **GCP_PROJECT_ID**.
- **Firebase Project:** Set up Firebase in your Google Cloud project and ensure the Firestore database is enabled.

**Secrets**

- Navigate to **Settings > Secrets and variables > Actions**.
Add the following secrets:
- GCP_SA_KEY: Your base64-encoded Google Cloud service account key.
- FIREBASE_TOKEN: The Firebase CI token for deploying functions.
- **GCP_PROJECT_ID**: The ID of your Google Cloud project.

**How it works**
This workflow automates several tasks:

1. **Code Checkout:** The workflow starts by checking out the repository code.
2. **Set up Docker Buildx:** This step sets up Docker Buildx, a builder for multi-platform Docker builds.
3. **Log in to Google Container Registry (GCR):** Logs into GCR using the service account key stored in the GitHub secrets.
4. **Build and Push Docker Images:** The workflow builds Docker images for three different endpoints (Firestore, HTTPS, and Scheduler) and pushes them to GCR.
5. **Set up Node.js and Firebase CLI:** The workflow installs Node.js and Firebase CLI, which are required for deploying Firebase Functions.
6. **Deploy Firestore Function:** The workflow deploys the Firestore-triggered function using Firebase CLI from the specified directory.
7. **Set up and Deploy with Terraform:** The workflow initializes Terraform, make all necessary steps and links to the deployed endpoints on Google Cloud Run stored in `terraform/outputs.tf`


### <a name='step2'></a>Workflow: Add GCP Project as GitHub Environment
This workflow allows you to add a new Google Cloud Platform (GCP) project as a GitHub environment. It automates the creation of the environment in your GitHub repository and sets up the required secrets for deploying to Google Cloud.

**Prerequisites**
- **GitHub CLI:** This workflow uses the GitHub CLI to create environments in your repository.
- **GCP Service Account Key:** You need to provide a base64-encoded service account JSON key with permissions to manage Google Cloud resources (`roles/storage.admin`, `roles/cloudfunctions.admin`). You will input this directly when triggering the workflow.

**Setup Instructions**
*Prepare Your GCP Service Account Key*
1. Generate a service account JSON key from your Google Cloud project with appropriate permissions.
2. Encode the key as base64 (using base64 gcp-key.json).
3. Keep the encoded key ready for input when triggering the workflow.

*Trigger the Workflow*
1. Go to the **Actions** tab of your GitHub repository.
2. Select the workflow named **create-gcp-environment.yml**.
3. Click the *Run workflow* button, which will open a form.

*Provide the following inputs:*
- environment_name: The name of the new GitHub environment.
- gcp_project_id: Your Google Cloud Project ID.
- gcp_service_account_key: The base64-encoded service account key.

*Monitor the Workflow*
- After triggering the workflow, you can monitor its progress in the **Actions** tab.
- The workflow will create the new GitHub environment and set up the necessary secrets for GCP authentication.