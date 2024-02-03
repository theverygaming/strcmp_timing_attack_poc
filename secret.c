#include <strcmp.h>

int test_secret(const char *guess) {
    const char *secret = "936453";
    
    int result;
    
    for(unsigned long i = 0; i < 100000000; i++) {
        result = strcmp_unsafe(secret, guess);
        //result = strcmp_safe(secret, guess);
    }

    return result;
}
