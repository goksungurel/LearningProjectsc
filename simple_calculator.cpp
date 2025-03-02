#include <iostream>
using namespace std;

int main() {
    double num1, num2;
    int choice;

    while (true) {
        cout << "Birinci sayıyı girin: ";
        cin >> num1;
        cout << "İkinci sayıyı girin: ";
        cin >> num2;
      
        cout << "\nİşlem Seçin:" << endl;
        cout << "1. Toplama" << endl;
        cout << "2. Çıkarma" << endl;
        cout << "3. Çarpma" << endl;
        cout << "4. Bölme" << endl;
        cout << "5. Çıkış" << endl;
        cout << "Seçiminizi yapın (1/2/3/4/5): ";
        cin >> choice;

      
        switch (choice) {
            case 1:
                cout << "Sonuç: " << num1 + num2 << endl;
                break;
            case 2:
                cout << "Sonuç: " << num1 - num2 << endl;
                break;
            case 3:
                cout << "Sonuç: " << num1 * num2 << endl;
                break;
            case 4:
                if (num2 != 0) {
                    cout << "Sonuç: " << num1 / num2 << endl;
                } else {
                    cout << "Bölme işlemi sıfıra yapılamaz!" << endl;
                }
                break;
            case 5:
                cout << "Çıkılıyor... Görüşürüz!" << endl;
                return 0;
            default:
                cout << "Geçersiz giriş, lütfen tekrar deneyin." << endl;
        }
        cout << "\n";
    }

    return 0;
}
