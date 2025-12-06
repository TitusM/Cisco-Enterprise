#Create a Loopback Interface with IP Address
resource "iosxe_interface_loopback" "loopback" {
  name       = 1
  ipv4_address = "1.1.1.1"
  ipv4_address_mask       = "255.255.255.255"
}

