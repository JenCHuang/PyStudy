# Copy data from teacher's share floder
import os
import shutil

path_local = r'C:\Shared'
path_origin= r'//172.22.34.240/Shared'

# 列出本地資料夾已有的資料夾與檔案列表
lst_path = []
lst_file = []
for paths, dirs, files in os.walk(path_local):
    lst_path.append(paths.split(path_local)[-1])
    for f in files:
        lst_file.append(paths.split(path_local)[-1]+'\\'+f)

print(f'Begin to visit {path_origin}')
# 訪問老師電腦中的共享資料夾，並複製資料到本地
skiplist = ['exe','msi','iso']
for paths, dirs, files in os.walk(path_origin):
    # 若共享資料夾有，而本地資料夾沒有的資料夾，建立該資料夾
    path_last = paths.split(path_origin)[-1]
    if path_last not in lst_path:
        print(f'Create dir:  {path_local+path_last}')
        os.mkdir(path_local+path_last)
    for f in files:
        if f.split('.')[-1] in skiplist: continue
        fmark = path_last + '\\' + f
        # 老師資料夾有，本地資料夾沒有的檔案，將其複製一份
        if fmark not in lst_file:
            print(f'Copying {path_origin+fmark} to local disk ......')
            shutil.copyfile(path_origin+fmark, path_local+fmark)
        # 老師資料夾有，本地資料夾有的檔案，但是是舊的，將其複製一份覆蓋本地資料
        # 採取比較最後修改時間
        elif os.path.getmtime(path_origin+fmark) > os.path.getmtime(path_local+fmark):
            print(f'Reflashing {path_origin+fmark} in local disk ......')
            shutil.copyfile(path_origin+fmark, path_local+fmark)
print('Done.')