import subprocess

git_commands = [
    "ls",
]

sp = subprocess.Popen(git_commands[0], shell=True,
                      stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
out, err = sp.communicate()
print('------------------------------------------------------------')
print(out)
