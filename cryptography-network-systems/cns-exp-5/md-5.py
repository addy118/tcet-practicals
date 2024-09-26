import hashlib

input = "This is the message to be encoded."

md5 = hashlib.md5(input.encode())
sha1 = hashlib.sha1(input.encode())

print(f"Hash of the input string: {md5.hexdigest()}")
print(f"Hash of the input string: {sha1.hexdigest()}")
 