#include <bits/stdc++.h>
#include <vector>
#include <queue>

int len_group = 16;
double half_low_limit = 5.96046447e-8;
double half_up_limit = 65518;
double single_low_limit = 1.4012984644e-45;
double single_up_limit = 3.402823e38f;

char types[] = {'h','s','d'};

bool is_in(char** type, int grp_id, char t) {
    for (int i = 0; i < len_group; i++) {
        if (type[grp_id][i] == t) {
            return true;
        }
    }
    return false;
}

int main()
{
    
    std::ios_base::sync_with_stdio(false);
    std::cout << std::setprecision(30);


    double x;
    int n;
    std::cin >> n;
    int nb_group = (n-1)/16 + 1;
    double** a = (double**)malloc(sizeof(double*) * (nb_group));
    char** type = (char**)malloc(sizeof(char*) * (nb_group));

    for (int i = 0; i < nb_group; i++) {
        a[i] = (double*)malloc(sizeof(double) * len_group);
        type[i] = (char*)malloc(sizeof(char) * len_group);
    }

    for (int i = 0; i < n; i++) {
        std::cin >> x;
        a[i/16][i%16] = x;
        type[i/16][i%16] = 'd';
        if (half_low_limit <= x && x <= half_up_limit) {
            type[i/16][i%16] = 'h';
        } else {
            if (single_low_limit <= x && x <= single_up_limit) {
                type[i/16][i%16] = 's';
            }
        }
    }

    std::cout << "{d:";
    bool global_first = true;
    for (int i = 0; i < nb_group; i++) {
        for (int ti = 0; ti < 3; ti++) {
            if (is_in(type, i, types[ti])) {
                bool first = true;
                if (!global_first) {
                    std::cout << ",";
                } else {
                    global_first = false;
                }
                std::cout << "{" << types[ti] << ":";
                for (int j = 0; j < len_group; j++) {
                    if (type[i][j] == types[ti]) {
                        if (!first) {
                            std::cout << ",";
                        } else {
                            first = false;
                        }
                        std::cout << 16*i + j + 1;
                    }
                }
                std::cout << "}";
            }
        }
    }
    std::cout << "}";


    return 0;
}