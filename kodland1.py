rastgele_gercekler=["Serkan","python basic projem","tost","kod yazmak"]
rastgele_gercek= random.choice(rastgele_gercekler)
print("Hakkımdaki rastgele gerçek: ", rastgele_gercek)

meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            }
            
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    print("Aradığınız kelimenin anlamı: ", meme_dict[word])
else:
    print("Aradığınız kelime bulunamamaktadır.")
