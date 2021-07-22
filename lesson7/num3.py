import os
import shutil
source_dir = 'my project'
dir_name = 'templates'
for i, a, r in os.walk(source_dir):
    if i.find(dir_name) > 0 and len(r) == 0:
        shutil.move(os.path.join(i), dir_name, dirs_exists_ok=True) #Я решил не удалять файлы вообще, а просто переместить их в нужную директроию
