module "alb" {
  source = "./modules/terraform-aws-alb-1.11.1"

  context = module.this.context
  stage   = "alb"

  vpc_id                            = module.vpc.vpc_id
  subnet_ids                        = module.subnets.public_subnet_ids
  cross_zone_load_balancing_enabled = true

  access_logs_enabled         = false
  deletion_protection_enabled = false

  https_enabled = false
  http2_enabled = false
  http_redirect = false
  # certificate_arn  = data.aws_acm_certificate.default.arn
  # https_ssl_policy = "ELBSecurityPolicy-TLS13-1-3-2021-06"

  depends_on = [
    module.vpc
  ]
}
