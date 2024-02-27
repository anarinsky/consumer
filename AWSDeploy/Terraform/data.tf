/*
data "aws_acm_certificate" "default" {
  domain      = local.domain_name
  key_types   = ["RSA_2048"]
  types       = ["AMAZON_ISSUED"]
  statuses    = ["ISSUED"]
  most_recent = true
}
*/

data "aws_availability_zones" "available" {}
