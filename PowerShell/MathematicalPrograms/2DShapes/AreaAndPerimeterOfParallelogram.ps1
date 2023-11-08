[double] $Length = Read-Host "Enter the Length Measure"
[double] $Breadth = Read-Host "Enter the Breadth Measure"
[double] $area = $Length*$Breadth
[double] $p = 2*($Length+$Breadth)
Write-Host "Area of the Parallelogram is $area"
Write-Host "Perimeter of the Parallelogram is $p"
