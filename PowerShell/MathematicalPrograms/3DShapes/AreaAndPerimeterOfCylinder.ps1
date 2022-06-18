[double] $pi = [MATH]::PI
[double] $radius = Read-Host "Enter the Radius"
[double] $height = Read-Host "Enter the Height"
[double] $c = 2*$pi*$radius
[double] $a = $pi*$radius*$radius
[double] $tsa = 2*$pi*$radius*($radius + $height)
[double] $lsa = 2*$pi*$radius*$height
Write-Host "Perimeter of the Bottom Circle is $c cm"
Write-Host "Area of the Bottom Circle is $a sq.cm."
Write-Host "Total Surface Area of the Cylinder is $tsa sq.cm."
Write-Host "Lateral Surface Area of the Cylinder is $lsa sq.cm."
