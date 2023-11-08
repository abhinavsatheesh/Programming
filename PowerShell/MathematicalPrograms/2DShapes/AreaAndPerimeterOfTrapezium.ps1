[double] $side1 = Read-Host "Enter the Length of Side 1"
[double] $side2 = Read-Host "Enter the Length of Side 2"
[double] $side3 = Read-Host "Enter the Length of Side 3"
[double] $side4 = Read-Host "Enter the Length of Side 4"
[double] $perimeter = $side1 + $side2 + $side3 + $side4
Write-Host "Perimeter of the Trapezium is $perimeter"
[double] $base_1 = Read-Host "Enter the Length of Base 1"
[double] $base_2 = Read-Host "Enter the Length of Base 2"
[double] $height = Read-Host "Enter the Height"
[double] $area = ($base_1 + $base_2) * $height / 2
Write-Host "Area of the Trapezium is $area sq.cm"
