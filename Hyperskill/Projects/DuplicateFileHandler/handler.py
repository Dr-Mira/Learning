import sys
import os
import fnmatch as fn
result = dict()


# def check():
#     if len(sys.argv) < 2:
#         print('Directory is not specified')
#         exit()


def tree():
    for root_dir_path, sub_dirs, files in os.walk('D:/Music'):
        for i in files:
            if fn.fnmatch(i, f'*.mp3'):
                file = f'{root_dir_path}\\{i}'
                size = os.stat(f'{root_dir_path}\\{i}').st_size
                result[size] = file
    return result

def main():
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

    files = tree()

    if sorting_option == '1':
        result = sorted(files, reverse=True)
    elif sorting_option == '2':
        result = sorted(files)

    for i in result:
        print(f'{i} bytes')
        for j in result[i]:
            print(j)



if __name__ == '__main__':
    # check()
    main()
