import os

root_tree = 'C:\\Users\\ecues\\OneDrive\\Documentos\\03 Academico\\03 Computer \
Science\\Automation\\Python\\TLACSP exercises\\Ch18_recursion\\litter_test_lv0'

def get_dirlist(path):
    """Return a sorted list of all directories in path"""
    
    folders_list = []

    def get_dirlist2(path):
        nonlocal folders_list
        dirlist = os.listdir(path)
        for f in dirlist:
            fullname = os.path.join(path, f)   # Turn name into full pathname
            if os.path.isdir(fullname):
                folders_list.append(fullname)
                get_dirlist2(fullname)

    get_dirlist2(path)

    return folders_list

#print(get_dirlist(root_tree))

def litter(path):
    for i in get_dirlist(path):
        open(i+'\\trash.txt','w')
    print('Files created!')

litter(root_tree)