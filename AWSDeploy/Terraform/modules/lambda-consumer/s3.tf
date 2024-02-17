module "mod_s3_label" {
  source = "../terraform-null-label"

  context = module.this.context

  attributes = ["package"]
}

resource "aws_s3_bucket" "mod" {
  bucket        = module.mod_s3_label.id
  force_destroy = true

  tags = module.mod_s3_label.tags
}

resource "aws_s3_bucket_ownership_controls" "mod" {
  bucket = aws_s3_bucket.mod.id
  rule {
    object_ownership = "BucketOwnerPreferred"
  }
}

resource "aws_s3_bucket_public_access_block" "mod" {
  bucket = aws_s3_bucket.mod.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

