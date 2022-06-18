[double] $num = Read-Host "Enter a number"
If ($num -gt 10 -or $num -lt 2) {
    Write-Host "This number is off limits. Try again."
}
Else {
    If ($num %2 -eq 0 -and $num -gt 2) {
        Write-Host "$num is not a Prime Number"
    }
    ElseIf ($num%3 -eq 0 -and $num -ne 3) {
        Write-Host "$num is a Prime Number"
    }
    Else {
        Write-Host "$num is a Prime Number"
    }
}