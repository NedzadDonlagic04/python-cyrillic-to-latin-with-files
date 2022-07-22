import argparse as arg

def main():
    parser=arg.ArgumentParser(description='Cyrillic to latin text file converter')
    parser.add_argument('filename',
                        help='Name of the file',
                        type=str)
    
    fileName=parser.parse_args()
    fileName=fileName.filename
    
    file_handler=open(fileName)
    for line in file_handler:
        print(line.rstrip())

if __name__ == '__main__':
    main()