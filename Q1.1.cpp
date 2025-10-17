#include <iostream>

using namespace std;


int find_s_n(int n) {
    if (n == 0) return 1;
    else return (find_s_n(n-1) * 3 % 9999);
}

void bonus() {
    string setA = "abc";
    int pos[10];
    
    for (int i = 0; i < 10; i++) {
        pos[i] = 0;
    }
    
    for (int i = 0; i< 99;i++ ) {
        pos[9] += 1;
        int check = 9;
            while (pos[check] == 3) {
                pos[check] = 0;
                pos[check-1] += 1;
                check -= 1;
            }
                    
    }
    for (int p = 0; p < 10; p++) {
                    cout << setA[pos[p]];
                }
}

int main()
{
    cout << find_s_n(1000) << endl;
    bonus();
    
    return 0;
}