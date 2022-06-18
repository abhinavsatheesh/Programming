[double] $pi = [MATH]::PI
[double] $radius = Read-Host "Enter the Radius"
[double] $height = Read-Host "Enter the Height"
[double] $volume = $pi*$radius*$radius*$height
Write-Host "Volume of the Cylinder is $volume"