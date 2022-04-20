import base64
import pwn

'''
KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf
'''


k1_hex = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
k1_bytes = bytes.fromhex(k1_hex)
#print('k1_bytes: ', k1_bytes)

k2k3_hex = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
k2k3_bytes = bytes.fromhex(k2k3_hex)
#print('k2k3_bytes: ', k2k3_bytes)

k1k2k3_bytes = pwn.xor(k1_bytes, k2k3_bytes)
#print('k1k2k3_bytes: ', k1k2k3_bytes)

flagk1k2k3_hex = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'
flagk1k2k3_bytes = bytes.fromhex(flagk1k2k3_hex)
#print('flagk1k2k3_bytes', flagk1k2k3_bytes)

flag_bytes = pwn.xor(k1k2k3_bytes, flagk1k2k3_bytes)
print('flag_bytes', flag_bytes)

#########################################################
'''
For the next few challenges, you'll use what you've just learned to solve some more XOR puzzles.

I've hidden some data using XOR with a single byte, but that byte is a secret. Don't forget to decode from hex first.

73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d

'''

hz_hex = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
hz_bytes = bytes.fromhex(hz_hex)
print('hz_bytes' ,hz_bytes)

for i in range(256):
    text = pwn.xor(i, hz_bytes)
    if text.startswith(b'crypto'):
        print(text)


###########################################################################

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