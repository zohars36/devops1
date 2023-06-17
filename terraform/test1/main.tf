terraform {
  required_providers {
    aws = {
        source = "hashicorp/aws"
        version = "~> 3.0"
    }
  }
}

provider "aws" {
  region = "eu-central-1"
}

resource "aws_instance" "zoharvm1" {
    ami = "ami-03aefa83246f44ef2"
    instance_type = "t2.micro"
  
}