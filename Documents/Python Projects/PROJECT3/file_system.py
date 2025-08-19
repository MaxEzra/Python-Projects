"""
File: file_system.py
Name: Ezra Enchill
Date: 12/1/2022
Lab Section: 42
Description: Project 3
"""
def mkdir(d_name, dir_name): 
    """"
    d_name = inputted directory name
    dir_name = directory location  
    """
    if DIRECTORIES not in dir_name: 
        dir_name[DIRECTORIES] = {}      
        # Checks to see if given directory name is not in use
    elif DIRECTORIES in dir_name: 
        print("That name is already in use for another directory.")  
    dir_name[DIRECTORIES][d_name] = {}
    
    
def touch(fd_name, dir_name): 
    """ 
    fd_name = inputted file or directory name
    dir_name = name of specific directory it is in
    """
    FILES = 'files'
    dir_name[FILES] = []
    if fd_name in dir_name[FILES]:
        print("This file already exists in this directory.")
    elif FILES not in dir_name: 
        dir_name[FILES] = []
    dir_name[FILES].append(fd_name)

def rm(fd_name, dir_name):
    """ 
    fd_name = file or directory name
    dir_name = name of specific directory it is in
    """
    DIRECTORIES = 'directories' 
    FILES = 'files'
    if fd_name not in dir_name[DIRECTORIES] or dir_name[FILES]: 
        print("Object not found.")
    elif fd_name in dir_name[DIRECTORIES]: 
        del dir_name[DIRECTORIES][fd_name]
        print("Successfully deleted Directory.")
    elif fd_name in dir_name[FILES]: 
        del dir_name[FILES][fd_name]
        print("Successfully deleted file.")
    
def ls(dir_name):
    """ 
    dir_name = name of directory 
    """
    DIRECTORIES = 'directories'
    FILES = 'files'
    if dir_name in FILES:    
        print(dir_name[DIRECTORIES].keys())
        if FILES in dir_name: 
            print(dir_name(FILES))
    
    elif dir_name == "": 
        print()
        
def cd(fd_name, dir_name): 
    """ 
    fd_name = inputted file or directory name
    dir_name = name of specific directory it is in
    """
    HOME = 'home'
    if fd_name != "": 
        return dir_name[fd_name]
    
    elif fd_name == "":
        if dir_name == directory_system[HOME]: 
            return dir_name
        else: 
            for dir_1, dir_2 in directory_system[HOME].items():  
                for dir_2n in dir_2: 
                    dir_3 = dir_2[dir_2n]
                    if dir_3 == dir_name: 
                        return dir_2
    
    else: 
        print("Directory cannot be located")
        return dir_name                
                    
def pwd(dir_name): 
    print(dir_name)
    # Simply outputs current directory
    
def locate(fd_name, dir_name, path): 
    """ 
    fd_name = inputted file or directory name
    dir_name = name of specific directory it is in
    path = Path lists all the various paths to that file with given name
    """
    # base case
    for x in dir_name: 
        if x == fd_name: 
            print(path + fd_name)
            # recursive case
        else: 
            if x in dir_name: 
                locate(fd_name, dir_name[x], path + x)
    
    
    path = "/"
    fd_name = "/"



def parsed(parse, current_directory): 
    if parse[0] == "cd": 
        if len(parse) > 1: 
            fd_name = parse[1]
        return cd(fd_name, current_directory)
    elif parse[0] == "rm": 
        return rm(parse[1], current_directory)
    elif parse[0] == "ls": 
        return ls(current_directory)
    elif parse[0] == "pwd": 
        return pwd(current_directory)
    elif parse[0] == "touch": 
        return touch(parse[1], current_directory)
    elif parse[0] == "mkdir": 
        return mkdir(parse[1], current_directory)
    elif parse[0] == "locate": 
        return locate(parse[1], current_directory, "")
    
    





if __name__ == 'main': 
    DIRECTORIES = 'directories'
    FILES = 'files'
    HOME = 'home'
    current_directory = "/"
    catch = True
    
    
    directory_system = {
       HOME : {
            DIRECTORIES: {'dir1': {
                DIRECTORIES: {'dir1_in_dir2': {}},
                FILES: ['file1.txt']
            }
            },
            FILES: ['file3.txt']
       }
    }
    while catch == True: 
        parse = input("[cmsc201 proj3]$ ").lower()
        if parse == "exit": 
            catch = False
        else: 
            new = parse.strip().split()
            current_directory = parsed(new, directory_system)
            print(current_directory)


