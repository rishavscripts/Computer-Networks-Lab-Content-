# Interactive Hamming Code Program

def calculate_parity_bits(data_length):
    r = 0
    while (2**r < data_length + r + 1):
        r += 1
    return r

def generate_hamming_code(data):
    r = calculate_parity_bits(len(data))
    hamming = ['0'] * (len(data) + r)

    # Place data bits in non-parity positions
    j = 0
    for i in range(1, len(hamming) + 1):
        if (i & (i - 1)) != 0:   # not a power of 2 → data position
            hamming[i - 1] = data[j]
            j += 1

    # Calculate parity bits
    for i in range(r):
        parity_pos = 2**i
        parity = 0
        for j in range(1, len(hamming) + 1):
            if j & parity_pos:
                parity ^= int(hamming[j - 1])
        hamming[parity_pos - 1] = str(parity)

    return ''.join(hamming)

def detect_error(hamming_code):
    r = calculate_parity_bits(len(hamming_code))
    error_pos = 0
    for i in range(r):
        parity_pos = 2**i
        parity = 0
        for j in range(1, len(hamming_code) + 1):
            if j & parity_pos:
                parity ^= int(hamming_code[j - 1])
        if parity != 0:
            error_pos += parity_pos
    return error_pos

# ---------------- MAIN PROGRAM ----------------
print("Hamming Code Program")


choice = input("Type 'generate' to create Hamming code OR 'check' to detect error: ").lower()
data = input("Enter data bits : ")
if choice == "generate":
    hamming_code = generate_hamming_code(data)
    print("Generated Hamming Code:", hamming_code)

elif choice == "check":
    hamming_code = data  # here user enters the received hamming code
    error_position = detect_error(hamming_code)
    if error_position == 0:
        print("No error detected.")
    else:
        print("Error detected at position:", error_position)

else:
    print("Invalid choice. Please type 'generate' or 'check'.")


#OUTPUT
# Hamming Code Program
# Type 'generate' to create Hamming code OR 'check' to detect error: generate   
# Enter data bits : 1011
# Generated Hamming Code: 1011010
# Hamming Code Program
# Type 'generate' to create Hamming code OR 'check' to detect error: check
# Enter data bits : 1011010
# No error detected.