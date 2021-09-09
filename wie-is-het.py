

kaasGeel = input("Is de kaas geel? ")
if kaasGeel == "ja":
    gaten = input("Zitten er gaten? ")
    if gaten == "ja":    	
        dureKaas = input("Is de kaas belachelijk duur? ")
        if dureKaas == "ja":
            print("Emmenthaler")
        else:
            print("Leerdammer")
    else:
        hardeKaas = input("Is de kaas hard als steen? ")
        if hardeKaas == "ja":
            print("Parmigiano Reggiano")
        else:
            print("Goudse kaas")
else:
    blauweSchimmels = input("Heeft de kaas blauwe schimmels? ")
    if blauweSchimmels == "ja":
        kaasKorst = input("Heeft de kaas een korst? ")
        if kaasKorst == "ja":
            print("Bleu de Rochbaron")
        else:
            print("Fourme d'Ambert")
    else:
        korstKaas = input("Heeft de kaas een korst? ")
        if korstKaas == "ja":
            print("Camembert")
        else:
            print("Mozzarella")
    