# Text-based Adventure game in Python
# De game is gebaseerd op het survival spel "The Forest"
# The Forest gaat over een vliegtuig die neerstort op een onbewoond eiland


print("Je hebt net een heftige noodlanding gemaakt omdat een van de motoren van het vliegtuig het begaf.")
print("Je wordt wakker zonder enig idee waar je bent alleen bij het wrak van het vliegtuig.")
print("-----------------------------------------------------------------------------")

antwoord = input("Er ligt een bijl op de grond van het vliegtuig wrak, neem je de bijl mee? (ja/nee) ")
if antwoord.lower().strip() == "ja":
    print("Goede keuze!")
    print()
    antwoord = input("Wil je deze bijl gebruiken om een veilige slaap plek te maken? (ja/nee) ")
    if antwoord.lower().strip() == "ja":
        print("Uitstekende keuze, je zelf gemaakte slaap plek beschermt jezelf tegen de mogelijke bedreigingen op het eiland.")
        print()
        print("De ochtend is aangebroken en je moet een beslissing maken.")
        antwoord = input("Ga je dieper het bos is of ga je naar het vliegtuig om spullen te verzamelen? (bos/vliegtuig) ")
        if antwoord.lower().strip() == "bos":
            print("Goede keuze!")
            print()
            antwoord = input("Je gaat dieper het bos in en komt een grot tegen. Ga je de grot in? (ja/nee) ")
            if antwoord.lower().strip() == "ja":
                print()
                print("Oh nee, dat was geen goede keus. Je bent de grot van een beer in gegaan en wordt vermoord. Je hebt verloren!")
            else:
                print("Zeer goede keuze, het was de grot van een beer en die heb je ontweken.")
                print()
                antwoord = input("Het wordt nacht, ga je terug naar je slaapplek? (ja/nee) ")
                if antwoord.lower().strip() == "ja":
                    print()
                    print("Verkeerde keuze, op de weg terug naar je slaapplek wordt je overvallen door een monster op het eiland. Game over!")
                else:
                    print("Correcte keuze!")
                    print()
                    print("Je gaat verder het bos in en vindt een verlaten huis.")
                    antwoord = input("Ga je het huis in? (ja/nee) ")
                    if antwoord.lower().strip() == "ja":
                        print("Goede keuze!")
                        print()
                        print("Binnen in het huis ziet het er erg verlaten uit, maar er valt wat op in de grond.")
                        antwoord = input("Het is een luik in de grond van het huis, ga je naar beneden in het luik? (ja/nee) ")
                        if antwoord.lower().strip() == "ja":
                            print("Goede keuze!")
                            print()
                            print("Je gaat het luik naar beneden en komt terecht in een ruimte waarin allemaal spullen staan,")
                            print("zoals een generator, lampen, een betere bijl en het lijkt erop dat er ook een radio staat. ")
                            antwoord = input("Je zet de generator aan, ga je de radio gebruiken? (ja/nee) ")
                            if antwoord.lower().strip() == "ja":
                                print("Uitstekende keuze!")
                                print()
                                print("Het lijkt erop dat de radio het nog doet en je besluit contact te zoeken met iemand via de radio.")
                                print("En de radio doet het nog en je hoort iemand praten over de radio en vraagt of er een manier is om van het eiland te komen.")
                                antwoord = input("De man op de radio stelt voor om een boot te varen richting het eiland, neem je dit offer aan? (ja/nee) ")
                                if antwoord.lower().strip() == "ja":
                                    print()
                                    print("De volgende dag hoor je de boot al in de verte aankomen")
                                    print("Je stapt op de boot zodra die aanmeert en daarmee hebt je get spel gewonnen")
                                    print("-------------------------------------")
                                    print("|             You won!              |")
                                    print("-------------------------------------")
                                else:
                                    print()
                                    print("Je hebt het offer niet aangenomen en daarmee hebt je de verkeerde keuze gemaakt. De boot is de enige manier van het eiland af. Game over!")
                            else:
                                print()
                                print("Je hebt gekozen om de radio niet te gebruiken, er is geen andere manier om van het eiland te komen dan de radio en dus heb je verloren. Game over!")
                        else:
                            print()
                            print("Het is nog nacht en er komt een monster het huis in die je om het leven brengt. Je hebt verloren")
                    else:
                        print()
                        print("Het is nog nacht en dus komt er een monster uit de bosjes tevoorschijn die jouw vermoord. Game over!")
        else:
            print()
            print("Je komt aan bij het vliegtuig en er springt ineens een monster op je vanuit de cockpit. Game over!")
    else:    
        print()
        print("Geen goede keuze, je faalt om jezelf in de nacht te beschermen tegen de monsters op het eiland. Je hebt verloren!")
else:
    print()
    print("Dat was geen goede keuze, je bent in de nacht om het leven gebracht door de monsters op het eiland. Game over!")
