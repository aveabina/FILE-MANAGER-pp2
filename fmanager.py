import os
import subprocess
import shutil
from sys import platform

def Cat(l,symb):
    cd = input('-Enter catalog name: \n ')
    catalog = (l + symb + cd)
    files = os.listdir(catalog)
    os.chdir(l + symb + cd)
    for i in files:
        print(i)
    file = os.chdir(l + symb + cd)
    return(catalog)

def upCat(l,symb):
    ccat = l.split(symb)
    print(ccat[-1])
    cd = l.split(symb+ccat[-1])
    print(cd[0])
    return(cd[0])

def delFile(l,symb):
    d = input('-Input way to file for delete: ')
    os.remove(l + symb + d, dir_fd=None)
    print('-File', d, 'deleted from :', l, 'catalog-')

def delCat(l,symb):
    d = input('-Input way to catalog for delete: ')
    os.rmdir(l + symb + d)
    print('-Catalog', d, 'deleted from:', l, '-')

def Filenew(l,symb):
    fn = input('-Input file name: ')
    open(fn, "w")
    print('-File ', fn, ' created in: ', l,'-')

def Catnew(l,symb):
    cn = input("-Input catalog name:")
    os.mkdir(cn)
    print('-Catalog', cn,' created in: ', l,'-')

def Read(l,symb):
    print('-Input way to file: ')
    fi = input()
    refi = open(l + symb + fi)
    strs = refi.read()
    print(strs)
    refi.close()
    print('-File ', fi, 'readed-')

def Write(l,symb):
    print('-Input way to file: ')
    fi = input()
    wfi = open(l + symb + fi, "a")
    writing = input('-Enter text: \n')
    wfi.write(writing)
    wfi.close()
    print('-Text added in ', fi,'-')

def CopyF(l,symb):
    f1 = input('-Input way to file for copy: \n')
    f2 = input('-Input way where copy: \n')
    shutil.copy2(l + symb + f1, l + symb + f2)
    print('-File copied in ', l + symb + f2,'-')

def MoveF(l,symb):
    f1 = input('-Input way to file for move: \n')
    f2 = input('-Input way where move: \n')
    shutil.move(l + symb + f1, l + symb + f2)
    print('-File moved in ', l + symb + f2,'-')

def RenameF(l,symb):
    f1 = input('-Input way to file for rename: \n')
    f2 = input('-Input new name for file: \n')
    os.rename(l + symb + f1, l + symb + f2)
    print('-File renamed ', l + symb + f2,'-')

def OpenF(l,symb):
    fopen = input('-Input file name: ')
    cmd = fopen
    subprocess.Popen(cmd, shell=True)

def __main__():
    symb = '/'
    c=''
    l = input('Enter work catalog: ')
    homecat = l
    print(symb)
    while c != 'stop':
        catalog = (l)
        files = os.listdir(catalog)
        file = os.chdir(l)
        print('Current catalog: ', l)
        print('Home catalog: ', homecat)
   
        print('Enter command, "help" to help: ')
        c = input('>>>')
        if c == 'help':
            print('\n "Cat" to go other catalog '
                '\n "upCat" to go catalog up '
                '\n "lsCat" to show content of current catalog '
                '\n "Filenew" to create new file '
                '\n "Catnew" to create new catalog '
                '\n "delFile" to delete file '
                '\n "delCat" to delete catalog '
                '\n "Read" to read file'
                '\n "Write" to add text to file'
                '\n "CopyF" to copy file'
                '\n "MoveF" to move file'
                '\n "RenameF" to rename file'
		'\n "OpenF" to open file \n'               
                '"stop" to stop programm\n',
                l)
        elif c == 'lsCat':
            for i in files:
                print(i)
        elif c == 'Cat':
            l = Cat(l,symb)
        elif c == 'upCat':
            if l == homecat:
                print('-You are in home catalog, cannot go up-')
            else:
                l = upCat(l,symb)
        elif c == 'delFile': 
            delFile(l,symb)
        elif c == 'delCat': 
            delCat(l,symb)
        elif c == 'Filenew':
            Filenew(l,symb)
        elif c == 'Catnew':
            Catnew(l,symb)
        elif c == 'Read':
            Read(l,symb)
        elif c == 'Write':
            Write(l,symb)
        elif c == 'CopyF':
            CopyF(l,symb)
        elif c == 'MoveF':
            MoveF(l,symb)
        elif c == 'RenameF':
            RenameF(l,symb)
        elif c == 'OpenF':
            OpenF(l,symb)
        elif c == 'stop':
            print('Stop programm')
        else:
            print('Invalid input\n Try again')

if __name__ == "__main__":
    __main__()
