import os
arr = ['settings', 'mainapp', 'adminapp', 'authapp']
for i in arr:
    dir_path = os.path.join('data', i)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
