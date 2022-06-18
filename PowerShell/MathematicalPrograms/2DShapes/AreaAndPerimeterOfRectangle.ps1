[double] $Length = Read-Host "Enter the Length Measure"
[double] $Breadth = Read-Host "Enter the Breadth Measure"
[double] $area = $Length*$Breadth
[double] $perimeter = 2*($Length+$Breadth)
Write-Host "Perimeter = $perimeter"
Write-Host "Area = $area"
