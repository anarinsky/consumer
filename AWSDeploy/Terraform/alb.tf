module "alb" {
  source = "./modules/terraform-aws-alb-1.11.1"

  context = module.this.context
  stage   = "alb"

  vpc_id                            = module.vpc.vpc_id
  subnet_ids                        = module.subnets.public_subnet_ids
  cross_zone_load_balancing_enabled = true

  deletion_protection_enabled = true

  http2_enabled    = true
  http_redirect    = true
  https_enabled    = true
  certificate_arn  = data.aws_acm_certificate.default.arn
  https_ssl_policy = "ELBSecurityPolicy-TLS13-1-3-2021-06"
  # additional_certs = []
}