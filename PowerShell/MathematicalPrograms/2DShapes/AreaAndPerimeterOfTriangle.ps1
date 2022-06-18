[double] $side1 = Read-Host "Enter the Length of Side 1"
[double] $side2 = Read-Host "Enter the Length of Side 2"
[double] $side3 = Read-Host "Enter the Length of Side 3"
[double] $perimeter = $side1 + $side2 + $side3
Write-Host "Perimeter of the Triangle is $perimeter cm"   
[double] $breadth = Read-Host "Enter the Breadth"
[double] $height = Read-Host "Enter the Height"
[double] $area = ($breadth * $height) / 2
Write-Host "Area of the Triangle is $area"