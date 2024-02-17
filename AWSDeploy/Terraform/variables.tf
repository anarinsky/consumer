variable "AWS_REGION" {
  default = "us-east-1"
}

variable "environment"  {
  default = "prod"
}
variable "project_main" {
  default = "consumer-report"
}
variable "cidr" {
  default = "10.10.0.0/16"
}
variable "max_subnet_count" {
  default = 2
}

