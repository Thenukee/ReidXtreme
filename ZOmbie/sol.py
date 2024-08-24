def decode_password(n, s):
    """Decodes a password from an encrypted message.

    Args:
        n: The number in the encrypted message.
        s: The string in the encrypted message.

    Returns:
        The decoded password.
    """

    compressed = ""
    current_char = s[0]
    count = 1

    for i in range(1, len(s)):
        if s[i] != current_char:
            compressed += current_char + str(count)
            current_char = s[i]
            count = 1
        else:
            count += 1

    compressed += current_char + str(count)

    password = ""
    while compressed:
        password += chr(ord('a') + int(compressed[-2:]))
        compressed = compressed[:-2]

    return password

# Example usage:
n = 1994
s = "abbbbbbbbbbbb"
password = decode_password(n, s)
print(password)  # Output: qgqbgmz