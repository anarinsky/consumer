variable "log_retention_in_days" {
  description = "The number of days to retain logs for the Lambda function."
}

variable "timeout" {
  default     = 900
  description = "The amount of time the Lambda function has to run in seconds."
}

variable "maximum_concurrency" {
  description = "The maximum number of instances for the Lambda function."
  default     = 100
}

variable "s3_bucket_name" {}

variable "alb_hosts" {
  default = []
}
variable "alb_listener_arn" {}
variable "alb_priority" {}
variable "vpc_id" {}
