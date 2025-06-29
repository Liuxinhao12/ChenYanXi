# 🧬 ChenYanXi· gāojí duō céng jiāmì miǎn shā ké shēngchéng qì > 👤 zuòzhě:**Mingshenhk** > 🎯 yòngtú: Ānquán yánjiū/ jiā ké shíyàn/ miǎn shā cèshì > ⚠️ **miǎnzé shēngmíng: Běn gōngjù jǐn xiàn jiàoxué yǔ shòuquán cèshì, jìnzhǐ yòng yú rènhé fēifǎ yòngtú!** --- ## 📖 Xiàngmù gàishù **ChenYanXi** shì yīgè zhuān wéi ānquán yánjiū rényuán yǔ hóng duì cèshì zhě shèjì de gāojí ké tǐ shēngchéng kuàngjià, jīyú Python shíxiàn, rónghé duō céng dòngtài jiāmì, kòngzhì liú rǎoluàn, xūnǐ jī jiǎncè, wú wénjiàn zhíxíng děng héxīn jìshù. Tā kěyǐ jiāng èrjìnzhì Payload(rú `.Elf`,`.Exe`) fēngzhuāng wèi fùzá de Python ké tǐ, jùbèi**qiáng kàng fēnxī nénglì, jí dī chá shā lǜ yǔ duō píngtái jiānróng xìng**, bìng kě tōngguò Nuitka jìnyībù shēngchéng gāodù yǐnnì de dān wénjiàn zhíxíng chéngxù. --- ## ✨ Gōngnéng tèxìng | mókuài | miáoshù | | ------------------ | ----------------------------------- | | 🔐**duō céng jiāmì + yāsuō** | zhīchí zuìduō 18 céng `zlib`+ AES/DES hùnhé jiāmì | | 🔑**dòngtài mì yào pàishēng** | shǐyòng `PBKDF2-HMAC-SHA256`jiā yán mì yào yǎnshēng, céng céng bùtóng | | 🌀**kòngzhì liú wèizhuāng** | zìdòng chārù wú hài fēnzhī, rǎoluàn chéngxù liúchéng fēnxī | | 🔎**fǎn shā xiāng/ fǎn tiáoshì/ fǎn zhuā bāo** | jiǎncè VM, tiáoshì qì, zhuā bāo qì, yīdàn mìngzhòng lìjí tuìchū | | 🧱**zìfú chuàn hùnxiáo** | suǒyǒu mǐngǎn zìfú chuàn `chr()`pīnjiē, duǒbì tèzhēng pǐpèi | | 🧬**nèicún jiāzài zhíxíng** | jǐn jiāzài jìn RAM, bìmiǎn luò pán, kàng shā ruǎn sǎomiáo | | 🗂️ **zhùcè biǎo wěi zhù liú (mónǐ)** | xūnǐ tiānjiā qǐdòng xiàng, wú zhēnshí xiě rù, míhuò fēnxī qì | --- ## ⚙️ jìshù yuánlǐ ### 🔐 duō céng jiāmì luójí měi céng zhí háng rúxià chu lǐ: 1. Yuánshǐ shùjù shǐyòng `zlib`yāsuō 2. Tiānjiā wèizhuāng zì jié gānrǎo tèzhēng shìbié 3. Suíjī shǐyòng AES huò DES(CBC) duìchèn jiāmì 4. Jiāmì jiéguǒ zài Base64 fēngzhuāng duō dá**zuìduō 18 céng qiàn tào shì chǔlǐ**, gòujiàn “yángcōng ké”, jí nán nìxiàng. --- ### 🔑 Mì yào pàishēng shèjì měi céng shǐyòng dúlì mì yào yǔ IV, pàishēng fāngshì: ```Python hashlib.Pbkdf2_hmac("sha256", secret, salt, 100000, dklen=32) ``` * `secret`yǔ `salt`jūn shǐyòng `get_random_bytes()`shēngchéng * fángzhǐ mì yào zhòngyòng yǔ jìngtài móshì shìbié --- ### 🌀 kòngzhì liú + zìfú chuàn hùnxiáo shìlì wèizhuāng kòngzhì liú yǔjù: ```Python if random.Random() < 0.99: Pass # kòngzhì liú zàoshēng ``` guānjiàn zìfú chuàn hùnxiáo (lìrú zhùcè biǎo lùjìng): ```Python reg_key = chr(83)+chr(111)+chr(102)+chr(116)+... ``` --- ### 🔍 Shā xiāng/ tiáoshì jiǎncè dàimǎ ```python def is_debugged(): Return ctypes.Windll.Kernel32.IsDebuggerPresent() def is_vm(): Return any(x in platform.Platform().Lower() for x in ["vbox", "vmware", "qemu", "sandbox"]) ``` rú mìngzhòng jiǎncè, lìjí zhōngzhǐ zhíxíng. --- ### 🧬 Nèicún jiāzài zhíxíng jīzhì (Windows) ```python ptr = VirtualAlloc(...) RtlMoveMemory(ptr, payload, ...) CreateThread(..., Ptr, ...) ``` * Quán guòchéng yùnxíng zài nèicún zhōng * bù luòdì wénjiàn, bì kāi dà duōshù shādú jiǎncè --- ## shǐyòng mìnglìng --- ``` usage: Chenyanxi.Exe [-h] [-l LAYERS] [--no-drop] payload OR usage:./Chenyanxi [-h] [-l LAYERS] [--no-drop] payload positional arguments: Payload kě zhíxíng yǒuxiào fùzǎi de wénjiàn (lìrú,shell.Exe,shell.Elf) options: -H, --help show this help message and exit -l LAYERS, --layers LAYERS jiāmì céng (1-18), mòrèn shì 3 --no-drop jǐn zài nèicún zhōng yùnxíng ``` --- ## 🚀 shǐyòng fāngfǎ 1. Zhǔnbèi yīgè èrjìnzhì Payload(rú `.Elf`,`.Exe`), mìngmíng wèi: ``` Shell.Elf shell.Exe ``` 2. Yùnxíng ké tǐ shēngchéng qì: ```Bash ./Chenyanxi -l 18 shell.Elf huòzhě chenyanxi.Exe -l 18 shell.Exe ``` 3. Shūchū jiéguǒ wèi miǎn shā ké tǐ jiǎoběn: ``` Packed_shell.Py ``` --- ## 🧰 xiàngmù jiégòu ``` chenyanxi/ ├── chenyanxi # zhǔ shēngchéng qì jiǎoběn ├── shell.Elf # shìlì Payload(èrjìnzhì) ├── shell.Exe ├── chenyanxi.Exe ├── ultra_shell.Py # shūchū dài ké Python mùmǎ ├── image/ # jiétú mùlù └── README.Md # běn wéndàng ``` --- ## 🧪 Windows dǎbāo jiànyì (Nuitka) ānzhuāng yīlài: ``` Pip install pycryptodome psutil nuitka ``` shǐyòng Nuitka dǎbāo: ``` Nuitka --mingw64 --standalone --onefile packed_shell.Py ``` zuìzhōng shūchū: ``` Packed_shell.Exe ``` --- ## 🧪 Linux dǎbāo jiànyì (Nuitka + UPX) ānzhuāng yīlài: ```Bash sudo apt update pip install nuitka pycryptodome psutil sudo apt install patchelf upx makeself ``` shǐyòng Nuitka dǎbāo: ```Bash nuitka --follow-imports --standalone --onefile packed_shell.Py ``` yāsuō zhǔ kě zhíxíng wénjiàn: ```Bash strip packed_shell.Dist/packed_shell.Bin upx -9 packed_shell.Dist/packed_shell.Bin ``` shēngchéng dān wénjiàn yùnxíng bāo: ```Bash sudo apt install makeself makeself --nox11 packed_shell.Dist/ packed_shell.Run"Packed Shell Installer" ./Packed_shell.Bin ``` zuìzhōng shūchū: ``` Packed_shell.Run ￩ kě zhíjiē zhíxíng, zìdòng jiěyā + jiāzài nèicún mùmǎ ``` jiéguǒ: <Img src="image/Screenshot 2025-06-24 185736.Png" width="600"/> <img src="image/Screenshot 2025-06-24 185655.Png" width="600"/> huòzhě win hé Linux kěyǐ shǐyòng pyinstaller(bù tuījiàn): ``` Pyinstaller --onefile packed_shell.Py ``` <img src="image/Screenshot 2025-06-24 185736.Png" width="600"/> <img src="image/Screenshot 2025-06-24 185656.Png" width="600"/> --- ## 📌 zhùyì shìxiàng * xiàngmù yīlài: ```Bash pip install pycryptodome psutil nuitka ``` * mòrèn zhēnduì Windows píngtái (bāohán `winreg`, `ctypes.Windll`), rú yòng yú Linux kěnéng yǒu yīxiē wèizhī de wèntí; * jiànyì dāpèi `pyarmor`,`obfuscator-llvm`děng gōngjù jìnyībù jiā ké hùnxiáo. --- ## 📢 Miǎnzé shēngmíng > běn xiàngmù jǐn gōng héfǎ shòuquán cèshì, jiàoxué yánjiū yòngtú. Jìnzhǐ jiāng běn gōngjù yòng yú rènhé fēifǎ xíngwéi, wéi zhě hòuguǒ zìfù, zuòzhě gài bù fùzé! --- ## ⭐ Míngxiè yǔ yǐnyòng * [PyCryptodome](https://Github.Com/Legrandin/pycryptodome) - gāojí jiāmì kù * [Metasploit Framework](https://Github.Com/rapid7/metasploit-framework) * [Veil Framework](https://Github.Com/Veil-Framework/Veil) * APT nèicún ké yánjiū wénxiàn, nìxiàng yǔ jiā ké jìshù yánjiū tuánduì --- ## ❤️ zhīchí xiàngmù rúguǒ nǐ juédé běn xiàngmù yǒu bāngzhù, qǐng diǎnjī ⭐Star zhīchí! Huānyíng Fork, tí Issue, tíjiāo PR yīqǐ wánshàn! ---
展开
4,333 / 5,000
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
发送反馈
复制
有翻译结果
