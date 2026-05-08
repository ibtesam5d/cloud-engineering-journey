#git command used

git status #to check the status of git, if there is any un-staged file, non-commited

git log --oneline #this shows all the commits in one simple line

git checkout -b #to create a new bramch

git merge <branch name> #to merge onto the current branch

#basic commands

##git add
git add --all/-A #adds all files and folders in the project directory to be staged

git add . #adds all files and folders in the current working directory only

git add \* #adds everything but the deleted files/folders to be staged

git add \*.txt #adds all the .txt file to be staged excluding thge deleted ones

##git remove
git rm <filename> #deletes the fileand also stages sos no need to run add

git reset --hard #brings back the deleted files and folders

git rm --cached <filename> #only removes the file from the staging

git rm -r <folder> #recursive deletion, includes all the subfolders and contents

##git branch
git branch <branch_name> #creates a new branch

git checkout -b <branch_name> #creates a new branch and moves to it

git merge <branch_name> #merges the branch to the current one

##version control
git checkout <commit_id> #moves to a previously commited version with commit ID.

git restore <filename/folder/.> #discards changes to a specific file/folder or . for discarding all uncommitted changes in the current directory or subdirectory to their last staged or commited state

git restore --staged ./filename #unstages everything in the current directory
