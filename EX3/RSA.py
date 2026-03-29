def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

try:
    p = int(input("Enter prime number p: "))
    q = int(input("Enter prime number q: "))
    e = int(input("Enter public exponent e: "))
    message = input("Enter message (number or text): ")

    print("\n========== RSA KEY GENERATION ==========\n")
    print(f"Step 1: p = {p}, q = {q}")

    n = p * q
    print(f"Step 2: n = p × q = {n}")

    phi = (p - 1) * (q - 1)
    print(f"Step 3: φ(n) = {phi}")

    print(f"Step 4: e = {e}")

    if gcd(e, phi) != 1:
        print("Error: e must be coprime with φ(n)")
    else:
        print(f"gcd({e}, {phi}) = 1 (valid)")
        d = pow(e, -1, phi)
        print(f"Step 5: d = {d}")

        print(f"\nPublic Key = ({e}, {n})")
        print(f"Private Key = ({d}, {n})")

        if message.isdigit():
            m = int(message)

            print("\nENCRYPTION")
            encrypted = pow(m, e, n)
            print(f"C = {m}^{e} mod {n} = {encrypted}")

            print("\nDECRYPTION")
            decrypted = pow(encrypted, d, n)
            print(f"M = {encrypted}^{d} mod {n} = {decrypted}")
        else:
            encrypted = []
            decrypted = ""
            for ch in message:
                m = ord(ch)
                c = pow(m, e, n)
                encrypted.append(c)
                print(f"{ch} -> {m} -> {c}")

            print("\nEncrypted message:", encrypted)

            for c in encrypted:
                m = pow(c, d, n)
                decrypted += chr(m)
                print(f"{c} -> {m} -> {chr(m)}")

            print("\nDecrypted message:", decrypted)

except:
    print("Invalid input! Please enter correct values.")
