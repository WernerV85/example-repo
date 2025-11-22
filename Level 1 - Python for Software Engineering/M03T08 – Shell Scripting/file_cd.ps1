<# Shell scripting task 1:
Creating Folders and Sub-folder
Deleting folders#>

# Creating 3 folder

$menu = Read-Host "Select an option from blow list: `n1 - Create 3 folders `n2 - Create Sub-folders (3) `n3 - Delete folders `n Please select your option:"
while($menu -ne 4){
    if ($menu -eq 1){
        $folder1 = Read-Host "Please enter name for folder 1 "
        if(Test-Path -Path $folder1){
            Write-Host "Folder $folder1 already exits!"
        }
        else{
            New-Item -Path $folder1 -ItemType Directory
            Write-Host "Folder $folder1 created successfully!"
        }
        $folder2 = Read-Host "Please enter name for folder 2 "
        if(Test-Path -Path $folder2){
            Write-Host "Folder $folder2 already exits!"
        }
        else{
                New-Item -Path $folder2 -ItemType Directory
                Write-Host "Folder $folder2 created successfully!"
            }
        $folder3 = Read-Host "Please enter name for folder 3 "
        if(Test-Path -Path $folder3){
            Write-Host "Folder $folder3 already exits!"
        }
        else{
            New-Item -Path $folder3 -ItemType Directory
            Write-Host "Folder $folder3 created successfully!"
           }
        }
        break
        
    elseif ($menu -eq 2){
        $mainFolder = Read-Host "Please select the main folder to create Sub-Folders in"
        ls
        if(Test-Path -Path $mainFolder){
            $subFolder1 = Read-Host "Please enter name for Sub-folder 1 "
                if(Test-Path -Path $subFolder1){
                Write-Host "Sub-folder $subFolder1 already exits in $mainFolder!"
                }
                else{
                New-Item -Path "$mainFolder\$subFolder1" -ItemType Directory
                Write-Host "Sub-folder $subFolder1 created successfully in $mainFolder!"
                }
            $subFolder2 = Read-Host "Please enter name for Sub-folder 2 "
                if(Test-Path -Path $subFolder2){
                Write-Host "Sub-folder $subFolder2 already exits in $mainFolder!"
                }
                else{
                New-Item -Path "$mainFolder\$subFolder2" -ItemType Directory
                Write-Host "Sub-folder $subFolder2 created successfully in $mainFolder!"
                }
            $subFolder3 = Read-Host "Please enter name for Sub-folder 3 "
                if(Test-Path -Path $subFolder3){
                Write-Host "Sub-folder $subFolder3 already exits in $mainFolder!"
                }
                else{
                New-Item -Path "$mainFolder\$subFolder3" -ItemType Directory
                Write-Host "Sub-folder $subFolder3 created successfully in $mainFolder!"
                }
            }
        else{
            Write-Host "The folder $mainFolder does not exist!"
            }
        }
        break
    
    elseif ($menu -eq 3){
        $select_folder = Read-Host "Please select where you want to delete folder from `n1 - Main folders `n2 - Sub-Folders"
        if($select_folder -eq 1){
            $del_folder1 = Read-Host "Please enter the names of the folders you want to delete in the main directory "{
                if(Test-Path -Path $del_folder1){
                    Remove-Item -Path $del_folder1 -Recurse -Force
                    Write-Host "Folder $del_folder1 deleted successfully!"
                }
                else{
                    Write-Host "Folder $del_folder1 does not exist!"
                    }
                }
               $del_folder2 = Read-Host "Please enter the names of the folders you want to delete in the main directory "{
                if(Test-Path -Path $del_folder2){
                    Remove-Item -Path $del_folder2 -Recurse -Force
                    Write-Host "Folder $del_folder2 deleted successfully!"
                    }
                else{
                    Write-Host "Folder $del_folder2 does not exist!"
                    }
                }            
            }
        }
    else{
        Write-Host "Invalid option selected. Please try again."
            }
        break
    }
    
    $menu = Read-Host "Select an option from blow list: `n1 - Create 3 folders `n2 - Create Sub-folders (3) `n3 - Delete folders `n4 - Exit"

