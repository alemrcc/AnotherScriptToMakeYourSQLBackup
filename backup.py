import pyodbc
import const
import os
import socket
import glob

DRIVER_NAME = const.DRIVER_NAME
SERVER_NAME = const.SERVER_NAME
UID = const.UID
PASSWORD = const.PASSWORD
WINAUTH = const.USE_WIN_AUTHENTICATION
WHERECONDITION = const.WHERECONDITION
BACKUP_FOLDER = const.BACKUP_FOLDER + os.sep


def backup():
    # first, i need to check if SERVER_NAME is the current machine, if it is not, i will not do anything
    # if (
    #    socket.gethostname() != SERVER_NAME
    #    and socket.gethostbyname(socket.gethostname()) != SERVER_NAME
    # ):
    #    print(
    #        "You are trying to backup from a machine that is not the machine where the instance is installed. You can't do that."
    #    )
    #    return None

    if WINAUTH:
        conn = pyodbc.connect(
            f"Driver={DRIVER_NAME};Server={SERVER_NAME};Trusted_Connection=yes;"
        )
    else:
        conn = pyodbc.connect(
            f"Driver={DRIVER_NAME};Server={SERVER_NAME};UID={UID};PWD={PASSWORD};"
        )

    sqlCommand = f"""DECLARE @name VARCHAR ( 50 ) -- database name 
                    DECLARE @path VARCHAR ( 256 ) -- path for backup files 
                    DECLARE @fileName VARCHAR ( 256 ) -- filename for backup 
                    DECLARE @fileDate VARCHAR ( 20 ) -- used for file name 

                    SET @path = '{BACKUP_FOLDER}'

                    SELECT @fileDate = CONVERT ( VARCHAR ( 20 ), GETDATE (), 112 ) 

                    DECLARE db_cursor CURSOR FOR 
                    SELECT name 
                    FROM master.dbo.sysdatabases 
                    {WHERECONDITION}

                    OPEN db_cursor 
                    FETCH NEXT FROM db_cursor INTO @name 

                    WHILE @@FETCH_STATUS = 0 
                    BEGIN 
                    SET @fileName = @path + @name + '_' + @fileDate + '.BAK' 
                    BACKUP DATABASE @name TO DISK = @fileName with init 

                    FETCH NEXT FROM db_cursor INTO @name 
                    END 

                    CLOSE db_cursor 
                    DEALLOCATE db_cursor"""

    # fisrt i will check if the directory exists, if it doesn't I will create it
    os.makedirs(BACKUP_FOLDER, exist_ok=True)

    # now i will execute the sql command
    conn.autocommit = True
    cursor = conn.cursor()
    print("Starting the backup...")
    cursor.execute(sqlCommand).commit()
    print("Backup done!")

    # now i will check all the names of the different databases
    backup_files = glob.glob(BACKUP_FOLDER + "*_????????.bak")
    # with os.listdir(BACKUP_FOLDER) as entries:
    #    print("im in 1")
    #    for entry in entries:
    #        print("im in 2")
    #        if entry.is_file() and re.match("*_????????.bak", entry.name):
    #            print("im in 3")
    #            backup_files.append(entry.name)
    for name in backup_files:
        print(name)
    # now i will check if the last backup done, for each database, has the sime size as the previous one, if it does I will delete the last one

    # now, considering hom many copies of each db I have to keep I will delete the oldest ones


backup()
