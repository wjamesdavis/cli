<!-- Configure Standard ACLs -->

access-list *access-list-number* {permit|deny} {*host*|*source* *source-wildcard*|any}

<!-- After the ACL is defined, it must be applied to the interface (inbound or outbound) -->

interface <interface>
ip access-group number {in|out}

<!-- Configure extended ACLs -->

access-list access-list-number 
     [dynamic *dynamic-name* [timeout minutes]] 
     {deny|permit} *protocol* *source* *source-wildcard* *destination* *destination-wildcard* [precedence *precedence*] 
     [tos *tos*] [log|log-input] [time-range *time-range-name*]