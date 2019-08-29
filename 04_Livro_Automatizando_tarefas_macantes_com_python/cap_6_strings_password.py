#!/Users/macbookair/.conda/envs/Git/bin/python3

# A program to save passwords IT IS NOT SECURITY.

passwords = {"email": "testEMAILpassword",
             "blog": "testBLOGpassword",
             "luggage": "testLUGGAGEpassword"}

import sys, pyperclip

print("What's password do you look?")
sys.argv = input()


if len(sys.argv) < 2:
    print("Usage: python Password Program [account] - copy account password")
    sys.exit()

account = sys.argv[:]  # the first argument of command line is the name of account

if account in passwords:
    pyperclip.copy(passwords[account])
    print("Password for " + account + "copied to clipboard")
else:
    print("There ins't account named " + account)


