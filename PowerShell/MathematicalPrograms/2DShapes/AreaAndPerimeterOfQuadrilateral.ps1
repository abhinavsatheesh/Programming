[double] $side1 = Read-Host "Enter the Length of 1st Side"
[double] $side2 = Read-Host "Enter the Length of 2nd Side"
[double] $side3 = Read-Host "Enter the Length of 3rd Side"
[double] $side4 = Read-Host "Enter the Length of 4th Side"
[double] $perimeter = $side1 + $side2 + $side3 + $side4
Write-Host "Perimeter of the Quadrilateral is $perimeter"
[double] $diagonal = Read-Host "Enter the Length of Diagonal"
[double] $height1 = Read-Host "Enter the 1st Altitude"
[double] $height2 = Read-Host "Enter the 2nd Altitude"
[double] $area = ($diagonal / 2) * ($height1 + $height2)
Write-Host "Area of the Quadrilateral is $area"
