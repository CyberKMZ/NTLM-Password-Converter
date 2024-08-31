import hashlib,binascii
import argparse

parser=argparse.ArgumentParser(description="ntlm password converter")

parser.add_argument('-password',type=str,required=True,help="The plain-text password")

args=parser.parse_args()
password=args.password

hash=hashlib.new('md4',password.encode('utf-16le')).digest()
print(binascii.hexlify(hash))
