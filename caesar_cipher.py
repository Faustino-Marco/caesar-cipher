### Need access to Corpus of some kind


# chars = [0...9]


from asyncio.proactor_events import _ProactorBaseWritePipeTransport


def encrypt(plain, shift):
  """
  Function that takes in a plain text phrase and a numeric shift.

  - The phrase will then be shifted that many letters.
    - E.g. encrypt(‘abc’,1) would return ‘bcd’. = E.g. - encrypt  (‘abc’, 10) would return ‘klm’.

  - Shifts that exceed 26 should wrap around.
    - E.g. encrypt(‘abc’,27) would return ‘bcd’.

  - Shifts that push a letter out of range should wrap around.
    - E.g. encrypt('zzz', 1) would return 'aaa'.
  """
  encrypted = ""
  for char in plain:
    num = ord(char)
    print("plain char: ", char)

    if ord(char) in range(65, 90):
      shifted_num = ((num + (shift - 65)) % 26 + 65)
      print("original: ", ord(char))
      print("shifted: ", shifted_num)
      encrypted += str(chr(shifted_num))
      print("progress: ", encrypted) 

    if ord(char) in range(97, 123):
      shifted_num = ((num + (shift - 97)) % 26 + 97)
      print("original: ", ord(char))
      print("shifted: ", shifted_num)
      encrypted += str(chr(shifted_num))
      print("progress: ", encrypted)

  return encrypted
  
  ####### convert alpha chars (letters) into numeric form
  # search for python "ord" fn() for letter -> num
  # "chr" fn() for num -> letter

  # different mod
  # handle upper/lower

  # return plain + " coming soon"

def decrypt(cipher, shift):
  """
  Function that takes in encrypted text and numeric shift which will restore the encrypted text back to its original form when correct key is supplied.
  """
  # return cipher + " coming soon"
  return encrypt(cipher, -shift)


def crack(code):
  """
  Function that will decode the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.

  Devise a method for the computer to determine if code was broken with minimal human guidance.
  """
  encrypted = ""
  for char in code:
    num = ord(char)
    print("code char: ", char)

    if num in range(65, 90):
      shifted_num = ((num + (shift - 65)) % 26 + 65)
      print("original: ", ord(char))
      print("shifted: ", shifted_num)
      encrypted += str(chr(shifted_num))
      print("progress: ", encrypted) 

    if ord(char) in range(97, 123):
      shifted_num = ((num + (shift - 97)) % 26 + 97)
      print("original: ", ord(char))
      print("shifted: ", shifted_num)
      encrypted += str(chr(shifted_num))
      print("progress: ", encrypted)

  return encrypted


if __name__ == "__main__":
  pins = []
  assert 1 + 1 == 2
  assert ord('A') == 65
  assert encrypt('A', 5) == 'F'
  assert encrypt('z', 9) == 'i'

print(encrypt("zebra", 9))