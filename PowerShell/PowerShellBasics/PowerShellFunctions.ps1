function GetNameJob {
    param (
        [string[]] $name,
        [string[]] $job
    )
    Write-Host "Hello $name. Your job is $job"
}
$nameper = Read-Host "May I know your name?"
$jobper = Read-Host "May I know your job?"
GetNameJob -name $nameper -job $jobper