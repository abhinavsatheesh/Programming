[double] $num = Read-Host "Enter a number"
If ($num -gt 0) {
    Write-Host "Your number $num is Positive"
}
ElseIf ($num -lt 0) {
    Write-Host "Your number $num is Negative"
}
ElseIf ($num -eq 0) {
    Write-Host "Your number 0 is neither Positive or Negative"
}