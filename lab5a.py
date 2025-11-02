#!/usr/bin/env python3
#Author: Agnestra Mahat
# Author ID:128939238
#Lab5 Inv1 Part1

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    f = open(f'{file_name}', 'r')               # Open file
    string_data = f.read()                      #Read from the file   
    f.close()                                   #close the file
    return string_data                          #return the contents of the file  as a string 
                                  

def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters
    f = open(f'{file_name}', 'r')              #open the file
    list_data = f.readlines()
    datalist = []
    for item in list_data:
        item = item.strip()
        datalist.append(item)
    f.close()
    return datalist

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
