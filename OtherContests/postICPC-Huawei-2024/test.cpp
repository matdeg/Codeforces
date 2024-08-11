#include <iostream>
#include <fstream>
int main(void) {
    double f = 1.19651e299;
    int n = 1000000;
    std::ofstream myfile;
    myfile.open ("input_float_test");
    myfile << n;
    for (int i = 0; i < n; i++) {
        myfile << " " << f;
    }
    myfile.close();
    return 0;
}