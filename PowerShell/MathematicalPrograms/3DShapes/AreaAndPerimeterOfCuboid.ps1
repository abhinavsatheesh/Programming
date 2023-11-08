[double] $length = Read-Host "Enter a Length Measure"
[double] $breadth = Read-Host "Enter a Breadth Measure"
[double] $height = Read-Host "Enter a Height Measure"
[double] $perimeter = 4*($length + $breadth + $height)
[double] $tsa = 2*(($length * $breadth) + ($length * $height) + ($breadth * $height))
[double] $lsa = 2*$height*($length + $breadth)
Write-Host "Perimeter of the Cuboid is $perimeter cm"
Write-Host "Total Surface Area of the Cuboid is $tsa sq.cm."
Write-Host "Lateral Surface Area of the Cuboid is $lsa sq.cm."