#include <iostream>
using namespace std;

int main(){
    string kullaniciadi,sifre;
    int hak=3;

    while(hak>0){
        cout<<"Kullanici adini girin: ";
        cin>>kullaniciadi;

        cout<<"Sifreyi girin: ";
        cin>>sifre;

        if(kullaniciadi=="goksun" && sifre=="1234"){
            cout<<"Hoşgeldin Göksun"<<endl;
            break;

        }else{
            hak--;
            cout<<"Geçersiz bilgiler.Kalan hak: "<<hak<<endl;
        }
    }
    if(hak==0){
        cout<<"3 defa hatalı giriş yapıldı .Giriş engellendi!"<<endl;
    }
    return 0;

}
