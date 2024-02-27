locals {
  private_subnet_ids = slice(module.subnets.private_subnet_ids, 0, var.max_subnet_count)
  public_subnet_ids  = slice(module.subnets.public_subnet_ids, 0, var.max_subnet_count)
}

module "vpc" {
  source = "./modules/terraform-aws-vpc-2.1.1"

  context = module.this.context
  stage   = "vpc"

  ipv4_primary_cidr_block = var.cidr
  ipv4_cidr_block_association_timeouts = {
    create = "3m"
    delete = "5m"
  }
}

module "subnets" {
  source = "./modules/terraform-aws-dynamic-subnets-2.4.1"

  context = module.this.context
  stage   = "subnet"

  availability_zones = data.aws_availability_zones.available.names

  max_subnet_count = max(var.max_subnet_count, 2)
  max_nats         = var.max_subnet_count

  vpc_id          = module.vpc.vpc_id
  igw_id          = [module.vpc.igw_id]
  ipv4_cidr_block = [module.vpc.vpc_cidr_block]

  nat_gateway_enabled  = false
  nat_instance_enabled = false
}
