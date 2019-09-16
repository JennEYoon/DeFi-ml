# Guide for editing Github History after the fact.   

Source:  https://codewithhugo.com/change-the-date-of-a-git-commit/  

One of the greatest and worst things with git is that you can rewrite the history. Here’s a sneaky way of abusing that, I can’t think of a legitimate reason to do this.  As with anything, thanks StackOverflow for all the options I can pick from 👍.  

#### Set the date of the last commit to the current date
>GIT_COMMITTER_DATE="$(date)" git commit --amend --no-edit --date "$(date)"

#### Set the date of the last commit to an arbitrary date
>GIT_COMMITTER_DATE="Mon 20 Aug 2018 20:19:19 BST" git commit --amend --no-edit --date "Mon 20 Aug 2018 20:19:19 BST"

#### Set the date of an arbitrary commit to an arbitrary or current date
>Rebase to before said commit and stop for amendment:
>
>git rebase <commit-hash>^ -i
>Replace **pick** with **e** (edit) on the line with that commit (the first one)
>quit the editor (ESC followed by :wq in VIM)

Either:
>GIT_COMMITTER_DATE="$(date)" git commit --amend --no-edit --date "$(date)"
>GIT_COMMITTER_DATE="Mon 20 Aug 2018 20:19:19 BST" git commit --amend --no-edit --date "Mon 20 Aug 2018 20:19:19 BST"

See here for more information around rebasing and editing in git: 
Split an existing git commit. https://codewithhugo.com/split-an-existing-git-commit/

Following any of these 3 options, you will want to run:
>git rebase --continue
