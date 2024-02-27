module "ingress" {
  source = "../terraform-aws-alb-ingress-0.28.0"

  context = module.this.context

  unauthenticated_priority      = var.alb_priority
  health_check_enabled          = false
  target_type                   = "lambda"
  vpc_id                        = var.vpc_id
  unauthenticated_hosts         = var.alb_hosts
  unauthenticated_listener_arns = [var.alb_listener_arn]
  unauthenticated_paths         = ["/*"]
}
