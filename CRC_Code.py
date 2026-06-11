# CRC Error Detection Program (following the algorithm)

def xor(a, b):
    # XOR operation: compare bits, return '0' if same, '1' if different
    result = ""
    for i in range(1, len(b)):
        result += '0' if a[i] == b[i] else '1'
    return result

def mod2div(dividend, divisor):
    # Step 2: Divide B(x) by G(x) using Modulo-2 Division
    pick = len(divisor)
    tmp = dividend[0:pick]

    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            tmp = xor('0'*pick, tmp) + dividend[pick]
        pick += 1

    # Final step for last bits
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)

    return tmp  # remainder R(x)

def encode(data, key):
    # Step 1: Append zeros (degree of generator polynomial)
    appended = data + '0'*(len(key)-1)
    # Step 2: Divide and get remainder R(x)
    remainder = mod2div(appended, key)
    # Step 3: Define T(x) = B(x) - R(x) → codeword
    return data + remainder

# ---------------- MAIN PROGRAM ----------------
data = input("Enter the Data Bits: ")
#data = "100100"   # Example bit string (B)
key = "1101"      # Generator polynomial (G)

print("Original Data (B):", data)
codeword = encode(data, key)
print("Transmitted Codeword (T):", codeword)

# Step 5: Receiver checks
received = codeword   # assume no error
remainder = mod2div(received, key)

if int(remainder) == 0:
    print("No error detected (T = T').")
else:
    print("Error detected! Retransmission required.")

# Output:
# Enter the Data Bits: 100100
# Original Data (B): 100100
# Transmitted Codeword (T): 100100001
# No error detected (T = T').