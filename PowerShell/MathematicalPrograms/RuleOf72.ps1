[double] $principal = Read-Host "Enter the Principal Amount"
[double] $rate = Read-Host "Enter the Rate of Interest"
[double] $doublep = 2*$principal
[double] $rate72 = 72/$rate
Write-Host "Your Principal Amount Rs. $principal will become Rs. $doublep in $rate72 years"