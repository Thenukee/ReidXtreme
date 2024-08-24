def find_compressed_string(n1, s1, output1, n2, s2, output2):
    def compress_string(s):
        compressed = ""
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                if count == 1:
                    compressed += s[i-1]
                else:
                    compressed += s[i-1] + str(count)
                count = 1
        if count == 1:
            compressed += s[-1]
        else:
            compressed += s[-1] + str(count)
        return compressed

    def match_output(compressed, output):
        return compressed == output

    for i in range(1, n1+1):
        for j in range(1, n2+1):
            compressed1 = compress_string(s1)
            compressed2 = compress_string(s2)
            if match_output(compressed1, output1) and match_output(compressed2, output2):
                return compress_string

    return None

# Example usage
n1 = 10
s1 = "aabbccc"
output1 = "a2b2c3"
n2 = 10
s2 = "abbbbbbbbbbb"
output2 = "ab12"

compressed_func = find_compressed_string(1994, "abbbbbbbbbbbb", "qgqbgmz", 58, "ab", "nxkkk")
if compressed_func:
    print("Found a matching function:", compressed_func)
else:
    print("No matching function found.")