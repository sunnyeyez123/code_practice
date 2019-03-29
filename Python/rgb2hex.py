def rgb_hex():
  INVALID_MSG = "Invalid input. Please try again"
  red = int(raw_input("Enter a value for red: "))
  if red < 0 or red > 255:
    print INVALID_MSG
    return
  green = int(raw_input("Enter a value for green: "))
  if green < 0 or green > 255:
    print INVALID_MSG
    return
  blue = int(raw_input("Enter a value for blue: "))
  if blue < 0 or blue > 255:
    print INVALID_MSG
    return
  val = (red << 16) + (green << 8) + blue
  print  "%s" % (hex(val)[2:]).upper()

def hex_rgb(): 
  hex_val = raw_input("Enter a Hex value: ")
  if len(hex_val) !=6:
    print INVALID_MSG
    return
  else:
    hex_val = int(hex_val,16)
  two_hex_digits = 2**8
  blue= hex_val % two_hex_digits
  hex_val = hex_val >>8
  green = hex_val % two_hex_digits
  hex_val = hex_val >>8
  red = hex_val % two_hex_digits
  print "Red: %s, Green: %s, Blue: %s" % (red, green, blue)
  
def convert():
  while(True):
    option = raw_input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit: ")
    if option == '1':
      rgb_hex()
    elif option == '2':
      hex_rgb()
    elif option == 'X'or option == 'x':
      break
    else:
      print "Invalid input. Please try again"
      
convert()
      
    
  
  
  
  
  