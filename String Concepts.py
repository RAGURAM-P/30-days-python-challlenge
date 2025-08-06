#String creation
name="oh god beautiful"
line="This is the nature of beautiful"
#multiline
quote="""Oh dare devil"""
#length
print(len(name))
#index
print(name[3])
#slicing
print(name[0:7])
#negative index
print(quote[-1])
#loop
for char in line:
    print(char,end="")
#concatenation
quotes=(name+"life")
print("\n",quotes)
#repetation
print("life"*3)
#membership
print("z" in name)
print("i" in line)
#strip
print(name.strip())
#replace
print("oh god".replace("god","devil"))
#find
print(name.find("god"))
#count
print(line.count("of"))
#lower
print(name.lower())
#upper
print(name.upper())
#capitalize
print("money".capitalize())
#title
print("money is always expensive".title())
#split
print(name.split(","))
#swapcase
print(quote.swapcase())
#endswith
print("thank".endswith("you"))
#startswith
print("you will".startswith("you"))
#zfill
print("42".zfill(5))
#isalpha
print("Python3".isalpha())
print("Python".isalpha())
#isdigit
print("12345".isdigit())
#isalnum
print("abc123".isalnum())
#isspace
print("   ".isspace())
#isupper
print("HELLO".isupper())
#islower
print("Hello".islower())
#istitle
print("Love You".istitle())
#format
print("dare, {}!".format("devil"))
#f-string
age = 25
print(f"My name is {name} and I am {age} years old.")
#Escape Characters
print("She said, \"\nPython is fun!\"\nand left")
#Unicode
print("Smile 😊")
#Encoding
encoded = "tuple".encode("utf-7")
print(encoded)
#Decoding
print(encoded.decode("utf-8"))
#Join
words = ["julius", "caesar"]
print(" ".join(words))
#Partition
print("key=value".partition("="))
#rjust
print("42".rjust(5, '0'))
#ljust
print("42".ljust(5, '-'))
#center
print("42".center(7, '*'))
#format_map
data = {'name': 'Paiyan'}
print("Hello, {name}".format_map(data))
#casefold
print("hotel paradise".casefold())
#maketrans
trans = str.maketrans("aeiou", "12345")
print("education".translate(trans))
#translate
text = "thank you"
map_table = str.maketrans({"t": "T", "y": "Y"})
print(text.translate(map_table))

