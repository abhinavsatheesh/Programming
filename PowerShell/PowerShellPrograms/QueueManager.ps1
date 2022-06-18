$name = Read-Host "Enter the Name of the person"
$age = Read-Host "Enter the Age of the person"
$mobileno = Read-Host "Enter the Mobile Number of the person"
$emailid = Read-Host "Enter the Email ID of the Person"
$address = Read-Host "Enter the Address of the person"
Out-File "$name.txt"
Add-Content "$name.txt" "Name: $name`nAge: $age`nMobile Number: $mobileno`nEmail ID: $emailid`nAddress: $address"
cd ..
Write-Host "Details saved successfully"


