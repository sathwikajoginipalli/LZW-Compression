##sathwika joginipalli ID-801166442
import math
import sys
import struct

class encoder:
    
    def __init__(self, filename, N):
        ## filename ->text file which is to be compressed
        ## N        ->bit length
        self.filename = filename
        self.N = N
        
    def encode(self):
        encoded = []
        ##encoded -> list where the compressed bits are stored
        input_file = open(self.filename,"r")
        initstring = input_file.read().strip()
        input_file.close()
        table = {}
        ##table -> dictionary where keys-characters,values-corresponding ASCII values
        MAX_TABLE_SIZE= pow(2,self.N)
        for i in range(0,256):
            table[str(chr(i))] = i
        current_table_size = 255
        string = ""
        for symbol in initstring:
            if string + symbol in table.keys():
                string = string + symbol
            else:
                encoded.append(table[string])
                if len(table)< MAX_TABLE_SIZE:
                    table[string+symbol] = current_table_size+1
                    current_table_size+=1
                string = symbol
        encoded.append(table[string])
        no_extention_filename = self.filename.split(".")[0]
        output_file = open("{}.lzw".format(no_extention_filename),"wb")
        for code in encoded:
            output_file.write(struct.pack('>H',code))
        output_file.close()
## by importing "sys" we can take arguments from command line     
filename = sys.argv[1]
N = int(sys.argv[2])
encode_file = encoder(filename, N)
encode_file.encode()
    


                
                
            
            
        
        
        
    
        
    
    

    
  
