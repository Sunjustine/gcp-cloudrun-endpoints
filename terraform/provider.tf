provider "google" {
  project = var.project_id
  region  = var.region
  credentials = file(env.GOOGLE_APPLICATION_CREDENTIALS)
}


