#include <stdio.h>
#include <string.h>

// Function to compress the string
void compressString(char* s, char* compressed) {
    int len = strlen(s);
    int j = 0;  // Index for compressed string
    for (int i = 0; i < len; i++) {
        int count = 1;
        while (i + 1 < len && s[i] == s[i + 1]) {
            count++;
            i++;
        }
        compressed[j++] = s[i];
        if (count > 1) {
            j += sprintf(&compressed[j], "%d", count);
        }
    }
    compressed[j] = '\0';  // Null-terminate the compressed string
}

// Function to generate the final password
void generatePassword(int length, char* password) {
    const char* alphabet = "abcdefghijklmnopqrstuvwxyz";
    int alphabetLength = strlen(alphabet);

    for (int i = 0; i < 7; i++) {
        password[i] = alphabet[(length * (i + 1) + i * i) % alphabetLength];
    }
    password[7] = '\0';  // Null-terminate the password
}

int main() {
    int n;
    char s[4000], compressed[8000];
    char password[8];  // Since password is 7 characters long plus a null-terminator

    // Read inputs
    scanf("%d", &n);
    scanf("%s", s);

    // Compress the string
    compressString(s, compressed);

    // Get the length of the compressed string
    int compressedLength = strlen(compressed);

    // Generate the password based on the length of the compressed string
    generatePassword(compressedLength, password);

    // Print the password
    printf("%s\n", password);

    return 0;
}
