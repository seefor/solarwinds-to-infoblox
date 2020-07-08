# solarwinds-to-infoblox
Convert CSV exports from Solarwinds to Infoblox CSV import for Networks

## For Networks Only
You will need to export just the following fileds:
IP Address, Subnet Display Name, Subnet Address, Subnet CIDR,Subnet Mask

The script will loop though all the CSV files and output a file name "infoblox-import.csv"
