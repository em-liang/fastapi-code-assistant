import os

exclude = ['.git', 'test', 'doc', 'scripts']
parsed = []

for (root,dirs,files) in os.walk('./fastapi-repo',topdown=True):
    for ex in exclude:
        dirs[:] = [x for x in dirs if ex not in x]
    files[:] = [x for x in files if x[-3:] == '.py']
    for file in files:
        parsed.append(str(os.path.join(root, file)))

with open("files-used.txt", "w") as f:
  for p in parsed:
    f.write(f'{p}\n')