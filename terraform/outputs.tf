output "https_trigger_url" {
  value = google_cloud_run_service.https_trigger.status[0].url
}

output "firestore_trigger_url" {
  value = google_cloud_run_service.firestore_trigger.status[0].url
}

output "scheduler_trigger_url" {
  value = google_cloud_run_service.scheduler_trigger.status[0].url
}