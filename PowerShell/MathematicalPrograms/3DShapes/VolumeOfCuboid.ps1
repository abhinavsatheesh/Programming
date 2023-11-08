$option = Read-Host "Do you wish to find the Volume of Cuboid by 2D Method or via 3D Method? Please enter either 2D or 3D"
if ($option -eq "2D") {
    Write-Host "Ok"
    [double] $ba = Read-Host "Enter the Base Area of the Cuboid"
    [double] $height = Read-Host "Enter a Height Measure"
    [double] $volume = $ba*$height
    Write-Host "Volume of the Cuboid is $volume"
}
elseif ($option -eq "3D") {
    Write-Host "Ok"
    [double] $length = Read-Host "Enter the Length of the Cuboid"
    [double] $breadth = Read-Host "Enter the Breadth of the Cuboid"
    [double] $height = Read-Host "Enter the Height of the Cuboid"
    [double] $volume = $length*$breadth*$height
    Write-Host "Volume of the Cuboid is $volume"
}
else {
    Write-Host "That's an invalid option. Try again later"
    [Environment]::Exit(1)
}