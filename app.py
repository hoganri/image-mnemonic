import os
import binascii
import hashlib
import unicodedata
import base64
import random
import sys

# Process image as base64
def get_base64_encoded_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

# Get base64 of image
r = get_base64_encoded_image(sys.argv[1])
r = base64.b64decode(r).hex()
rLength = len(r)
newRand = ''
i = 0
while i < 64:
    newRand += r[random.randrange(0,rLength)]
    i += 1

random_bin = binascii.unhexlify(newRand) # random in bin
random_hex = binascii.hexlify(random_bin) # random in hex
bytes = len(random_bin)
hashed_sha256 = hashlib.sha256(random_bin).hexdigest()

bin_result = (
    bin(int(random_hex, 16))[2:].zfill(bytes * 8)
    + bin(int(hashed_sha256, 16))[2:].zfill(256)[: bytes * 8 // 32]
)
print("BINARY: " + str(bin_result))

index_list = []
with open("english.txt", "r", encoding="utf-8") as f:
    for w in f.readlines():
        index_list.append(w.strip())

wordlist = []
for i in range(len(bin_result) // 11):
    index = int(bin_result[i*11 : (i+1)*11], 2)
    wordlist.append(index_list[index])

phrase = " ".join(wordlist)
print("PHRASE: " + phrase)