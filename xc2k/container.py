import bitstring

def revbits8(n):
    return int('{:08b}'.format(n)[::-1], 2)

def revbits4(n):
    return int('{:04b}'.format(n)[::-1], 2)

def revnib(n):
    return ((n & 0xF) << 4) | ((n >> 4) & 0xF)

def munge(n):
    return (revbits4(n & 0xF) << 4) | revbits4((n >> 4) & 0xF)

def getbits_bin(f):
    return bitstring.ConstBitStream(bytes=f.read())

def getbits_bit(f):
    # bit w/ header
    buff = f.read()
    buff = buff[0x76:]
    return bitstring.ConstBitStream(bytes=buff)

def getbits_rom(f):
    # random rom file they gave me
    buff = bytearray()
    for b in f.read():
        # Reverse bits, swap nibbles
        buff += chr(munge(ord(b)))
    return bitstring.ConstBitStream(bytes=buff)

def getbits(f, format='bit'):
    bits = {
        'bin': getbits_bin,
        'bit': getbits_bit,
        'rom': getbits_rom,
        }[format](f)
    return bits