import os
files_mass = []
for root, dirs, files in os.walk('./'):
    for file in files:
        file_path = os.path.join(root, file)
        files_mass.append(os.stat(file_path).st_size)
size_threshold = 1
output = {}
for _ in range(len(str(max(files)))):
    size_threshold *= 10
    output[size_threshold] = 0
for file in files_mass:
    output[10 ** len(str(file))] += 1

print(output)