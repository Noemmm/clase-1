meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "CREEPY": "aterrador o siniestro",
            "XD": "algo que da risa",
            "POV": "tu punto de vista"
            }

for i in range(5):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Tu palabra no fue encontrada😅😅 intenta con otra")
