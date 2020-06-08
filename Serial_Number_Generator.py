import random, os, string, time, sys 
os.system('Serial Number Generator')
digits = string.digits
rangeL = string.ascii_uppercase + string.digits
print('Serial Generator')
print('Products:\nSerial Name #1\nSerial Name #2\nSerial Name #3\nSerial Name #4\nSerial Name #5\nSerial Name #6\nSerial Name #7\nSerial Name #8\nSerial Name #9\nSerial Name #10\nSerial Name #11\nSerial Name #12\nSerial Name #13\nSerial Name #14\nSerial Name #15')
whatproduct = input('Number (#) of product you would like to generate?: ')
print('')
try:

    if whatproduct =='#1' or whatproduct == '1':
        product = ['8806LZ03T']
        small = ['C', 'W', 'B', 'T', 'A']
        num = '9'
    if whatproduct == '#2' or whatproduct == '2':
        product = ['1234ABCD1']
        small = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        num = '8'    
    if whatproduct == '#3' or whatproduct == '3':
        product = ['1212LZ001']
        small = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K' ,'L', 'M', 'Q', 'R', 'S' ]
        num = '8'    
    if whatproduct == '#4' or whatproduct == '4':
        product = ['4213LZ0BS']
        small = ['U', 'N', 'M', 'Q', 'R', 'S', 'T', 'V']
        num = '8'
    if whatproduct == '#5' or whatproduct == '5':
        product = ['0000AAAA1']
        small = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        num = '8'
    if whatproduct == '#6' or whatproduct == '6':
        product = ['0000AAAA1']
        small = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        num = '8'
    if whatproduct == '#7' or whatproduct == '7':
        product = ['0000AAAA1']
        small = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N' 'O', 'P']
        num = '8'
    if whatproduct == '#8' or whatproduct == '8':
        product = ['8806LZ03T']
        small = ['G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'W', 'E']
        num = '8'
    if whatproduct == '#9' or whatproduct == '9':
        product = ['8806LZ03T']
        small = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'Q', 'R', 'S']
        num = '8'
    if whatproduct == '#10' or whatproduct == '10':
        product = ['8806LZ03T']
        small = string.ascii_uppercase + string.digits
        num = '8'
    if whatproduct == '#11' or whatproduct == '11':
        product = ['1830LZ0ZM']
        small = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
        num = '8'
    if whatproduct == '#12' or whatproduct == '12':
        product = ['1940LZ51U']
        small = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'Q', 'R', 'S']
        num = '8'
    if whatproduct == '#13' or whatproduct == '13':
        product = ['8806LZ03T', '1841MR13BA', '1841MR13AA', '1841MR13AB', '1841MR13AC', '1841MR13AD', '1841MR13AE', '1841MR13AF', '1841MR13A1', '1841MR13A2', '1841MR13A3', '1841MR13A4', '1841M13A5', '1841M13A6', '1841M13A7', '1841M13A8', '1841M13A9', '1841MR13A0']
        small = ['']
        num = '8'
    if whatproduct == '#14' or whatproduct == '14':
        product = ['8806LZ03T']
        small = ['A', 'B', 'C', 'D', 'E', 'F', 'F', 'G', 'H', 'I', 'J', 'K' ,'L', 'Q', 'R', 'S', '0','1', '2', '3', '4', '5', '6', '7', '8', '9']
        num = '8'
    if whatproduct == '#15' or whatproduct == '15':
        product = ['8806LZ03T']
        small = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
        num = '8'

    def generate_serials():
    	return ''.join([random.choice(product) for x in range(1)]) + ''.join([random.choice(small) for x in range(1)]) + ''.join([random.choice(rangeL) for x in range(1)]) + num

    for serialAmount in range(10): # displayed keys
        print(generate_serials())

except ValueError:
    print('\nWARNING...')
    print('ValueError (did you put in a number?')
else:
    print('\nTerminating program in 1 hour...')
    time.sleep(3600) # value in seconds
    sys.exit() 

input('Press ENTER to exit')