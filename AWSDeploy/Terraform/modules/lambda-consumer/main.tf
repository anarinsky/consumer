locals {
  store_on_s3 = false
}

module "mod" {
  source = "../terraform-aws-lambda"

  function_name = module.this.id
  description   = "Billing Lambda Function"
  timeout       = var.timeout
  handler       = "app.lambda_handler"
  runtime       = "python3.10"
  memory_size   = "128"

  build_in_docker  = true
  docker_pip_cache = true

#  environment_variables = {
#    S3_BUCKET_NAME = data.aws_s3_bucket.selected.bucket
#  }

  docker_additional_options = [
    "--platform", "linux/amd64",
  ]

  source_path = [{
    path             = "${path.module}/../../../../server/src"
    pip_requirements = true
  }]

#  allowed_triggers = {
#    elasticloadbalancing = {
#      principal  = "elasticloadbalancing.amazonaws.com"
#      source_arn = module.ingress.target_group_arn
#    }
#  }
  store_on_s3 = local.store_on_s3
#  s3_bucket   = local.store_on_s3 ? aws_s3_bucket.mod[0].bucket : null

  #vpc_subnet_ids         = var.vpc_subnet_ids
  #vpc_security_group_ids = [
  #  module.sg.id,
  #]

  cloudwatch_logs_retention_in_days         = var.log_retention_in_days
  create_unqualified_alias_allowed_triggers = true
  create_current_version_allowed_triggers   = false

  attach_policy_json = false
  #policy_json        = data.aws_iam_policy_document.policy.json

  tags = module.this.tags

#  depends_on = [
#    aws_s3_bucket.mod,
#  ]
}

#data "aws_iam_policy_document" "policy" {
#  statement {
#    effect = "Allow"
#    actions = [
#      "s3:*",
#    ]
#    resources = ["*"]
##    resources = [
##      format("%s/*", data.aws_s3_bucket.selected.arn),
##    ]
#  }
#}

#resource "aws_lb_target_group_attachment" "mod" {
#  target_group_arn = module.ingress.target_group_arn
#  target_id        = module.mod.lambda_function_arn
#
#  depends_on = [
#    module.mod,
#    module.ingress,
#  ]
#}
