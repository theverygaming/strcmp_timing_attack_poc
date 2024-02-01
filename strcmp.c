int strcmp_unsafe(const char *str1, const char *str2) {
    int idx_1 = 0;
    int idx_2 = 0;
    while ((str1[idx_1] != '\0') && (str2[idx_2] != '\0')) {
        if (str1[idx_1] != str2[idx_1]) {
            return 1;
        }
        idx_1++;
        idx_2++;
    }
    return 0;
}

int strcmp_safe(const char *str1, const char *str2) {
    int returnval = 0;
    int idx_1 = 0;
    int idx_2 = 0;
    while ((str1[idx_1] != '\0') && (str2[idx_2] != '\0')) {
        if (str1[idx_1] != str2[idx_1]) {
            returnval = 1;
        }
        idx_1++;
        idx_2++;
    }
    return returnval;
}
