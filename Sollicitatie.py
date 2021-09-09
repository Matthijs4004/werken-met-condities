# Sollicitatie Ruimtevuilnisman


print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("+        Sollicitatie formulier Ruimte-vuilnisman        +")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Er wordt u een aantal relevante vragen gesteld...")
print("Gelieve die naar eer en geweten in te vullen.")
print("Als blijkst dat u aan de criteria voldoet dan komt u in")
print("aanmerking voor een serieus solliciatiegesprek!")
print("Ontspan maar blijf wakker, hier komen de vragen.")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

naam = input("Wat is uw naam? ")

faaltekst = "Beste " + naam + ","
faaltekst2 = "U voldoet niet aan onze strenge eisen voor de functie van Ruimte-vuilnisman, het spijt ons!"
geslaagdtekst = "Beste " + naam + ","
geslaagdtekst2 = "Proficiat! U komt in aanmerking voor een sollicitatiegesprek, stuur snel uw CV."

lichaamslengte = int(input("Wat is uw netto lichaamslengte in hele cm, dus exclusief uw kapsel? "))
if lichaamslengte > 150:
    lichaamsgewicht = int(input("Wat is uw lichaamsgewicht in hele kg? "))
    if lichaamsgewicht > 90:
        praktijkervaring = int(input("Hoeveel jaar praktijkervaring heeft u met dieren-dressuur? "))
        if praktijkervaring > 4:
            diploma = input("Bent u in het bezit van een diploma MBO-4 ondernemen? J/N ")
            if diploma.lower() == "ja":
                hogehoed = input("Bent u in het bezit van een hoge hoed? J/N ")
                if hogehoed.lower() == "ja":
                    man = input("Bent u een man? J/N ")
                    if man.lower() == "ja":
                        snor = int(input("Hoe breedt is uw snor in hele cm? "))
                        if snor > 10:
                            rijbewijs = input("Bent u in het bezit van een geldig vrachtwagen rijbewijs? J/N ")
                            if rijbewijs.lower() == "ja":
                                certificaat = input("Bent u in het bezit van het Certificaat “Overleven met gevaarlijk personeel”? J/N ")
                                if certificaat.lower() == "ja":
                                    print(geslaagdtekst)
                                    print(geslaagdtekst2)
                            else:
                                print(faaltekst)
                                print(faaltekst2)
                        else:
                            print(faaltekst)
                            print(faaltekst2)
                    else:
                        print(faaltekst)
                        print(faaltekst2)
                else:
                    print(faaltekst)
                    print(faaltekst2)
            else:
                print(faaltekst)
                print(faaltekst2)        
        else:
            print(faaltekst)
            print(faaltekst2)
    else:
        print(faaltekst)
        print(faaltekst2)    
else:
    print(faaltekst)
    print(faaltekst2)


