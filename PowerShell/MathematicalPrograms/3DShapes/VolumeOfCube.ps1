$choice = Read-Host "Do you wish to find the Volume of Cube by 2D Method or via Side Method? Please enter either 2D or Side"
if ($choice -eq "2D") {
    Write-Host "Ok"
    [double] $ba = Read-Host "Enter the Base Area of the Cube"
    [double] $height = Read-Host "Enter a Height Measure"
    [double] $volume = $ba*$height
    Write-Host "Volume of the Cube is $volume"
}
elseif ($choice -eq "Side") {
    Write-Host "Ok"
    [double] $side = Read-Host "Enter the Side of the Cube"
    [double] $volume = [MATH]::Pow($side, 3)
    Write-Host "Volume of the Cube is $volume"
}
else {
    Write-Host "That's an invalid option. Try again later"
    [Environment]::Exit(1)
}