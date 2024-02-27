module "lambda_consumer_label" {
  source  = "./modules/terraform-null-label"
  context = module.this.context
  stage   = "lambda"
}

module "lambda_consumer" {
  source                = "./modules/lambda-consumer"
  context               = module.lambda_consumer_label.context
  log_retention_in_days = "14"

  s3_bucket_name = "alex-billing-semcasting-lambda-package"

  alb_hosts = [
    # "example.com",
  ]
  alb_priority = 100
  # alb_listener_arn = module.alb.https_listener_arn
  alb_listener_arn = module.alb.http_listener_arn
  vpc_id           = module.vpc.vpc_id

  depends_on = [
    module.vpc
  ]
}
