
from cryptography.fernet import Fernet
# key = Fernet.generate_key() #Generating the key 
key = b'2Bsy_jRLsVXTc-QanwydVLp0urIl8rBR0voFiLmX4wY=' 
#Save is carefully without this we cannot decrypt
cipher_suite = Fernet(key)
#Given password string encrypted using the KEY generated above
# ciphered_text = cipher_suite.encrypt(b"My@TestPass")   



print(ciphered_text)

from cryptography.fernet import Fernet
key = b'2Bsy_jRLsVXTc-QanwydVLp0urIl8rBR0voFiLmX4wY='
cipher_suite = Fernet(key)
# Decrypting the following encrypted content for the above given password to text format back
ciphered_text = b'gAAAAABlO04QcAEIF8fa_aqUfIABqnWvhBZ6mZMKDmtWYnC1_tc3ZOcngh6sFgrGo3YDhRfMv4oexDGoNEL4incAgLU9-w5V5g=='
unciphered_text = (cipher_suite.decrypt(ciphered_text))
print(unciphered_text)