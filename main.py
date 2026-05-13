import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Util.Padding import pad
import sys

def decrypt_file(input_path, output_path, key_str):
    with open(input_path, 'r', encoding='utf-8') as f:
        base64_data = f.read().strip()
    
    encrypted_bytes = base64.b64decode(base64_data)
    
    key_bytes = key_str.encode('utf-8')
    iv = b'\x00' * 16
    
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    decrypted_bytes = unpad(cipher.decrypt(encrypted_bytes), AES.block_size)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(decrypted_bytes.decode('utf-8'))
        
    print(f"Done: {output_path}")

def encrypt_file(input_json_path, output_sav_path, key_str):
    with open(input_json_path, 'r', encoding='utf-8') as f:
        json_data = f.read()
    
    input_bytes = json_data.encode('utf-8')
    
    key_bytes = key_str.encode('utf-8')
    iv = b'\x00' * 16
    
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    padded_bytes = pad(input_bytes, AES.block_size)
    
    encrypted_bytes = cipher.encrypt(padded_bytes)
    
    base64_data = base64.b64encode(encrypted_bytes).decode('utf-8')
    
    with open(output_sav_path, 'w', encoding='utf-8') as f:
        f.write(base64_data)
        
    print(f"Done: {output_sav_path}")

KEY = "54c35c94b65d837d9e8f77ddc6376439"

if __name__ == "__main__":
    mode = input("Enter mode (encrypt, decrypt):\n=>")
    if mode in ("encrypt", "decrypt"):
        path = input("Enter path:\n=>")
    else:
        print("Bad option")
        sys.exit(0)
    if mode == "decrypt":
        try:
            decrypt_file(path, f"{''.join(list(path)[:-4])}_decrypted.sav", KEY)
        except Exception as e:
            print(f"ERROR: {e}")
    else:
        try:
            encrypt_file(path, f"{''.join(list(path)[:-4])}_encrypted.sav", KEY)
        except Exception as e:
            print(f"ERROR: {e}")
