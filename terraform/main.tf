resource "google_project_service" "cloud_run" {
  project = var.project_id
  service = "run.googleapis.com"
}


resource "google_cloud_run_service" "https_trigger" {
  name     = "https-trigger-service"
  location = var.region

  template {
    spec {
      containers {
        image = "gcr.io/${var.project_id}/https-trigger:${var.image_tag}"
        ports {
          container_port = 8080
        }
      }
    }
  }
}

resource "google_cloud_run_service" "firestore_trigger" {
  name     = "firestore-trigger-service"
  location = var.region

  template {
    spec {
      containers {
        image = "gcr.io/${var.project_id}/firestone-trigger:${var.image_tag}"
        ports {
          container_port = 8080
        }
      }
    }
  }
}

resource "google_cloud_run_service" "scheduler_trigger" {
  name     = "scheduler-trigger-service"
  location = var.region

  template {
    spec {
      containers {
        image = "gcr.io/${var.project_id}/scheduler-trigger:${var.image_tag}"
        ports {
          container_port = 8080
        }
      }
    }
  }
}