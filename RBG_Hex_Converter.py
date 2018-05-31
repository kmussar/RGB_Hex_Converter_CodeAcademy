""" This program converts RGB to HEX and vice versa."""

# Initialize static variables and import neccessary items. 
invalid_msg = "The value that you entered is invalid."
from time import sleep 

# This function converts RGB to HEX 
def rgb_hex():
  # First, request RGB values from the user
  # Check to make sure they are valid inputs
  red = int(input("Please enter a value for red. "))
  if red < 0 or red > 255: 
    print(invalid_msg)
    sleep(1)
    return
  green = int(input("Please enter a value for green. "))
  if green < 0 or green > 255: 
   print(invalid_msg)
   sleep(1)
   return
  blue = int(input("Please enter a value for blue. "))
  if blue < 0 or blue > 255: 
    print(invalid_msg)
    sleep(1)
    return

  #Next, converting the inputs to HEX values (this is outside of the if statements)
  val = (red << 16) + (green << 8 ) + (blue)
  print("%s" % (hex(val)[2:]).upper())

# This function converts HEX to RGB  
  # First, request HEX values from the user. 
  # As above, check that they are valid inputs. 
def hex_rgb(): 
  hex_val = input("Please enter a hexadecimal value. ")
  print(len(hex_val))
  if len(hex_val) != 5: 
    print(invalid_msg)
    return
  else: 
    hex_val = int(hex_val,16)
  two_hex_digits = 2 ** 8
  blue = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  green = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  red = hex_val % two_hex_digits
  print("%s%s%s" % (red, green, blue))
  print("Red: %s Green: %s Blue:%s" % (red, green, blue))
  
# This function contains the operations of the program  
def convert(): 
  while True: 
    option = input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit: ")
    if option == "1": 
      print("RGB to Hex...")
      rgb_hex()
    elif option == "2": 
      print("Hex to RGB...")
      hex_rgb()
    elif option == "X" or option == "x": 
      break
    else: 
      print("Error")

# This statement runs the program.      
convert()
