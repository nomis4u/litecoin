provider "aws" {
  region  = var.region
  version = "~> 3.0"
}

#terraform {
#  required_version = "0.12.31"
#
#  backend "s3" {
#    bucket = "bucket_name"
#    key    = "path/to/terraform.tfstate"
#    region = var.region
#  }
#}

terraform {
  required_version = "0.12.31"
}
