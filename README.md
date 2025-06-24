# 🧬 ChenYanXi - 多层加密与高级免杀壳生成器

> 👤 作者：Mingshenhk
> 📌 项目用途：安全研究 / 加密实验 / 壳体开发  
> ⚠️ **免责声明：本项目仅供学习与科研用途，禁止用于任何非法用途，否则后果自负！**

---

## 📖 项目简介

**ChenYanXi** 是一个基于 Python 的高级壳体生成框架，专为研究加密混淆、防沙箱分析、内存加载执行等核心技术而设计。它允许用户将任意二进制文件（如 `.elf`、`.exe`、shellcode）进行**多层加密封装**，并自动生成一个带有反调试、自保护与内存执行能力的 Python 壳体脚本。

本项目集成了动态密钥派生、AES/DES 随机多层加密、字符串与控制流混淆、虚拟机与调试器检测、注册表伪装驻留、无文件内存执行等机制，旨在帮助安全研究人员深入理解现代高级持久化机制（APT）与免杀壳设计。

---

## ✨ 功能特性

| 功能模块 | 描述 |
|----------|------|
| 🔐 多层压缩 + 加密 | 每层使用 `zlib` 压缩 + 随机 AES / DES 加密，最多支持 8 层嵌套 |
| 🔑 动态密钥派生 | 使用 `PBKDF2-HMAC-SHA256` 从主密钥 + 盐派生加密密钥与 IV |
| 🌀 控制流混淆 | 自动注入虚假控制流语句，扰乱静态分析与逆向工程 |
| 🧱 字符串混淆 | 所有关键字符串以 `chr(x)` 拼接，防止特征提取与静态匹配 |
| 🔎 沙箱与调试检测 | 自动检测 VirtualBox、VMware、QEMU 等虚拟机环境与调试器 |
| 🗂️ 注册表伪装 | 模拟写入注册表启动项，提升隐蔽性（非真实驻留） |
| 🧬 内存加载执行 | 使用 `VirtualAlloc` + `CreateThread` 实现无文件内存执行 |

---

## ⚙️ 技术原理

### 🔐 多层加密封装

每一层处理逻辑如下：

1. `zlib` 压缩原始数据  
2. 添加特征干扰字节（如 `\x00\xFF`）  
3. 随机选择 `AES` 或 `DES` 进行对称加密（CBC 模式）  
4. 最终通过 `Base64` 编码封装  

默认层数为 8 层，形成洋葱式加密结构，极大提升逆向难度。

---

### 🔑 密钥派生机制

项目使用如下方式动态生成每个用户独立的加密密钥：

```python
hashlib.pbkdf2_hmac("sha256", secret, salt, 100000, dklen)
````

* `secret` 和 `salt` 由 `get_random_bytes()` 生成
* 每一层加密对应独立密钥与 IV，避免特征复用

---

### 🌀 混淆与干扰设计

#### 控制流混淆：

在壳体代码中插入如下伪代码：

```python
if random.random() < 0.99: pass  # control flow noise
```

用于扰乱程序流程图，迷惑静态分析器。

#### 字符串混淆：

将注册表路径等关键字改写为：

```python
chr(83)+chr(111)+chr(102)+chr(116)+...
```

避免字符串特征被静态识别或规则拦截。

---

### 🔍 反沙箱与反调试机制

内置以下检测逻辑：

```python
def is_debugged(): return ctypes.windll.kernel32.IsDebuggerPresent()
def is_vm(): return any(x in platform.platform().lower() for x in ["vbox", "vmware", "qemu", "sandbox"])
```

若检测到调试器或虚拟环境，程序会直接终止。

---

### 🧬 无文件内存执行

解密后的 payload 会通过如下方式直接注入内存执行：

```python
ptr = VirtualAlloc(...)
RtlMoveMemory(ptr, payload, ...)
CreateThread(..., ptr, ...)
```

此过程完全不依赖磁盘落地，有效绕过文件查杀。

---

## 🚀 使用方法

准备一个任意格式的二进制 Payload（如 shellcode、elf 文件等），命名为 `shell.elf`，然后运行主程序：

```bash
python chenyanxi.py
```

运行完成后，将自动生成带壳体的 Python 文件：`ultra_shell.py`

---

## 📁 项目结构

```
chenyanxi/
├── chenyanxi.py           # 主加壳生成器
├── shell.elf              # 示例 payload（自行替换）
├── ultra_shell.py         # 输出的免杀壳体脚本
└── README.md              # 项目文档（即本文件）

当然，也有可以生成到dist和build目录里！

```
<img src="images/Screenshot 2025-06-24 185736.png" width="600"/>
<img src="images/Screenshot 2025-06-24 185656.png" width="600"/>
---

## 📌 注意事项

* 壳体生成过程依赖 `pycryptodome` 模块，请先执行：

  ```bash
  pip install pycryptodome
  ```
* 脚本默认生成 Windows 平台使用的壳体，如需兼容 Linux，可修改 `winreg` 与 `ctypes` 相关部分；
* 加壳结果可配合 `pyarmor`、`nuitka`、`obfuscator-llvm` 等工具进一步加固。

---

## 📢 免责声明

> **本项目仅供学习、教学、研究与合法授权测试使用。任何利用本工具从事非法行为的后果由使用者自行承担，作者不承担任何法律责任。**

---

## ⭐ 鸣谢与参考

* [PyCryptoDome](https://github.com/Legrandin/pycryptodome)
* [Metasploit Framework](https://github.com/rapid7/metasploit-framework)
* [Veil Framework](https://github.com/Veil-Framework/Veil)
* 各类关于反沙箱、加密壳与控制流混淆的研究论文与实践

---

## ❤️ 支持本项目

如果你觉得本项目对你有帮助，请点个 ⭐Star 支持我！
欢迎 Fork / Issue / PR，共同完善本项目！

```
