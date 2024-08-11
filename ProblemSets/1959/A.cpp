#include <iostream>

int t;

int test() {
    int n; 
    std::cin >> n;
    int* a = (int*)malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
    }
    int common;
    if (a[0] == a[1]) {
        common = a[0];
    } else {
        common = a[2];
    }
    for (int i = 0; i < n; i++) {
        if (a[i] != common) {
            return i+1;
        }
    }
    return 0;
}

int main() {
    std::cin >> t;
    for (int i = 0; i<t; i++) {
        int sol = test();
        std::cout << sol << "\n ";
    }
    return 0;
}