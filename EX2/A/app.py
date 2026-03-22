P10 = [3,5,2,7,4,10,1,9,8,6]
P8  = [6,3,7,4,8,5,10,9]
IP  = [2,6,3,1,4,8,5,7]
IP_INV = [4,1,3,5,7,2,8,6]
EP  = [4,1,2,3,2,3,4,1]
P4  = [2,4,3,1]

S0 = [[1,0,3,2],
      [3,2,1,0],
      [0,2,1,3],
      [3,1,3,2]]
S1 = [[0,1,2,3],
      [2,0,1,3],
      [3,0,1,0],
      [2,1,0,3]]

def permute(bits, table):
    return "".join(bits[i-1] for i in table)

def shift(bits, n):
    return bits[n:] + bits[:n]

def xor(a, b):
    return "".join('0' if a[i]==b[i] else '1' for i in range(len(a)))

def encrypt(plain, key):

    print("\n===== KEY GENERATION =====")

    key_p10 = permute(key, P10)
    print("After P10:", key_p10)

    left = key_p10[:5]
    right = key_p10[5:]
    print("Left:", left, "Right:", right)

    # LS-1
    left = shift(left, 1)
    right = shift(right, 1)
    print("After LS-1 Left:", left, "Right:", right)

    K1 = permute(left + right, P8)
    print("K1:", K1)

    # LS-2
    left = shift(left, 2)
    right = shift(right, 2)
    print("After LS-2 Left:", left, "Right:", right)

    K2 = permute(left + right, P8)
    print("K2:", K2)

    print("\n===== ENCRYPTION =====")

    ip = permute(plain, IP)
    print("After IP:", ip)

    left = ip[:4]
    right = ip[4:]
    print("L0:", left, "R0:", right)

    # ROUND 1
    print("\n----- ROUND 1 -----")

    ep = permute(right, EP)
    print("After EP:", ep)

    xor1 = xor(ep, K1)
    print("After XOR with K1:", xor1)

    row = int(xor1[0] + xor1[3], 2)
    col = int(xor1[1] + xor1[2], 2)
    s0 = format(S0[row][col], '02b')

    row = int(xor1[4] + xor1[7], 2)
    col = int(xor1[5] + xor1[6], 2)
    s1 = format(S1[row][col], '02b')

    print("S0:", s0, "S1:", s1)

    p4 = permute(s0 + s1, P4)
    print("After P4:", p4)

    left = xor(left, p4)
    print("L1:", left)

    # SWAP
    left, right = right, left
    print("After Swap L:", left, "R:", right)

    # ROUND 2
    print("\n----- ROUND 2 -----")

    ep = permute(right, EP)
    print("After EP:", ep)

    xor2 = xor(ep, K2)
    print("After XOR with K2:", xor2)

    row = int(xor2[0] + xor2[3], 2)
    col = int(xor2[1] + xor2[2], 2)
    s0 = format(S0[row][col], '02b')

    row = int(xor2[4] + xor2[7], 2)
    col = int(xor2[5] + xor2[6], 2)
    s1 = format(S1[row][col], '02b')

    print("S0:", s0, "S1:", s1)

    p4 = permute(s0 + s1, P4)
    print("After P4:", p4)

    left = xor(left, p4)
    print("L2:", left)

    combined = left + right
    print("Before IP-1:", combined)

    cipher = permute(combined, IP_INV)
    print("\nFinal Cipher:", cipher)

    return cipher

while True:
    print("\n===== S-DES MENU =====")
    print("1. Encrypt")
    print("2. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        plain = input("Enter 8-bit plaintext: ")
        key = input("Enter 10-bit key: ")

        if len(plain) != 8 or len(key) != 10:
            print("Invalid length!")
        elif not (set(plain) <= {'0','1'} and set(key) <= {'0','1'}):
            print(" Only binary allowed!")
        else:
            encrypt(plain, key)

    elif ch == 2:
        break

    else:
        print("Invalid choice!")
