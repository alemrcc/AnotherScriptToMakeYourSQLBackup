import pyodbc
import const

DRIVER_NAME = const.DRIVER_NAME
SERVER_NAME = const.SERVER_NAME
UID = const.UID
PASSWORD = const.PASSWORD
WINAUTH = const.USE_WIN_AUTHENTICATION
WHERECONDITION = const.WHERECONDITION
BACKUP_FOLDER = const.BACKUP_FOLDER

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

                SET @path = '{BACKUP_FOLDER}\'

                SELECT @fileDate = CONVERT ( VARCHAR ( 20 ), GETDATE (), 112 ) 

                DECLARE db_cursor CURSOR FOR 
                SELECT name 
                FROM master.dbo.sysdatabases 
                WHERE {WHERECONDITION}

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
