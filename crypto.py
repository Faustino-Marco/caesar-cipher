


# chars = [0...9]


def encrypt(plain, shift):
  encrypted = ""
  for char in plain:
    num = int(char)
    shifted_num = (num + shift) % 10 # must be 0-9
    encrypted += str(shifted_num)

  return encrypted
  
  ####### convert alpha chars (letters) into numeric form
  # search for python "ord" fn() for letter -> num
  # "chr" fn() for num -> letter

  # different mod
  # handle upper/lower

  # return plain + " coming soon"

def decrypt(cipher, shift):
  """"""
  # return cipher + " coming soon"
  return encrypt(cipher, -shift)

if __name__ == "__main__":
  pins = []