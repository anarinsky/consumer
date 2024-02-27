terraform {
  backend "s3" {
    bucket = "semcasting-terraform-state"
    key    = "terraform_consumer"
    region = "us-east-1"
  }

}