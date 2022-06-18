[System.Collections.ArrayList] $AbhinavList = "Python", "C++", "JavaScript", "HTML", "CSS"
Write-Host "Hi. Your list is $AbhinavList"
Write-Host "Removing C++"
$AbhinavList.Remove("C++")
Write-Host "Updated List is $AbhinavList"
Write-Host "Adding Java"
$AbhinavList.Add("Java")
Write-Host "Updated List is $AbhinavList"

