'''
Code formatter.
This code will format the code into a triangle and put it to a new file, and it will make sure it is a valid code.
Written by: Eym6565 in 09/07/2023.
'''

'''
This part imports necessary libraries.
'''
import sys
import os
import re

'''
This part defines the functions.
'''
def format(code):
    '''
    This function formats the code.
    '''
    code = code.split('\n')
    for i in range(len(code)):
        code[i] = code[i].strip()
    code = '\n'.join(code)
    code = re.sub(r' +', ' ', code)
    code = re.sub(r' *\n *', '\n', code)
    code = re.sub(r'\n+', '\n', code)
    code = re.sub(r'\n', '\n    ', code)
    return code + '\n'


'''
This part defines the main function.
'''

def main():
    '''
    This is the main function.
    '''
    if len(sys.argv) != 2:
        print('Usage: python format.py <file>')
        return
    if not os.path.exists(sys.argv[1]):
        print('Error: file not found.')
        return
    with open(sys.argv[1], 'r') as file:
        code = file.read()
    code = format(code)
    with open(sys.argv[1] + '.formatted', 'w') as file:
        file.write(code)

'''
This part runs the main function.
'''
if __name__ == '__main__':
    main()
