import hashlib

input = "This is a message sent by a computer user."

output = hashlib.md5(input.encode())

print(f"Hash of the input string: {output.hexdigest()}")
