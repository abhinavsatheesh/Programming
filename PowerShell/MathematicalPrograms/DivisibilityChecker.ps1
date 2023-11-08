[uint16] $num = Read-Host "Enter a number"
[uint16] $num2 = Read-Host "Enter another number by which we should check if" $num "is divisble"
If ($num % $num2 -eq 0) {
    Write-Host "Your number" $num "is divisible by" $num2
}
Else {
    Write-Host "Your number" $num "is not divisible by" $num2
}
 