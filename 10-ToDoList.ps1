$list = '.\ToDoList.txt'
$todoArr = @()
$OFS = "`n"

function Get-List() {
  $text = Get-Content -Path $list
  $text = $text.split("`n")
  $out = @()
  for($i = 0;$i -lt $text.length; $i++) {
    $out += , $text[$i].split('|')
  }
  return $out
}

function Save-List() {
  $fileIn = ""
  foreach($line in $todoArr) {
    $fileIn += $line[0] + "|" + $line[1] +"`n"
  }
  $fileIn.Substring(0, $fileIn.Length - 1)
  Out-File -FilePath $list -InputObject $fileIn
}

function Remove-Done() {
  $out = @()
  foreach($line in $todoArr) {
    if($line[1] -ne "Done") { $out.Add($line) }
  }
  return $out
}

function Remove-Item($item) {
  $out = @()
  foreach($line in $todoArr) {
    if($line[0] -ne $item) { $out.Add($line) }
  }
  return $out
}

function Set-Done($item) {
  foreach($line in $todoArr) {
    if($line[0] -eq $item) { $line[1] = "Done" }
  }
}

function Test-Item($item, $list) {
  $valid = $false
  foreach($line in $list) { if($line[0] -eq $item) { $valid = $true } }
  return $valid
}

$todoArr = Get-List
$choice = Read-Host "What would you like to do?`n`n1.Add Item`n2.Remove Item`n3.Display Items`n4.Remove ALL Done Items`n5.Set Item As Done`n`n0. Exit"
switch ($choice) {
  1 {
    $add = Read-Host "What would you like to add?"
    $todoArr += , @($add, "Not")
  }
  2 { 
    $isValid = Test-Item ($item, $todoArr)
    if($isValid) { Remove-Item($item) }
  }
  3 {
    Write-Host $todoArr
  }
  4 {
    Remove-Done
  }
  5 {
    $isValid = Test-Item ($item, $todoArr)
    if($isValid) { Set-Done $item }
  }
}