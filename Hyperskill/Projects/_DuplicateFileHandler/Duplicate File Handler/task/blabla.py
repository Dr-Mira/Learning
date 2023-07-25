import os
import sys
import fnmatch as fn
result = dict()


def tree():
    for root_dir_path, sub_dirs, files in os.walk('D:\Music'):
        for i in files:
            if fn.fnmatch(i, f'*.mp3'):
                file = f'{root_dir_path}\\{i}'
                size = os.stat(f'{root_dir_path}\\{i}').st_size
                result[size] = file


print('Enter file format')
format_option = str(input())
print()
print('Size of sorting options')
print('1. Descending')
print('2. Ascending')
print()

while True:
    print('Enter a sorting option')
    sorting_option = str(input())
    if sorting_option in '12':
        break
    else:
        print('Wrong option\n')

tree()

if sorting_option == '1':
    result = sorted(result, reverse=True)
elif sorting_option == '2':
    result = sorted(result)

for i in result:
    print(i)



        # filtered = fn.filter(lst, 'th?s')
        #
        #
        # files = [i for i in files if i.endswith(f'.{format_option}')]

# for i in set(files):
#     print(i, files.count(i))




