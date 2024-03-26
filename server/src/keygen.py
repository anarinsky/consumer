import nacl.signing
import nacl.encoding

# Generate a new random signing key
signing_key = nacl.signing.SigningKey.generate()

# Obtain the verify key for a given signing key
verify_key = signing_key.verify_key

# Serialize the signing and verify keys to hexadecimal for storage or transmission
signing_key_hex = signing_key.encode(encoder=nacl.encoding.HexEncoder).decode()
verify_key_hex = verify_key.encode(encoder=nacl.encoding.HexEncoder).decode()

print("Signing Key (Private):", signing_key_hex)
print("Verify Key (Public):", verify_key_hex)