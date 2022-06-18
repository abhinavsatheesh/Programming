[double] $pi = [math]::pi
[double] $r = Read-Host "Enter the Radius"
[double] $area = $pi * $r * $r
[double] $c = 2*$pi*$r
Write-Host "Area = $area"
Write-Host "Perimeter = $c"
 