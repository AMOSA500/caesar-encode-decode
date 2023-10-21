from art import logo

print(logo)
alphabets =[
'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
           ]


def cipher(text, shift_amount, direction):
  encrypted_text = ""
  direction_dict = {1:"encode", 2:"decode"}
  #Encode here
  if direction_dict[direction] == "encode":
    shift_amount = shift_amount
  elif direction_dict[direction] == "decode":
    shift_amount *= -1
  else:
    pass
    
  for x in text:
    x = x.lower()
    if x in alphabets:
      position = alphabets.index(x)
      shift_position = position + shift_amount
      if shift_position > 26 or shift_position < 26:
        # Check if shift_amount is perfectly divided.
        r_char = alphabets[shift_position%26]
        encrypted_text += r_char
      else:
        r_char = alphabets[shift_position]
        encrypted_text += r_char
    else:
      encrypted_text += x
  

  print(f"{text} was encode to {encrypted_text}")

start = False

while not start:
  plain_text = input("Enter your plain text: ")
  shift = int(input("Enter a shift number: "))
  direction = int(input("1. Encode \n2. Decode \n"))
  cipher(text=plain_text, shift_amount=shift,direction=direction)

  restart = input("Yes - Restart \nNo - Exit \n")
  if restart.lower() == "no":
    start = True
    print("Thank you for using my Caesar Cipher App")