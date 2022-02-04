<!-- Configuring a router as a dhcp server -->

<!-- If needed, exclude addresses in a range in global config mode -->
ip dhcp excluded-address *low address* *high address*

<!-- DHCP config -->
conf t
ip dhcp pool
network *network address* *mask*
domain-name *domain*
dns-server *address*
default-router *address*

