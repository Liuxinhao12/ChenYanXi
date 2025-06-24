# 🧬 ChenYanXi · Advanced Multi-layer Encrypted AV-Evasion Shell Generator

> 👤 Author: **Mingshenhk**
> 🎯 Purpose: Security Research / Obfuscation Experiments / AV-Evasion Testing
> ⚠️ **Disclaimer: This tool is strictly for educational and authorized testing purposes only. Illegal use is strictly prohibited!**

---

## 📖 Project Overview

**ChenYanXi** is an advanced shell wrapper generation framework built with Python, designed for security researchers and red team operators. It integrates cutting-edge techniques such as **multi-layer dynamic encryption**, **control flow obfuscation**, **anti-sandbox detection**, and **fileless in-memory execution**.

It can wrap any binary payload (e.g., `.elf`, `.exe`, raw shellcode) into a highly obfuscated Python script with **strong anti-analysis, minimal detection rate**, and **cross-platform adaptability**. The output can be further compiled into a stealthy standalone binary using **Nuitka**.

---

## ✨ Features

| Module                                      | Description                                                       |
| ------------------------------------------- | ----------------------------------------------------------------- |
| 🔐 **Multi-layer Encryption + Compression** | Supports up to 8 layers of combined `zlib` + AES/DES encryption   |
| 🔑 **Dynamic Key Derivation**               | Uses `PBKDF2-HMAC-SHA256` with salt for layer-wise key derivation |
| 🌀 **Control Flow Obfuscation**             | Injects decoy control flow to confuse static analysis             |
| 🔎 **Anti-Sandbox / Anti-Debug**            | Detects VMs and debuggers, terminates on detection                |
| 🧱 **String Obfuscation**                   | Encodes sensitive strings via `chr()` concatenation               |
| 🧬 **In-Memory Execution**                  | Executes entirely in RAM, avoids file I/O                         |
| 🗂️ **Registry Persistence Simulation**     | Fakes autorun entries without actual registry writing             |

---

## ⚙️ Technical Details

### 🔐 Multi-layer Encryption Logic

Each encryption layer performs the following:

1. Compresses original data using `zlib`
2. Inserts fake bytes (e.g., `\x00\xFF`) for signature pollution
3. Randomly selects **AES** or **DES** (CBC mode) for encryption
4. Wraps the result with Base64 encoding

With up to **8 nested layers**, the structure becomes onion-like, significantly increasing reverse engineering difficulty.

---

### 🔑 Key Derivation Mechanism

Each layer uses a unique key and IV, derived as follows:

```python
hashlib.pbkdf2_hmac("sha256", secret, salt, 100000, dklen=32)
```

* Both `secret` and `salt` are generated using `get_random_bytes()`
* Prevents key reuse and avoids static detection patterns

---

### 🌀 Obfuscation Examples

**Control flow noise injection:**

```python
if random.random() < 0.99:
    pass  # Noise
```

**String obfuscation (e.g., for registry path):**

```python
reg_key = chr(83)+chr(111)+chr(102)+chr(116)+...
```

---

### 🔍 Sandbox / Debugger Detection

```python
def is_debugged():
    return ctypes.windll.kernel32.IsDebuggerPresent()

def is_vm():
    return any(x in platform.platform().lower() for x in ["vbox", "vmware", "qemu", "sandbox"])
```

On detection, execution is immediately terminated.

---

### 🧬 In-Memory Execution (Windows)

```python
ptr = VirtualAlloc(...)
RtlMoveMemory(ptr, payload, ...)
CreateThread(..., ptr, ...)
```

* Runs entirely in memory
* Avoids touching disk, bypasses most AV scanning engines

---

## 🚀 Usage Guide

1. Prepare your binary payload (e.g., raw shellcode, `.elf`, `.exe`), and name it:

   ```
   shell.elf
   ```

2. Run the main shell generator:

   ```bash
   python chenyanxi.py
   ```

3. The output will be a fully obfuscated Python payload script:

   ```
   ultra_shell.py
   ```

---

## 🧰 Project Structure

```
chenyanxi/
├── chenyanxi.py           # Main wrapper generator
├── shell.elf              # Example binary payload
├── ultra_shell.py         # Final obfuscated Python shell
├── image/                 # Screenshot directory
└── README.md              # This documentation
```

---

## 🧪 Packaging (Nuitka + UPX)

### Install dependencies:

```bash
sudo apt update
sudo apt install patchelf upx makeself
```

### Compile with Nuitka:

```bash
nuitka --follow-imports --standalone ultra_shell.py
```

### Strip and compress output binary:

```bash
strip ultra_shell.dist/ultra_shell.bin
upx -9 ultra_shell.dist/ultra_shell.bin
```

### Create self-extracting onefile binary:

```bash
sudo apt install makeself
makeself --nox11 ultra_shell.dist/ ultra_shell.run "Ultra Shell Installer" ./ultra_shell.bin
```

### Final output:

```
ultra_shell.run  ← Standalone executable with in-memory payload
```
result:

<img src="image/Screenshot 2025-06-24 185736.png" width="600"/>  
<img src="image/Screenshot 2025-06-24 185655.png" width="600"/>

Alternatively, you **can** use PyInstaller (not recommended):

```
pyinstaller --onefile ultra_shell.py
```


<img src="image/Screenshot 2025-06-24 185736.png" width="600"/> 
<img src="image/Screenshot 2025-06-24 185656.png" width="600"/>

---

## 📌 Notes

* This project requires the `pycryptodome` package:

  ```bash
  pip install pycryptodome
  ```

* Default shell is Windows-compatible (uses `winreg`, `ctypes.windll`),
  for Linux compatibility, manually adapt platform-specific code.

* Consider combining with `pyarmor`, `obfuscator-llvm`, or other obfuscation tools for maximum stealth.

---

## 📢 Disclaimer

> This project is strictly for educational, authorized testing, and research purposes only.
> Any misuse is the sole responsibility of the user. The author assumes no liability for any consequences.

---

## ⭐ Credits & References

* [PyCryptodome](https://github.com/Legrandin/pycryptodome) - Cryptographic primitives
* [Metasploit Framework](https://github.com/rapid7/metasploit-framework)
* [Veil Framework](https://github.com/Veil-Framework/Veil)
* Academic & practical research on APT memory shells, obfuscation, and anti-analysis

---

## ❤️ Support This Project

If you found this project helpful, please consider giving it a ⭐Star!
Forks, Issues, and PRs are welcome to help improve and evolve the project.


