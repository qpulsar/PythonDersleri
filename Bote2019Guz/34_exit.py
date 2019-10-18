# exit girilinceye kadar kelimeleri kaydettirin
# Kaç kelime girildi
# Toplam kaç harf girildi
# Bir kelimedeki ortalama harf sayısını bulun
# en uzun kelime
# en kısa keliemeyi bulsunlar

words = []
word = ""
while word.lower() != "exit":
    word = input("Bir kelime giriniz:")
    words.append(word)

words.pop()  # son kelimeyi siler
count = len(words)
print("Girilen kelime sayısı:", count)

toplamHarf = 0
for w in words:
    toplamHarf += len(w)

print("Toplam Harf Sayısı:", toplamHarf)
print("Ortalama kelime uzunluğu :", toplamHarf / count)

enuzun = 0
hangisi = 0
for i in range(0, len(words)):
    print("Bir kelimenin uzunluğu:", len(words[i]))
    if len(words[i]) > enuzun:
        enuzun = len(words[i])
        hangisi = i
    print("şu ana kadarki en uzun:", enuzun)

print("En uzun kelim : {}, uzunluğu {} harf".
      format(enuzun,words[hangisi]))