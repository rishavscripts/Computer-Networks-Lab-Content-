# Hamming Code Implementation in Python
def calculate_parity_bits(data):
    m = len(data)
    r = 0
    while (2**r < m + r + 1):
        r += 1
    return r


def generate_hamming_code(data):
    r = calculate_parity_bits(data)
    hamming_code = ['0'] * (len(data) + r)

    # Place data bits in non-parity positions
    j = 0
    for i in range(1, len(hamming_code) + 1):
        if (i & (i - 1)) != 0:   # not a power of 2
            hamming_code[i - 1] = data[j]
            j += 1

    # Calculate parity bits
    for i in range(r):
        parity_pos = 2 ** i
        parity = 0
        # Calculate parity for the current parity bit
        for j in range(1, len(hamming_code) + 1):
            # Check if the current position is covered by the parity bit
            if j & parity_pos:
                # If it's a data bit, include it in the parity calculation
                parity ^= int(hamming_code[j - 1])
        # Set the parity bit in the hamming code
        hamming_code[parity_pos - 1] = str(parity)    
    return hamming_code
    #return ''.join(hamming_code)


def detect_error(hamming_code):
    r = calculate_parity_bits(hamming_code)
    error_pos = 0
    for i in range(r):
        parity_pos = 2**i
        parity_count = 0
        for j in range(1, len(hamming_code) + 1):
            if j & parity_pos == parity_pos:
                for k in range(j, min(j + parity_pos, len(hamming_code) + 1)):
                    if k & (k - 1) != 0:
                        parity_count += int(hamming_code[k - 1])
        if parity_count % 2 != 0:
            error_pos += parity_pos
    return error_pos



# Example usage
data = "1011"           
hamming_code = generate_hamming_code(data)
print("Hamming Code:", hamming_code)    
# Introduce an error
hamming_code_with_error = list(hamming_code)        
hamming_code_with_error[2] = '1' if hamming_code_with_error[2] == '0' else '0'
hamming_code_with_error = ''.join(hamming_code_with_error)  
print("Hamming Code with Error:", hamming_code_with_error)
error_position = detect_error(hamming_code_with_error)
if error_position == 0:
    print("No error detected.")
else:
    print(f"Error detected at position: {error_position}")
