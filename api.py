access_key = ""
secret_key = ""

file_key = open("keys.txt",'r')

access_key= file_key.readline().strip("\n")
secret_key= file_key.readline().strip("\n")

print(f"access:{access_key},secret:{secret_key}")
