variable "project_id" {
  description = "The project ID to deploy the services."
}

variable "region" {
  description = "The region to deploy Cloud Run services."
  default     = "us-central1"
}

variable "image_tag" {
  description = "The image tag to use for the Docker images."
  default     = "latest"
}
