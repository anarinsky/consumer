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
data "aws_s3_bucket" "selected" {
  bucket = var.s3_bucket_name
}
