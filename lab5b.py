#!/usr/bin/env python3
#Author: Agnestra Mahat
# Author ID:128939238
#Lab5 Inv1 Part2

# without comments

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

def append_file_string(file_name, string_of_lines):
    # Takes two strings, appends the string to the end of the file
    f = open(f'{file_name}', 'a')
    f.write(string_of_lines)
    f.close()
    return f
def write_file_list(file_name, list_of_lines):
    # Takes a string and list, writes all items from list to file where each item is one line
    f = open(f'{file_name}', 'w')
    for item in list_of_lines:
        f.write(str(item) + '\n')
    f.close()

def copy_file_add_line_numbers(file_name_read, file_name_write):
    # Takes two strings, reads data from first file, writes data to new file, adds line number to new file
    f = open(f'{file_name_read}', 'r')
    list_data = f.readlines()
    f.close()
    f = open(f'{file_name_write}', 'w')
    datalist = []
    n = 1
    for item in list_data:
        f.write(f"{n}:{item}")
        n += 1
    f.close()
    return datalist
    

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))
   