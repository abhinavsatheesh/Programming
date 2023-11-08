[double] $num1 = Read-Host "Enter a number"
[double] $sq = [Math]::Pow($num1, 2)
[double] $num2 = Read-Host "Enter another number"
[double] $cube = [Math]::Pow($num2, 3)
[double] $num3 = Read-Host "Enter another number"
[double] $roots = [Math]::Sqrt($num3)
[double] $num4 = Read-Host "Enter another number"
[double] $x = [Math]::Pow($num4, 1/3)
Write-Host "The square of $num1 is $sq"
Write-Host "The cube of $num2 is $cube"
Write-Host "The square root of $num3 is $roots"
Write-Host "The cube root of $num4 is $x"