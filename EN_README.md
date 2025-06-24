# 🧬 ChenYanXi - Multi-layer Encryption & Advanced Evasion Shell Generator

> 👤 Author: Mingshenhk  
> 📌 Purpose: Security Research / Encryption Experimentation / Shell Generator Development  
> ⚠️ **Disclaimer: This project is for educational and research purposes only. Do NOT use it for any illegal activities. Use at your own risk.**

---

## 📖 Project Overview

**ChenYanXi** is an advanced Python-based shell generator framework designed for studying key techniques in encryption obfuscation, sandbox evasion, and in-memory payload execution. It allows users to wrap arbitrary binary files (e.g., `.elf`, `.exe`, shellcode) in a **multi-layer encryption shell**, and automatically generate a Python script capable of anti-debugging, self-protection, and in-memory execution.

This project integrates features such as dynamic key derivation, AES/DES randomized multi-layer encryption, string/control flow obfuscation, virtual machine and debugger detection, registry-based stealth, and fileless execution. It aims to help security researchers understand modern Advanced Persistent Threat (APT) persistence techniques and evasive shell design.

---

## ✨ Key Features

| Module | Description |
|--------|-------------|
| 🔐 Multi-layer Compression + Encryption | Each layer uses `zlib` compression + random AES/DES encryption, supporting up to 8 nested layers |
| 🔑 Dynamic Key Derivation | Uses `PBKDF2-HMAC-SHA256` to derive keys and IVs from a master secret and salt |
| 🌀 Control Flow Obfuscation | Injects fake control flow logic to disrupt static analysis and reverse engineering |
| 🧱 String Obfuscation | Encodes all critical strings using `chr(x)` to evade signature matching |
| 🔎 Sandbox and Debugger Detection | Automatically detects VirtualBox, VMware, QEMU, and common debugger indicators |
| 🗂️ Registry Stealth | Simulates writing startup keys to Windows Registry (not real persistence) |
| 🧬 In-Memory Execution | Executes decrypted payload using `VirtualAlloc` + `CreateThread` without writing to disk |

---

## ⚙️ Technical Details

### 🔐 Multi-layer Encryption

Each processing layer includes:

1. Compressing raw data with `zlib`  
2. Appending fake data bytes (e.g., `\x00\xFF`)  
3. Randomly choosing AES or DES (CBC mode) for encryption  
4. Base64 encoding the result  

Up to 8 encryption layers are supported, forming an onion-style structure that significantly increases reverse-engineering complexity.

---

### 🔑 Key Derivation

Keys and IVs are derived per layer using:

```python
hashlib.pbkdf2_hmac("sha256", secret, salt, 100000, dklen)
````

* `secret` and `salt` are randomly generated using `get_random_bytes()`
* Each layer has a unique derived key and IV to prevent reuse or detection

---

### 🌀 Obfuscation Design

#### Control Flow Obfuscation

Fake logic like the following is inserted:

```python
if random.random() < 0.99: pass  # control flow noise
```

This disrupts the control flow graph and confuses static analysis tools.

#### String Obfuscation

Critical strings such as registry paths are converted to:

```python
chr(83)+chr(111)+chr(102)+chr(116)+...
```

Avoids being flagged by static signatures or rules.

---

### 🔍 Anti-Sandbox & Anti-Debugging

The following logic is embedded to detect sandboxed or analyzed environments:

```python
def is_debugged(): return ctypes.windll.kernel32.IsDebuggerPresent()
def is_vm(): return any(x in platform.platform().lower() for x in ["vbox", "vmware", "qemu", "sandbox"])
```

If such conditions are detected, the shell exits immediately.

---

### 🧬 Fileless In-Memory Execution

After decrypting the payload, it is directly injected into memory via:

```python
ptr = VirtualAlloc(...)
RtlMoveMemory(ptr, payload, ...)
CreateThread(..., ptr, ...)
```

This ensures fileless execution, avoiding disk-based detection and AV scanning.

---

## 🚀 Usage

Prepare any binary payload (e.g., shellcode, ELF file) and name it `shell.elf`. Then run the main generator:

```bash
python chenyanxi.py
```

After execution, a Python script named `ultra_shell.py` will be generated, containing the fully obfuscated and encrypted shell.

---

## 📁 Project Structure

```
chenyanxi/
├── chenyanxi.py           # Main shell packer script
├── shell.elf              # Example payload (replace with your own)
├── ultra_shell.py         # Output Python shell script with layered encryption
└── README.md              # This documentation file

Optionally, the shell can also be compiled into `dist/` or `build/` directories using packers.
```

---

## 📌 Notes

* The script requires the `pycryptodome` module. Install it with:

  ```bash
  pip install pycryptodome
  ```

* The output shell is designed for **Windows** by default. To adapt for Linux, modify `winreg`, `ctypes`, and related logic accordingly.

* For enhanced evasion, use `pyarmor`, `nuitka`, or `obfuscator-llvm` to compile and obfuscate the generated shell script.

---

## 📢 Disclaimer

> **This project is intended for educational, academic, and authorized security research only. Misuse of this tool for illegal purposes is strictly forbidden. The author assumes no responsibility for any misuse or damages caused.**

---

## ⭐ Acknowledgements & References

* [PyCryptoDome](https://github.com/Legrandin/pycryptodome)
* [Metasploit Framework](https://github.com/rapid7/metasploit-framework)
* [Veil Framework](https://github.com/Veil-Framework/Veil)
* Research papers and tools on sandbox evasion, encryption shells, and control flow obfuscation

---

## ❤️ Support This Project

If you find this project useful, please give it a ⭐Star!
Feel free to Fork / Open Issues / Submit PRs to improve it together!

```


