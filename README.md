# Paper Lily Save Manipulation

A set of Python scripts to decrypt and encrypt save files (`.sav`) for the game **Paper Lily - Chapter I**.

### Verified Version
* **Game Version:** v1.1.6 (Linux / Windows)

---

## Technical Details

The game encrypts its text-based JSON save files using the following cryptographic parameters:
* **Algorithm:** AES-256-CBC
* **Key Generation:** Standard UTF-8 byte array from a hardcoded 32-character MD5 string.
* **Initialization Vector (IV):** 16 zerobed bytes (`b'\x00' * 16`).
* **Padding:** PKCS7.
* **Output Format:** Base64-encoded string.
