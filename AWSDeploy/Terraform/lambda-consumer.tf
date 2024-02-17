module "lambda_consumer_label" {
  source = "./modules/terraform-null-label"
  context = module.this.context
  stage       = "lambda"
}

module "lambda_consumer" {

  source = "./modules/lambda-consumer"
  context = module.lambda_billing_label.context
  log_retention_in_days = "14"

  s3_bucket_name        = ""
}