import os
folder = 'my_project'
folder_mass = ["settings", "mainapp", "adminapp", "authapp"]
for i in range(len(folder_mass)):
	if not os.path.exists(folder):
		os.mkdir(folder)
	dir_path = os.path.join('my_project', folder_mass[i])
	if not os.path.exists(dir_path):
   		os.mkdir(dir_path)