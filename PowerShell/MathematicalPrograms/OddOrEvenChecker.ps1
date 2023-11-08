[uint16] $num = Read-Host "Enter a number"
If ($num%2 -eq 0) {
    Write-Host "Your number $num is even"
} 
Else {
    Write-Host "Your number $num is Odd"
}