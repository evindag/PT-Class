#Girilen şifre “Python” olana kadar “Tekrar deneyiniz”
#uyarısı veren, “Python” girildiğinde “Giriş başarılı” 
#uyarısı veren kodu yazınız.

while True:
    girilen_sifre = input("Lütfen şifreyi giriniz: ")
    if girilen_sifre != "Python":
        print("Tekrar deneyiniz.")
    else:
        print("Giriş başarılı.")
        break
