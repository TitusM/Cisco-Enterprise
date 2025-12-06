#The actual infrastructure resource to be created on the device
resource "iosxe_vlan" "devices" {
  vlan_id  = 30
  name     = "Terraform_VLAN30"
  shutdown = false
}

#Define VLAN using variables from variables.tf
resource "iosxe_vlan" "vlan_from_vars" {
  vlan_id  = var.vlan_id
  name     = var.vlan_name
  shutdown = var.vlan_shutdown
}

#Define another VLAN - Variables using Maps
resource  "iosxe_vlan" "vlans_from_map" {
  for_each = var.vlans_map
   vlan_id  = each.value.id
   name     = each.value.name
   shutdown = each.value.shutdown
}