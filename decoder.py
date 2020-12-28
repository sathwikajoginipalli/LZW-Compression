##sathwika joginipalli ID-801166442
import math
import sys
import struct

class decoder:
    
    def __init__(self, filename, N):
        ## filename ->text file which is to be compressed
        ## N        ->bit length
        self.filename = filename
        self.N = N
        
    def decode(self):
        decoded = []
        ##decoded -> list where the decoded string is stored
        input_file = open(self.filename,"rb")
        code=[]
        ## code -> list to store compressed numbers
        while True:
            initstring = input_file.read(2) 
            if len(initstring)!=2:
                break
            (data, )= struct.unpack('>H',initstring)
            code.append(data)
        input_file.close()
        table = {}
        ## table -> dictionary where keys-ASCII values,values-corresponding characters
        MAX_TABLE_SIZE= pow(2,self.N) 
        for i in range(0,256):
            temp = str(i)
            table[temp] = str(chr(i))
        current_table_size = 255
        string = table[str(code[0])]
        decoded.append(string)
        for i in range(1,len(code)):
            if str(code[i]) not in table.keys():
                new_string = string + string[0]
            else:
                new_string = table[str(code[i])]
            decoded.append(new_string)
            if len(table)< MAX_TABLE_SIZE:
                table[str(current_table_size+1)] = string + new_string[0]
                current_table_size+=1
            string = new_string
        no_extention_filename = self.filename.split(".")[0]
        output_file = open("{}_decoded.txt".format(no_extention_filename),"w")
        output_file.write("".join(decoded))
        output_file.close()
## by importing "sys" we can take arguments from command line     
filename = sys.argv[1]
N = int(sys.argv[2])
decode_file = decoder(filename, N)
decode_file.decode()
    
