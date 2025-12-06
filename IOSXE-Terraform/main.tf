#Terraform block defines the required provider and its version
terraform {
  required_providers {
    iosxe = {
      source  = "CiscoDevNet/iosxe"
      version = ">= 0.5.0"
    }
  }
}

#Provider blocker tells Terraform how to connect to the device
provider "iosxe" {
  host     = var.device_ip
  username = var.username
  password = var.password
}
