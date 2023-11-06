# DRIVER_NAME = "{/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.10.so.2.1}"
DRIVER_NAME = "{ODBC Driver 17 for SQL Server}"
SERVER_NAME = "localhost"
USE_WIN_AUTHENTICATION = True
UID = "backupsa"
PASSWORD = "ImtheonedoingtheBackup"
WHERECONDITION = "WHERE [name] LIKE 'ADB%' AND [name] NOT IN ('ADB_SYSTEM', 'ADB_DEMO')"
BACKUP_FOLDER = "/home/backupuser/backup/"
