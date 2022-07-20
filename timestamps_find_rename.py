import os  # чтобы получить лист названия файлов
import re  # regex
import numpy as np

dir_path = '/home/qq/Vault/test'

# рабочая версия
with os.scandir(dir_path) as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file() and entry.name.endswith('.md') and not re.search(r'[0-9]{14}', entry.name):
            file_path = dir_path + '/' + entry.name
            with open(file_path, encoding='utf-8') as f:
                full_file = f.readlines()[:6]
            file_search = [1 if re.search(r'timestamp:: [0-9]+', i) else 0 for i in full_file]
            if any(file_search):
                timestamp_in = np.argmax(file_search)
                # print('old:', full_file[timestamp_in])
                if len(re.search(r'[0-9]+', full_file[timestamp_in]).group(0)) < 14:
                    timestamp = re.search(r'[0-9]+', full_file[timestamp_in]).group(0)
                    timestamp = timestamp + str((int(timestamp[-1]) + int(timestamp[-2]))) + str((int(timestamp[-3]) + int(timestamp[-4])))
                    # print('new:', timestamp)
                    if len(timestamp) > 14:
                        timestamp = timestamp[:14]
                else:
                    timestamp = re.search(r'[0-9]+', full_file[timestamp_in]).group(0)
                new_file_lines = [re.sub(r".md", '', entry.name) + '\n']
                new_file_name = dir_path + '/' + timestamp + '.md'
                with open(file_path, encoding='utf-8') as f:
                    full_file = f.readlines()
                full_file.pop(timestamp_in)
                new_file_lines.extend(full_file)
                print(new_file_lines)
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(''.join(new_file_lines))
                os.rename(file_path, new_file_name)