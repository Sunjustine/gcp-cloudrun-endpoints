provider "google" {
  project = var.project_id
  region  = var.region
  credentials = file("/mnt/data/devops/gcp-cloudrun-endpoints/terraform/gcp-cloudrun-endpoints-project-594f7791f9cb.json")
}


