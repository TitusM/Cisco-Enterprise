variable "device_ip" {
  description = "The IP address of the Cisco device."
  type        = string
}

variable "username" {
  description = "The username for device authentication."
  type        = string
}

variable "password" {
  description = "The password for device authentication."
  type        = string
  sensitive   = true
}

variable "vlan_id" {
  description = "VLAN ID to be created on the device."
  type        = number

  validation {
    condition     = var.vlan_id > 0 && var.vlan_id < 4095 && !(var.vlan_id >= 1002 && var.vlan_id <= 1005)
    error_message = "VLAN ID must be between 1 and 4094, excluding 1002-1005."
  }
}

variable "vlan_name" {
  description = "Name of the VLAN to be created."
  type        = string
}

variable "vlan_shutdown" {
  description = "Indicates whether the VLAN should be shutdown."
  type        = bool
  default     = false
}

variable "vlans_map" {
  description = "Map of VLANs to be created on the device."
  type = map(object({
    id       = number
    name     = string
    shutdown = bool
  }))

  validation {
    condition     = length(var.vlans_map) > 0
    error_message = "The vlans_map variable must contain at least one VLAN definition."
  }
}