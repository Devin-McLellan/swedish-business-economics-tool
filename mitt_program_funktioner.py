import csv
import numpy as np
import matplotlib.pyplot as plt
import time

# Konstanter
NAMN = "Akre Handel AB"
MOMS, AGA, TP, SE, SKATT = 25, 31.42, 4.5, 12, 30

def countdown():
    """Nedräkning innan avslut."""
    for i in range(3, 0, -1):
        print(f"00:00:{i:02}")
        time.sleep(1)
    print("Nu slutar programmet!")

def avsluta_program():
    """Avslutar programmet med en nedräkning."""
    print("Avslutar programmet...")
    countdown()
    exit()

def welcome():
    """Skriver ut välkomstmeddelande."""
    ram = "*" * 74
    text = " Välkommen till programmet som hanterar företagsekonomi! ".center(72)
    prompt = " Vänligen skriv in följande uppgifter: ".center(72)

    print(f"\n{ram}\n{text}\n\n{prompt}\n{ram}\n")

def reader_csv(filename='skattetabell.csv'):
    """Läser in skattetabellen från en CSV-fil."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return list(csv.reader(file, delimiter=';'))
    except FileNotFoundError:
        print("Fel: Filen hittades inte.")
        exit()

def val_forsamling(skattetabell):
    """Låter användaren välja en församling."""
    while True:
        forsamling_val = input("\n\tAnge din församling ('q' för att avsluta): ").upper().strip()
        if forsamling_val == "Q":
            avsluta_program()
        
        matchande_rader = [rad for rad in skattetabell if rad[3].upper() == forsamling_val]
        if matchande_rader:
            print(f"Du har valt församlingen: {forsamling_val}")
            if input("Bekräfta val? ('Y/N'): ").upper().strip() == "Y":
                return matchande_rader
        else:
            print("Församling hittades inte. Försök igen.")

def berakna_brutto(timPris, antalTimmar):
    """Beräknar bruttoinkomst och inkomst med moms."""
    bruttoInkomst = timPris * antalTimmar
    inkomstMedMoms = bruttoInkomst * (1 + (MOMS / 100))
    return bruttoInkomst, inkomstMedMoms

def skriva_ut_faktura(antalTimmar, timPris, bruttoInkomst, inkomstMedMoms):
    """Skriver ut en faktura."""
    print(f"\n{NAMN:^50}")
    print("-" * 50)
    print(f"Arbetade timmar: {antalTimmar:>26,.2f} timmar")
    print(f"Timpris: {timPris:>34,.2f} kr/tim")
    print(f"Totalt exkl. moms: {bruttoInkomst:28,.2f} kr")
    print(f"Moms: {(inkomstMedMoms - bruttoInkomst):>41,.2f} kr")
    print("-" * 50)
    print(f"Totalt fakturerat: {inkomstMedMoms:>28,.2f} kr\n")

def berakna_lone_kostnad(bruttoLon):
    """Beräknar arbetsgivaravgifter, pension och total lönekostnad."""
    agAvgifter = bruttoLon * (AGA / 100)
    tpAvgifter = bruttoLon * (TP / 100)
    seAvgifter = bruttoLon * (SE / 100)
    totalLon = bruttoLon + agAvgifter + tpAvgifter + seAvgifter
    return agAvgifter, tpAvgifter, seAvgifter, totalLon


def berakna_netto():
    #konstanter
    MOMS = 25
    AGA = 31.42
    TP = 4.5
    SE = 12
    SKATT = 30

    months = ["Januari", "Februari", "Mars", "April",
            "Maj", "Juni", "Juli", "Augusti",
            "September",
            "Oktober", "November", "December"]
    
    #Användar-inmatning till matris:
    
    while True:
        bruttoLon = input("Ange din önskade bruttolön (före skatt, ('q') för att avsluta)): ").upper()
        if bruttoLon == "Q":
             print("Avslutar")
             break
        timPris = input("Mata in företagets timpris (exklusive moms): ").upper()
        if timPris == "Q":
            print("Avslutar")
            break
        timPris = float(timPris)

        total_100 = total_80 = 0

        print(f"\nExempel baserat på {timPris} kr timpris\n")
        print(f"{'Månad':<10} {'100% beläggning':<15} {'80% beläggning':<15}")
        print("-"*40)

        for month in months:
            antalTimmar = (input(f"Ange antal arbetade timmar som skall faktureras för {month}, ('q' för att avsluta): ")).upper().strip()
            if antalTimmar == "Q":
                break
            else:
                antalTimmar = float(antalTimmar)
                bruttoInkomst = round(timPris * antalTimmar, 4)
                inkomst_100, inkomst_80 = bruttoInkomst, bruttoInkomst * 0.80
                total_100 += inkomst_100
                total_80 += inkomst_80
                print(f"{month:<10} {inkomst_100:<15.0f} {inkomst_80:<15.0f}")

        print("-" * 40)
        print(f"Totala intälten för året (100 %): {total_100:2.0f} kr")
        print(f"Realistiska intäkten för året (80% ): {total_80:2.0f} kr\n")

def skriv_ut_lonekostnad(bruttoLon, agAvgifter, tpAvgifter, seAvgifter, totalLon):
    """Skriver ut lönekostnaden."""
    print(f"\n{'Sammanställning':^50}")
    print("-" * 50)
    print(f"Bruttolön: {bruttoLon:>36,.2f} kr")
    print(f"Arbetsgivaravgift: {agAvgifter:>28,.2f} kr")
    print(f"Tjänstepension: {tpAvgifter:31,.2f} kr")
    print(f"Semesterersättning: {seAvgifter:>27,.2f} kr")
    print("-" * 50)
    print(f"Total lönekostnad: {totalLon:>28,.2f} kr\n")

def visa_menu():
    """Visar huvudmenyn."""
    menu_val = {
        "1": "Skapa en faktura",
        "2": "Beräkna företagets kostnader",
        "3": "Beräkna nettolön och semesterdagar",
        "4": "Beräkna kvarvarande pengar i bolaget",
        "5": "Skriv ut en fin prognos, tabell och diagram",
        "6": "Beräkna totala intäkter för ett helt år",
        "7": "Avsluta programmet"
    }
    print("\n", "-" * 10, "Menu", "-" * 10)
    for key, value in menu_val.items():
        print(f"{key}: {value}")















# konstanter
NAMN, MOMS, AGA, TP, SE, SKATT = "Akre handel AB", 25, 31.42,  4.5, 12, 30 


def welcome():
        #Välkomsttext/ design
    ram = "*" * 74
    text = " Välkommen programmet som hanterar företagsekonomi!".title().center(72)
    prompt = " Vänligen skriv in följande uppgifter: ".title().center(72)
    ram = "*" * 74

    print("\n" + ram)
    print(f"{text}\n")
    print(f"{prompt}")
    print(ram + "\n")


def kommun_val(skattetabell):
    while True:
        kommun_val = input("\tAnge din kommun ('q' för att avsluta): ").upper().strip()

        if kommun_val == "Q":   # Avslutar program
            print("Avslutar program.")
            break

        matchande_rader = [rad for rad in skattetabell if rad[2].upper() == kommun_val]

        if matchande_rader:
            print(f"\nMatchande kommuner för: {kommun_val}")
            re_choice = input(("Bekräfta med 'Y', välj om med 'N': ")).upper().strip()
            if re_choice == 'Y':
                    return matchande_rader
        else:
             print("Kommun hittades ej. Försök igen.")



def val_forsamling(skattetabell):
    while True:
        forsamling_val = input("\n\tAnge din församling ('q' för att avsluta): ").upper().strip()

        if forsamling_val == "Q":
            avsluta_program()
        
        matchande_rader = [rad for rad in skattetabell if rad[3].upper() == forsamling_val]

        if matchande_rader:
            print(f"Du har valt församlingen: {forsamling_val}")
            re_choice = input("Bekräfta val? ('Y/N): ").upper().strip()
            if re_choice == "Y":
                return matchande_rader
        else:
            print("Församling hittades inte. Försök igen.")    # Felmeddelande om fel inmatning



def berakna_nettolon(valda_rader): 
    while True:
        user_input = input("\nAnge din bruttolön, 'q' för att avsluta: ").strip().upper()

        if user_input == "Q":   #Avslutar loopen
            avsluta_program()

        try: 
            bruttolon = float(user_input)   # Omvandlar till annan variabel för tydlighet
            skattesats = float(valda_rader[0][4]) if valda_rader else 30.0  # Standard 30 om saknas
            skatt = bruttolon * skattesats / 100
            netto_lon = bruttolon - skatt

            print(f"Bruttolönen: {bruttolon:.2f} kr")
            print(f"Skatt: {skattesats}%")
            print(f"Skatt: {skatt:.2f} kr")
            print(f"Nettolön: {netto_lon:.2f} kr\n")
            return
        except ValueError:
            print("Felaktig inmatning, ange ett numretiskt värde.")




def berakna_brutto(timPris, antalTimmar):   # Funktion som BERÄKNAR brutto... pusslar ihop alla delar...
    # timPris = float(input("Mata in företagets timpris (exklusive moms): "))
    # antalTimmar = float(input("Ange antal arbetade timmar, som skall faktureras: "))
    # räknar ut brutto inkomst och inkomst med moms
    bruttoInkomst = timPris * antalTimmar
    inkomstMedMoms = bruttoInkomst * (1+ (MOMS/100))
    return bruttoInkomst, inkomstMedMoms

def skriva_ut_faktura(antalTimmar, timPris, bruttoInkomst,inkomstMedMoms):# Fkn som SKRIVER faktura
    # skriver ut fakturan
    print(f"\n{NAMN:^50}")
    print("-"*50)
    print(f"Arbetade timmar: {antalTimmar:>26,.2f} timmar")
    print(f"Timpris: {timPris:>34,.2f} kr/tim")
    print(f"Totalt exkl. moms: {bruttoInkomst:28,.2f} kr")
    print(f"Moms: {(inkomstMedMoms - bruttoInkomst):>41,.2f} kr")
    print("-"*50)
    print(f"Totalt fakturerat: {inkomstMedMoms:>28,.2f} kr\n")
    return antalTimmar, timPris, bruttoInkomst,inkomstMedMoms

def berakna_lone_kostnad(bruttoLon): # Fkn som beräknar löne kostnad
    # tar användarens input för önskad brutto lön
    # bruttoLon = float(input("Ange din önskade bruttolön (före skatt): "))
    #beräknar arbetsavgifter, semesterersättning och tjänstepension
    agAvgifter = bruttoLon * (AGA/100)
    tpAvgifter = bruttoLon * (TP/100)
    seAvgifter = bruttoLon * (SE/100)
    totalLon = bruttoLon + agAvgifter + tpAvgifter + seAvgifter
    return agAvgifter, tpAvgifter, seAvgifter,totalLon

def skriv_ut_lonekostnad(bruttoLon,agAvgifter,tpAvgifter,seAvgifter,totalLon):  # Fkn som SKRIVER ut lönekostnad
    # skriver ut en samman stälning på brutto lönen och avigfter
    print(f"\n{"Sammanställning":^50}")
    print("-"*50)
    print(f"Bruttolön: {bruttoLon:>36,.2f} kr")
    print(f"Arbetsgivaravgift: {agAvgifter:>28,.2f} kr")
    print(f"Tjänstepension: {tpAvgifter:31,.2f} kr")
    print(f"Semesterersättning: {seAvgifter:>27,.2f} kr")
    print("-"*50)
    print(f"Total lönekostnad: {totalLon:>28,.2f} kr\n")

def nettolon_resterande_pengar(bruttoLon,bruttoInkomst,totalLon): # Fkn som BERÄKNAR nettolön och resterande pengar i bolaget
    # räknar ut netolönen och resterande pengar
    netLon = bruttoLon * (1-(SKATT/100))
    resterande = bruttoInkomst - totalLon
    return netLon, resterande

def skriv_ut_nettolon(netLon,bruttoLon,resterande): # Fkn som SKRIVER ut nettolön
    #funktionen skriver ut sammanställning av nettolön och skatt
    print(f"{"Sammanställning":^50}")
    print("-"*50)
    print(f"Nettolön: {netLon:37,.2f} kr")
    print(f"Betald skatt: {bruttoLon - netLon:>33,.2f} kr")
    print("-"*50)
    print(f"Resterande Pengar: {resterande:>28,.2f} kr")


# Till steg 5 i del 2, funktion som jag skapat med uppgifter från klasskamrats kod: 

def berakna_netto():
    #konstanter
    MOMS = 25
    AGA = 31.42
    TP = 4.5
    SE = 12
    SKATT = 30

    months = ["Januari", "Februari", "Mars", "April",
            "Maj", "Juni", "Juli", "Augusti",
            "September",
            "Oktober", "November", "December"]
    
    #Användar-inmatning till matris:
    
    while True:
        bruttoLon = input("Ange din önskade bruttolön (före skatt, ('q') för att avsluta)): ").upper()
        if bruttoLon == "Q":
             print("Avslutar")
             break
        timPris = input("Mata in företagets timpris (exklusive moms): ").upper()
        if timPris == "Q":
            print("Avslutar")
            break
        timPris = float(timPris)

        total_100 = total_80 = 0

        print(f"\nExempel baserat på {timPris} kr timpris\n")
        print(f"{'Månad':<10} {'100% beläggning':<15} {'80% beläggning':<15}")
        print("-"*40)

        for month in months:
            antalTimmar = (input(f"Ange antal arbetade timmar som skall faktureras för {month}, ('q' för att avsluta): ")).upper().strip()
            if antalTimmar == "Q":
                break
            else:
                antalTimmar = float(antalTimmar)
                bruttoInkomst = round(timPris * antalTimmar, 4)
                inkomst_100, inkomst_80 = bruttoInkomst, bruttoInkomst * 0.80
                total_100 += inkomst_100
                total_80 += inkomst_80
                print(f"{month:<10} {inkomst_100:<15.0f} {inkomst_80:<15.0f}")

        print("-" * 40)
        print(f"Totala intälten för året (100 %): {total_100:2.0f} kr")
        print(f"Realistiska intäkten för året (80% ): {total_80:2.0f} kr\n")

def visa_menu():
    menu_val = {
        "1": "Skapa en faktura",
        "2": "Beräkna företagets kostnader",
        "3": "Beräkna nettolön och semesterdagar",
        "4": "Beräkna kvarvarande pengar i bolaget",
        "5": "Skriv ut en fin prognos, tabell och diagram", 
        "6": "Beräkna totala intäkter för ett helt år",
        "7": "Avsluta programmet"
    }
    print("\n", "-"*10,"Menu","-"*10)
    for key, value in menu_val.items():   #Går igenom de två parametrarna
        print(f"{key.capitalize():12}: {value}")

#Rolig nedräkningsfunktion till quit() funktionen i main, (fick tråkigt klockan 1 på natten)
def countdown(): 
    min_tid = 3

    for i in range(min_tid,0,-1):    # Nedräkning baklänges=P
        sekunder = i % 60
        minuter = int(i / 60) % 60
        timmar = int(i / 3600)
        print(f"{timmar}:{minuter:02}:{sekunder:02}")
        time.sleep(1)
    print("Nu slutar programmet!")


def stapel_diagram():
    months = ["Januari", "Februari", "Mars", "April",
              "Maj", "Juni", "Juli", "Augusti",
              "September", "Oktober", "November", "December"]

    fakturerad_summa = []
    
    for month in months:
        while True: 
            inkomst = input(f"Ange fakturerat belopp för {month} ('Q' för att avsluta): ").strip().upper()
            if inkomst == "Q":
                break
            try:
                inkomst = float(inkomst)
                fakturerad_summa.append(inkomst)
                break
            except ValueError:
                print("Felaktig inmatning, försök igen.")

    if not fakturerad_summa:
        print("Det verkar som att det var tomt här!")
        return

    # Beräkna den 80 procent av inkomsterna: 
    fakturerad_summa_80 = [inkomst * 0.80 for inkomst in fakturerad_summa]

    # Skapar stapeldiagram: 
    xposition = np.arange(len(fakturerad_summa))

    plt.bar(xposition - 0.2, fakturerad_summa, width=0.4, color='blue', label="100% Fakturerat (Blå)") 
    plt.bar(xposition + 0.2, fakturerad_summa_80, width=0.4, color='orange', label="80% av Fakturerat (Orange)") 

    plt.xticks(xposition, months[:len(fakturerad_summa)], rotation=45) 

    plt.title("Fakturerat belopp (KR)")
    plt.xlabel("Månad")
    plt.ylabel("Belopp (KR)")
    plt.legend(title="Färgförklaring")

    plt.show()

