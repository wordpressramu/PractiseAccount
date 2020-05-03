Get-NetFirewallRule  | Select-Object  -Property Name,DisplayName,DisplayGroup,
@{Name='Protocol';Expression={($PSItem | Get-NetFirewallPortFilter).Protocol}},
@{Name='LocalPort';Expression={($PSItem | Get-NetFirewallPortFilter).LocalPort}},
@{Name='RemotePort';Expression={($PSItem | Get-NetFirewallPortFilter).RemotePort}},
@{Name='RemoteAddress';Expression={($PSItem | Get-NetFirewallAddressFilter).RemoteAddress}},
Enabled,
Profile,
Direction,
Action | ConvertTo-Html -Property Name, DisplayName, DisplayGroup,	Protocol,	LocalPort,	RemotePort,	RemoteAddress,	Enabled	,Profile,	Direction,	Action | Out-File -FilePath E:\PSDrives.html
