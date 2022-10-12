
#Decompression - It divided into two parts, one, print_decompressed_data, is to print out decompressed data (eg. it takes a list of lists of how many letters there is, for instance, [[2, 'a', 1, 'd', 6, '8'], [2, 's', 6, 'g', 9, 'a']] and returns aad888888, ssggggggaaaaaaaaa), and the other one being decompress_rle which decompresses 02a01d068 to aad888888

def print_decompressed_data(data):
  for line in data:
    count = 0
    data_lst = ''
    for a in range(len(line)//2):
      data_lst += line[count+1] * line[count]
      count += 2
    return data_lst

def decompress_rle(lst):
  for line in lst:
    decompressed_data = []
    count = 0
    one_line = []
    for a in range(len(line)//3):
      data = line[count:count+3]
      number = int(data[0:2])
      character = str(data[-1])
      count += 3
      one_line.extend([number, character])
    decompressed_data.append(one_line)
    print (print_decompressed_data(decompressed_data))


#Compression - Same as before. Print_compressed_data takes [[2, 'a', 1, 'd', 6, '8']] and returns 02a01d068 and is added to the compress_str function. On the other hand, the compress_str takes a list of items and compresses it, eg. ['aad88888']

def print_compressed_data(data):
  new_data = ''
  for line in data:
    count = 0
    for a in range(len(line)//2):
      if line[count] < 10:
        new_data += ('0' + str(line[count]))
      else:
        new_data += str(line[count])
      count += 1
      new_data += line[count]
      count += 1
  return new_data

def compress_str(lst):
  occurance = []
  for line in lst:
    line = line.strip()
    line_occurance = []
    next_letter = line[0]
    count = 1
    for a in range(len(line)):
      if len(line) > a+1 and next_letter != line[a+1]:
        line_occurance.extend([count, next_letter])
        next_letter = line[a+1]
        count = 1
      else:
        count += 1
    line_occurance.extend([count-1, next_letter])
    occurance.append(line_occurance)
  return print_compressed_data(occurance)


#Menu Functions

#This is an enter_rle function which accepts user input of the rle line by line. It asks for how many lines, if its <= 2 then displays error message. It then asks for the data line by line and stores it in variable 'data'.
def enter_rle ():
  lines = 0
  data = []
  while lines <= 2:
    lines = int(input("\nHow many lines of RLE compressed data would you like to enter:\n"))
    if lines > 2:
      while lines > 0:
        data.append(input("\nPlease input your line of compressed data:\n"))
        lines -= 1
      return data
    else:
      print ("Error. The number of lines must be greater than 2.")

#This function opens the ascii art the user inputs and reads it.
def display_art ():print (open(input("\nPlease enter the name of the text file that contains the ASCII art:\n"), 'r').read())

#This function decompresses the ascii rle the user inputs and displays the art image.
def convert_to_ascii_art (): print (decompress_rle(open(input("\nPlease enter the name of the text file that contains the ASCII art:\n"), 'r')))

#This function asks for input, opens a new file called LogoRLE_NEW.txt and writes to it. It then computes the difference of size between the ascii art file and compressed LogoRLE_NEW.txt and displays the space saved.
def convert_to_rle ():
  ascii_art = open(input("\nPlease enter the name of the text file that contains the ASCII art:\n"), 'r')
  compressed_data = open('LogoRLE_NEW.txt', 'r+')
  compressed_data.write(compress_str(ascii_art))
  compressed_data.seek(0)
  ascii_art.seek(0)
  ascii_count = 0
  for a in ascii_art:
    ascii_count += len(a.strip())
  print ('ASCII: ',ascii_count )
  compressed_count = 0
  for b in compressed_data:
    compressed_count += len(b.strip())
  print ('Compressed: ', compressed_count)
  print (f"\nSpace saved through compression: {ascii_count - compressed_count}")
  compressed_data.close()
  ascii_art.close()

convert_to_rle()

#Actual Menu
menu_input = None

while menu_input != 'quit' and menu_input != 'e':
  menu_input = input("\n\n\n================\n      Menu\n================\nA - Enter RLE \nB - Display ASCII art \nC - Convert to ASCII art \nD - Convert to RLE \nE - Quit\n\nPlease select from the following options: \n").lower()
  if menu_input == 'enter rle' or menu_input == 'a':
    decompress_rle(enter_rle())
  elif menu_input == 'display ascii art' or menu_input == 'b':
    display_art()
  elif menu_input == 'convert to ascii art' or menu_input == 'c':
    convert_to_ascii_art()
  elif menu_input == 'convert to rle' or menu_input == 'd':
    convert_to_rle()
  else:
    print ("\nUnknown command.")
print ("\nWe are sorry to see you go. Please consider donating.")
