## sathwika joginipalli 
The Lempel–Ziv–Welch (LZW) algorithm is a lossless data compression algorithm.
This algorithm has two steps: 
1. Encoding/Compressing 
2. Decoding/Decompressing

Encoding/Compressing:  encoder.py
The code imports two modules math, sys,import where math is imported for basic mathematical operations(power) ,sys for taking arguments from the console,import for packing into compressed data
The class  encoder have two functions:

1.__init__: It is a magic function of python which is basically like a constructor in OOPS. By calling this method  we create an object of the class and it allow the class to initialize the attributes of a class. Here in my code  input                       file which is to be compressed and the bit length are the objects of  the class. Whenever we use them, they must be in the format self.objectname.

2.encode() : The actual encoding is done in this function. At first a list called "encoded" is created to store the compressed output. Then the input file which is to be compressed is opened in read mode. "initstring" contains                             the string in the input file, without any spaces at the ends(if given any) as strip function is used.

	     A dictionary called "table" is created whose maximum size is MAX_TABLE_SIZE, where MAX_TABLE_SIZE is 2 power bit length. ASCII values for 0 to 255 characters are inserted into the table using for loop and then                         the current size of table is stored in "current_table_size" to keep track the next location of table where the values are to be inserted.

	     The process of encoding is carried out like the given pseudocode and now the "encoded" list contains the values(ASCII values) of compressed input string. 
	                                 
                      "no_extention_filename" contains the name of input file without .txt extention. An "output_file" is created in write mode which will have inputfile name with .lzw extention.
 	     
                      Next the "output_file" which is in binarywrite mode will be inserted with the hexadecimals(compressed version) of encoded data by using struct.pack(format,string) method. Then the "output_file" will be closed.

	     sys.argv[1] and sys.argv[2] which are command line arguments of inputfile.txt and bit length are given to filename and N. encode_file takes the input arguments and passes to encode() function.

Decoding/Decompressing: decoder.py
The code imports two modules math, sys,import as in encoder.py.
The class decoder have 2 functions:

1.__init__: It is a magic function of python which is basically like a constructor in OOPS. By calling this method  we create an object of the class and it allow the class to initialize the attributes of a class. Here in my                                            code  input file which is to be compressed and the bit length are the objects of  the class. Whenever we use them, they must be in the format self.objectname.

2.decode() : This function decodes the input string and stores it in the list named "decoded". The compressed input file which is to be decoded is opened in binary read mode and code[] list is created.
                     
                    Using struct.unpack(format,string) method we unpack the hexadecimal to numbers into list code[] which is to be restored back into  given string.

                     A dictionary called "table" is  created similar to the table in encoder, but the keys and values are interchanged. In this dictionary the keys are ASCII values and the values are corresponding characters.
               
                     Decoding is done as in the pseudocode and "decoded" list now contains the decompressed string. 

                     "no_extention_file"  is the input file name without .lzw extention. "output_file" is created and opened in write mode with the inputfile name_decoded.txt. "decoded" list is written into the output_file and then                            closed after writing.

                      sys.argv[1] and sys.argv[2] which are command line arguments of inputfile.lzw and bit length are given to filename and N. decode_file takes the input arguments and passes to decode() function.
