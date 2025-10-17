#include <iostream>

using namespace std;


int find_s_n(int n) {
    if (n < 0) return 0;
    if (n == 0) return 1; 

    int so_chu = (n + 1) / 2;

    long long kq = 1;
    for (int i = 0; i < so_chu; i++) {
        kq = (kq * 3) % 9999;
    }

    return kq;
}

void bonus() {
    string setA = "abc";
    int pos[10];
    
    for (int i = 0; i < 10; i++) {
        pos[i] = 0;
    }
    
    int cnt = 0;
    int vtri = 0;
    string palin100;
    
    for (int i = 0; i < 59049;i++ ) {
        
        
        
        int kt = 1;
        for (int i = 0; i < 10 / 2; i++) {
            if (pos[i] != pos[9-i]) {
                kt = 0;
            }
        }
        
        if (kt == 1) {
            vtri += 1;
        
        if (vtri == 99) {
            
            for (int p = 0; p < 10; p++) {
                palin100 += setA[pos[p]];
            }
        }
        }
        
        if (kt == 1) {
            for (int p = 0; p < 10; p++) {
                cout << setA[pos[p]];
            }
        cout << endl;
        }         
        
        pos[9] += 1;
        int check = 9;
            while (pos[check] == 3) {
                pos[check] = 0;
                pos[check-1] += 1;
                check -= 1;
            }
        
        
    }
    cout << "so thu 100: " << palin100;
}

int main()
{
    cout << find_s_n(1000) << endl;
    bonus();
    
    return 0;
}
