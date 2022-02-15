$adminCreds = Get-Credential
$userId = ""

Enter-PSSession -ComputerName 'spodc2' -Credential $adminCreds

Get-ADUser -Identity $userId -LockedOut -False
