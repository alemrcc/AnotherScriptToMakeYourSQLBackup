# DRIVER_NAME = "{/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.10.so.2.1}"
# DRIVER_NAME = "{ODBC Driver 18 for SQL Server}"
DRIVER_NAME = "{SQL Server}"
SERVER_NAME = "10.0.0.179"
USE_WIN_AUTHENTICATION = True
UID = "backupsa"
PASSWORD = "ImtheonedoingtheBackup"
WHERECONDITION = "WHERE [name] LIKE 'ADB%' AND [name] NOT IN ('ADB_SYSTEM', 'ADB_DEMO') and [name] = 'ADB_GELA'"
BACKUP_FOLDER = "C:\OSRA\COPIE"
