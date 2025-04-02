import random 
print("🎲 Zar Atma Simülatörüne Hoş Geldin!")
print("Zar atmak için 'zar at' yaz, çıkmak için 'çık' yaz.\n")

while True:
    komut=input("Komut: ").lower()
    
    if komut=="zar at":
        zar=random.randint(1,6)
        print(f"Zar sonucu: {zar}\n")
    elif komut =="çık":
        print("Görüşmek üzere! 👋")
        break
    else:
        print("Geçersiz komut. Lütfen 'zar at' ya da 'çık' yaz.\n")    
