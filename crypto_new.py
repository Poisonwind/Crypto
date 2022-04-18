import pwn


'''
I've encrypted the flag with my secret key, you'll never be able to guess it.
flag is like crypto{...}
'''

hz_hex = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
hz_bytes = bytes.fromhex(hz_hex)

flag_start_bytes = b'crypto{'
flag_end_bytes = b'}'

key_part1_b = pwn.xor(flag_start_bytes, hz_bytes[:7])
print('key_part1_b',  key_part1_b)

key_part2_b = pwn.xor(flag_end_bytes, hz_bytes[-1])
print('key_part2_b',  key_part2_b)

key = key_part1_b+key_part2_b
print('key', key)

flag = pwn.xor(key, hz_bytes)
print('flag', flag)






