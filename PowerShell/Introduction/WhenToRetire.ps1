$name = Read-Host "Enter your Name"
[uint16]$age = Read-Host -Prompt 'Enter your Age'
$profession = Read-Host "Enter your Profession"
[uint16]$retiringage = Read-Host -Prompt "Enter your Retiring Age"
[uint16]$yearsleft = $retiringage-$age
Write-Host "Hello" $name". Your age is" $age". You will have to retire from" $profession" in "$yearsleft "years."