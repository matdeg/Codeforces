#include <bits/stdc++.h>
#include <vector>

int len_group = 16;

int main()
{
    
    std::ios_base::sync_with_stdio(false);
    std::cout << std::setprecision(30);

    int n;
    std::cin >> n;
    int nb_group = (n-1)/16 + 1;
    double** a = (double**)malloc(sizeof(double*) * (nb_group));

    for (int i = 0; i < nb_group; i++) {
        a[i] = (double*)malloc(sizeof(double) * len_group);
    }

    for (int i = 0; i < n; i++) {
        std::cin >> a[i/16][i%16];
    }

    std::cout << "{d:1";
    for (int i = 2; i <= n; i++) {
        std::cout << "," << i;
    }
    std::cout << "}\n";
    return 0;
}