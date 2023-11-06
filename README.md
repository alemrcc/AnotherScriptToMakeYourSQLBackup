# AnotherScriptToMakeYourSQLBackup
This is a script that I use in a scheduled manner to make the backup of certain MS SQL databases.
What I usually do is creating a folder called "BACKUP", and inside of it other 2 sub folders called
"SCRIPT" and "COPIES" (this COPIES folder you can change it in the config file.)
The concept of the script is "I will keep a certain amount of copies inside the directory and I will
insert a new copy only if the size of said copy will be different compared to the previous one ( I tried
to use the hash value of each copy but apparently it changes even with copies taken of the same db with no edits, 
probably is connected to the fact that somewere the current time of the copy is saved.)

I hope it will be useful to somebody!