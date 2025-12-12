# from pathlib import Path
# logs_path = Path("D:\Logs_all\Logs\OldLogs")
# match_file = 'AccountPrune*.log'
# str_find = 'was removed - (241 days since last access)'
# py_files_generator = logs_path.rglob(match_file)
# for filename in py_files_generator:
#     print(filename)
#     while True:
#         line = filename.read_text()
#         print(line)
#             # if line.find(str_find) != -1:
#             #     print(filename, line)
#             # if not line:
#             #     break



import os, glob
folder_path = r"D:\Logs_all"
#folder_path = input('Введите путь к папке для поиска: ')
match_file = 'AccountPrune*.log'
str_find = 'was removed - (241 days since last access)'
#str_find = 'bakulina@gmail.com'
#str_find = input('Введите строку для поиска: ')
for filename in glob.glob(os.path.join(folder_path, match_file)):
    #print(filename)
    with open(filename, 'r') as f:
        while True:
            line = f.readline()
            if line.find(str_find) != -1:
                print(filename, line)
            if not line:
                break

