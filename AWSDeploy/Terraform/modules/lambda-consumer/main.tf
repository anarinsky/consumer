module "mod" {
  source = "../terraform-aws-lambda"

  function_name = module.this.id
  description   = "Billing Lambda Function"
  timeout       = var.timeout
  handler       = "lambda_handler.lambda_handler"
  runtime       = "python3.12"
  memory_size   = "256"

  build_in_docker  = true
  docker_pip_cache = true

  docker_additional_options = [
    "--platform", "linux/amd64",
  ]

  source_path = [{
    path             = "${path.module}/files"
    pip_requirements = true
  }]

  store_on_s3 = true
  s3_bucket   = aws_s3_bucket.mod.bucket

  cloudwatch_logs_retention_in_days         = var.log_retention_in_days
  create_unqualified_alias_allowed_triggers = true
  create_current_version_allowed_triggers   = false

  attach_policy_json = true
  policy_json        = data.aws_iam_policy_document.policy.json

  tags = module.this.tags

  depends_on = [
    aws_s3_bucket.mod,
  ]
}

data "aws_iam_policy_document" "policy" {
  # SQS
  statement {
    effect = "Allow"
    actions = [
      "s3:*",
    ]
    resources = [
      format("%s/*", data.aws_s3_bucket.selected.arn),
    ]
  }
}
