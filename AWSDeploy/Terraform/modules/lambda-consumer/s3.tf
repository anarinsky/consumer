#module "mod_s3_label" {
#  source = "../terraform-null-label"
#
#  context = module.this.context
#
#  attributes = ["package"]
#}
#
#resource "aws_s3_bucket" "mod" {
#  count = local.store_on_s3 ? 1 : 0
#
#  bucket        = module.mod_s3_label.id
#  force_destroy = true
#
#  tags = module.mod_s3_label.tags
#}
#
#resource "aws_s3_bucket_ownership_controls" "mod" {
#  count = local.store_on_s3 ? 1 : 0
#
#  bucket = aws_s3_bucket.mod[0].id
#  rule {
#    object_ownership = "BucketOwnerPreferred"
#  }
#}
#
#resource "aws_s3_bucket_public_access_block" "mod" {
#  count = local.store_on_s3 ? 1 : 0
#
#  bucket = aws_s3_bucket.mod[0].id
#
#  block_public_acls       = true
#  block_public_policy     = true
#  ignore_public_acls      = true
#  restrict_public_buckets = true
#}
#
