module "this" {
  source = "./modules/terraform-null-label"

  enabled     = true
  namespace   = var.project_main
  environment = var.environment
  tags = {
    Terraform = "true"
    owner     = "AlexN"
  }
}