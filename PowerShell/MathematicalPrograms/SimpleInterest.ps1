[uint16] $principal = Read-Host "Enter the Principal Amount"
[uint16] $rate = Read-Host "Enter the Rate of Interest"
[uint16] $time = Read-Host "Enter the Time in Years"
[uint16] $si = ($principal*$rate*$time)/100
[uint16] $amount = $si+$principal
Write-Host "Simple Interest = ₹ "$si
Write-Host "Amount = ₹ "$amount
