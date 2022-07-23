import os
import argparse as arg
import cyrtranslit as cyr

def main():
    parser=arg.ArgumentParser(description='Cyrillic to latin text file converter')
    parser.add_argument('-f','--filename',
                        help='Name of the file',
                        type=str)
    
    fileName=parser.parse_args()
    
    fileName=fileName.filename

    if fileName:
        if not os.path.exists(fileName):
            print("File doesn't exist!")
            quit()

        if not fileName.endswith('.txt'):
            print("File has to be a text file!")
            quit()
        
        print('The conversion from the file is:')
        with open(fileName) as file:
            for line in file:
                line=cyr.to_latin(line)
                print(line.rstrip())
    else:
        inputText=input('Enter the cyrillic to convert: ')
        converted=cyr.to_latin(inputText)
        print(f'The converted text is: {converted}')

if __name__ == '__main__':
    main()