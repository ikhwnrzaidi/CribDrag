from pickle import TRUE

BITS = ('0', '1')
ASCII_BITS = 7

def display_bits(b):
    """convert list of {0, 1}* to string"""
    return ''.join([BITS[e] for e in b])

def seq_to_bits(seq):
    return [0 if b == '0' else 1 for b in seq]

def pad_bits(bits, pad):
    """pads seq with leading 0s up to length of pad"""
    assert len(bits) <= pad
    return [0] * (pad - len(bits)) + bits

def convert_to_bits(n):
    """convert an integer 'n' to bit array"""
    result = []
    if n == 0:
        return [0]
    while n > 0:
        result = [(n % 2)] + result
        n = int(n / 2)
    return result

def string_to_bits(s):
    def char_to_bit(c):
        return pad_bits(convert_to_bits(ord(c)), ASCII_BITS)
    return [b for group in
            map(char_to_bit, s)
            for b in group]

def bits_to_char(b):
    assert len(b) == ASCII_BITS
    value = 0
    for e in b:
        value = (value * 2) + e
    return chr(value)

def list_to_string(p):
    return ''.join(p)

def bits_to_string(b):
    return ''.join([bits_to_char(b[i:i + ASCII_BITS])
                    for i in range(0, len(b), ASCII_BITS)])

def otp(m, k):
    assert len(m) == len(k)
    return [(mm + kk) % 2 for mm, kk in zip(m, k)]

def XOR(A, B):
    return ''.join([chr(x ^ y) for x, y in zip(bytes(A, 'ascii'), bytes(B, 'ascii'))])

def crib_drag(text, c):
    for i in range(0, len(text) - len(c) + 1):
        pt = text[i:(i + len(c))]
        print("\t{0}:{1}".format(i,XOR(pt,c)))


######################### ENCRYPTION ####################################
print("\n")
print("***ENCRYPTION***")

k = string_to_bits("country")

M1 = string_to_bits("germany")
M2 = string_to_bits("denmark")

C1 = otp(M1, k)
C2 = otp(M2, k)

C1C2 = otp(C1, C2)

print("Key: " + str(k))
print("\n")

#Encryption of Message 1
print("Message 1: Germany")
print("Message 1: " + str(M1))
print("Ciphertext 1: " + str(C1))
print("\n")

#Encryption of Message 2
print("Message 2: Denmark")
print("Message 2: " + str(M2))
print("Ciphertext 2: " + str(C2))
print("\n")

#C1 and C2
print("Ciphertext 1: " + str(C1))
print("Ciphertext 2: " + str(C2))
print("C1 XOR C2: " + str(C1C2))
print("\n")


######################### DECRYPTION ####################################
print("***DECRYPTION***")

C1 = XOR("germany", "country")
C2 = XOR("denmark", "country")
C1C2 = XOR("germany", "denmark")

while(TRUE):
    print("Try some letters that may be in your messages (Hint: country with 7 letter words)")
    guess = input()
    crib_drag(C1C2, guess)