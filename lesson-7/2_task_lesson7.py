import os
import shutil
folder = 'my_project'
new_folder = 'templates'
dirs = [item
            for item in os.listdir(folder)
            if os.path.isdir(os.path.join(folder, item)) if item[-3:] == "app"]
if not os.path.exists(new_folder):
	os.mkdir(new_folder)
for i in dirs:
	if not os.path.exists(os.path.join(folder, new_folder, i)):
		shutil.copytree(os.path.join(folder, i), os.path.join(folder, new_folder, i))
print(dirs)
