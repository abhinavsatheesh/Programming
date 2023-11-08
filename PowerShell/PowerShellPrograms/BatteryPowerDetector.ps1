$batteryPercentage = (Get-WmiObject win32_battery).estimatedChargeRemaining
$batteryPercentage = "Battery Percentage : $batteryPercentage%"
Write-Host $batteryPercentage