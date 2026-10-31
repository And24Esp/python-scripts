folder = "C:\\Users\\ecues\\OneDrive\\Documentos\\03 Academico\\03 Computer \
Science\\Automation\\Python\\TLACSP exercises\\Ch13_files\\"

'''
myfile = open(folder+"test2.txt", "a")
myfile.write("\n2th file written from Python\n")
myfile.write("---------------------------------\n")
myfile.write("Dormir es para los debiles. \n")
myfile.close()
'''
'''
mynewhandle = open(folder+"test2.txt", "r")
while True:                            # Keep reading forever
    theline = mynewhandle.readline()   # Try to read next line
    if len(theline) == 0:              # If there are no more lines
        break                          #     leave the loop

    # Now process the line we've just read
    print(theline, end="")

mynewhandle.close()
'''
'''
f = open(folder+"friends.txt", "r")
xs = f.readlines()
f.close()

xs.sort()

g = open(folder+"sortedfriends.txt", "w")
for v in xs:
    g.write(v)
g.close()

print(type(f))
print(type(g))
print(type('bye'))
'''
'''
f = open(folder+"sortedfriends.txt")
content = f.read()
f.close()

words = content.split()
print("There are {0} words in the file.".format(len(words)))
'''
'''
e = open(folder+"somefile.zip", "wb")
f = open(folder+"somefile.zip", "rb")
g = open(folder+"thecopy.zip", "wb")

while True:
    buf = f.read(1024)
    if len(buf) == 0:
         break
    g.write(buf)

f.close()
g.close()
'''
'''
import urllib.request

url = "http://openbookproject.net/thinkcs/python/english3e/files.html"
destination_filename = folder+"test5.txt"

urllib.request.urlretrieve(url, destination_filename)
'''
'''
import urllib.request

def retrieve_page(url):
    """ Retrieve the contents of a web page.
        The contents is converted to a string before returning it.
    """
    my_socket = urllib.request.urlopen(url)
    dta = str(my_socket.read())     #I changed the attribute given on the textbook, from "readall()" to "read()"
    my_socket.close()
    return dta

the_text = retrieve_page("http://openbookproject.net/thinkcs/python/english3e/files.html")
print(the_text)
'''
#Chapter 13 Exercises:
'''
def reverse_line_order(original,new):
    """Reads a file and writes out a new file with the lines in reversed order"""
    handle1 = open(original,"r")
    handle2 = open(new,"w")
    xs = handle1.readlines()
    for i in range(-1,-len(xs)-1,-1):
        handle2.write(xs[i])
    handle1.close
    handle2.close

reverse_line_order(folder+"test1.0.txt", folder+"test1.1.txt")
'''
'''
def print_snake_substrings(file):
    """Reads a file and prints only those lines that contain the substring snake."""
    handle1 = open(file,"r")
    xs = handle1.readlines()
    for i in range(len(xs)):
        if 'snake' in xs[i]:
            print(xs[i], end='')
    handle1.close

print_snake_substrings(folder+"test2.txt")
'''
'''
def insert_digit_columns(oldFile,newFile):
    """ Reads a text file and produces an output file which is a copy of the file, 
    except the first five columns of each line contain a four digit line number"""
    handle1 = open(folder+oldFile,'r')
    line_list = handle1.readlines()
    handle2 = open(folder+newFile,'w')
    for i in range(len(line_list)):
        handle2.write('{0:>4}'.format(i+1)+' ')
        handle2.write(line_list[i])
    handle1.close
    handle2.close

insert_digit_columns("test3.0.py","test3.1.py")
'''

def remove_digit_columns(oldFile,newFile):
    """Reads a text file and produces an output file which is a copy of the file, 
    except the first five columns of each line contain a four digit line number"""
    handle1 = open(folder+oldFile,'r')
    line_list = handle1.readlines()
    new_line_list = []
    for i in range(len(line_list)):
        new_line_list.append(line_list[i][5:])
    
    handle2 = open(folder+newFile,'w')
    for i in range(len(new_line_list)):
        handle2.write(new_line_list[i])
    handle1.close
    handle2.close
    
remove_digit_columns("test3.1.py","test4.1.py")
