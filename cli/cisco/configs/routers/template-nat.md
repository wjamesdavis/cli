<!-- Configuring static NAT of inside source address -->

enable
configure terminal
ip nat inside source static *local-ip* *global-ip*
interface *type number*
ip address *ip-address mask* [secondary]
ip nat inside
exit
interface *type number*
ip address *ip-address mask* [secondary]
ip nat outside
end

<!-- Configuring dynamic NAT of inside source address -->

enable
configure terminal
ip nat pool *name* *start-ip* *end-ip* {netmask *netmask* | prefix-length *prefix-length*}
access-list *access-list-number* permit *source* [*source-wildcard*]
ip nat inside source list *access-list-number* pool *name*
interface *type number*
ip address *ip-address mask*
ip nat inside
exit
interface *type number*
ip address *ip-address mask*
ip nat outside
end

<!-- Using NAT to allow internal users access to the internet -->

enable
configure terminal
ip nat pool *name* *start-ip* *end-ip* {netmask *netmask* | prefix-length *prefix-length*}
access-list *access-list-number* permit source [*source-wildcard*]
ip nat inside source list *access-list-number* pool *name* overload
interface *type number*
ip address *ip-address mask*
ip nat inside
exit
interface *type number*
ip address *ip-address mask*
ip nat outside
end

<!-- Show commands -->

<!-- Display info about all ip address pools and NAT mappings configured -->
show ip nat statistics