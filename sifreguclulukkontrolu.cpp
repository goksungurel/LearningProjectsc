#include <iostream>
#include <string>
using namespace std;

int main() {
    string sifre;
    bool sayiVar = false;
    bool ozelKarakterVar = false;

    cout << "Lutfen bir sifre girin: ";
    getline(cin, sifre);

    for (int i = 0; i < sifre.length(); i++) {
        char ch = sifre[i];

        if (ch >= '0' && ch <= '9') {
            sayiVar = true;
        }

        if (ch == '@' || ch == '#' || ch == '!' || ch == '%' || ch == '-' || ch == '*') {
            ozelKarakterVar = true;
        }
    }

    if (sifre.length() >= 8 && sayiVar && ozelKarakterVar) {
        cout << "Guclu sifre 🔒" << endl;
    } else {
        cout << "Zayif sifre! En az 8 karakter, bir sayi ve bir ozel karakter kullanmalisiniz." << endl;
    }

    return 0;
}
