import sys
import git



print "paste repo URL here"
url = raw_input()

print url

git.Repo.clone_from('https://github.com/DavidAwad/Arduino', 'local/')



print 'Success'
