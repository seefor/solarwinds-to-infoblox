# solarwinds-to-infoblox
Convert CSV exports from Solarwinds to Infoblox CSV import for Networks

## For Networks Only
Use the script in the network folder
You will need to export just the following fileds:
IP Address, Subnet Display Name, Subnet Address, Subnet CIDR,Subnet Mask

The script will loop though all the CSV files and output a file name "infoblox-import.out"
You will need to rename it to ".csv"
I've added some example exports from SolarWinds IPAM


## For Fixed Address
Use the script in the fix-address folder
You will need to export just the following fileds:
IP Address,MAC Address,Hostname,DHCP Client Name,System Name,Description,Contact,System Location,Vendor,Machine Type,Comments,Response Time,Last Boot Time,Last Synchronization,Status,System Object ID,Type,Skip Scan,Alias,Lease Expiration,Dual Stack IPv6 Address,Subnet Display Name,Subnet Address,Subnet CIDR,Subnet Mask

The script will loop though all the CSV files and output a file name "infoblox-fixed-address.out"
You will need to rename it to ".csv"
I've added some example exports from SolarWinds IPAM