# PYTHON_NUMBER = 3531
# MAGIC_NUMBER = (PYTHON_NUMBER).to_bytes(2, 'little') + b'\r\n'
# _RAW_MAGIC_NUMBER = int.from_bytes(MAGIC_NUMBER, 'little')
# hex_value = hex(_RAW_MAGIC_NUMBER)      # 转换为16进制
# hex_value_without_prefix = hex_value[2:]    # 去除0x前缀
# bit_len = len(hex_value_without_prefix)
# hex_len = bit_len % 2 + bit_len
# magic_number_hex = hex_value.replace('0x','').zfill(hex_len).upper()
# print(magic_number_hex)


import importlib.util
print(importlib.util.MAGIC_NUMBER.hex())  # 输出十六进制
print(int(importlib.util.MAGIC_NUMBER.hex(), 16))  # 转换为十进制