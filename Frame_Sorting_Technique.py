#Frame Sorting Technique
# Frames arriving out of order
frames = [
    (2, "or"),   # Frame 2
    (1, "W"),    # Frame 1
    (3, "ld")    # Frame 3
]

print("Received Frames:", frames)

# Sort by sequence number
frames.sort(key=lambda x: x[0])
print("Sorted Frames:", frames)

# Reconstruct message
message = ""
for number, data in frames:
    message += data

print("Reconstructed Message:", message)
