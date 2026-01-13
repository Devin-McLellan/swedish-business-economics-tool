"""
Ekonomiprogram - Funktionsmodul

Innehåller alla hjälpfunktioner för ekonomiprogrammet:
- CSV-hantering
- Kommunval
- Fakturahantering
- Kostnadsberäkningar
- Lönberäkningar
- Prognoser och visualiseringar

Författare: [Kevin McLellan]
Version: 1.0
"""

import time
import csv
import matplotlib.pyplot as plt


# === Designelement ===
RAM = "*" * 74
LINE = "-" * 74


# === Startmeny ===
def welcome():
    """Visar välkomstmeddelande när programmet startar."""
    text = "Välkommen till världens bästa program för företagsekonomi!".title().center(72)
    prompt = "För att skapa magi - skriv in din kommun nedanför:".title().center(72)
    
    print("\n" + RAM)
    print(f"{text}\n")
    print(f"{prompt}")
    print(RAM + "\n")


# === CSV-hantering ===
def reader_csv(filnamn='skattetabell.csv', delimiter=';'):
    """
    Läser in en CSV-fil och returnerar innehållet som en 2D-lista.
    
    Args:
        filnamn (str): Filnamn för CSV-filen
        delimiter (str): Avgränsare i CSV-filen
    
    Returns:
        list: 2D-lista med CSV-data, eller None vid fel
    """
    try:
        with open(filnamn, 'r', encoding='utf-8') as file:
            return list(csv.reader(file, delimiter=delimiter))
    except FileNotFoundError:
        print(f"❌ Fel: Filen '{filnamn}' hittades inte.")
        return None


# === Kommunval ===
def val_kommun(filnamn):
    """
    Låter användaren välja kommun och församling från skattetabellen.
    
    Args:
        filnamn (str): Filnamn för skattetabellen
    
    Returns:
        tuple: (valda_rader, skattesats) eller (None, None) vid fel
    """
    data = reader_csv(filnamn)
    if data is None:
        return None, None
    
    valda_rader = []
    skattesats = None
    
    # === Välj kommun ===
    while True:
        try:
            kommun_val = input("\tAnge din kommun ('Enter' för att bekräfta, 'q' för att avsluta): ").upper().strip()
            
            if kommun_val == "Q":
                avsluta()
            
            # Filtrera matchande kommuner
            matchande_rader_kommun = [rad for rad in data if rad[2].upper() == kommun_val]
            
            if matchande_rader_kommun:
                print(f"\nMatchande kommuner för: {kommun_val}")
                re_choice = input("Bekräfta med 'Y', välj om med 'N': ").upper().strip()
                print(LINE)
                
                if re_choice == 'N':
                    continue
                elif re_choice == 'Y':
                    print(f"\n\tVald kommun: {kommun_val}\n")
                    print(LINE)
                    for rad in matchande_rader_kommun:
                        print(rad[3])
                    break
            else:
                print("❌ Kommunen fanns inte med! Försök gärna igen.")
        
        except Exception as fel:
            print(f"❌ Något konstigt inträffade: {fel}, försök igen!")
    
    # === Välj församling ===
    while True:
        try:
            forsamling_val = input("\n\tAnge din församling ('q' för att avsluta): ").upper().strip()
            
            if forsamling_val == "Q":
                avsluta()
            
            # Filtrera matchande församlingar
            matchande_rader_forsamling = [rad for rad in data if rad[3].upper() == forsamling_val]
            
            if matchande_rader_forsamling:
                print(LINE)
                print(f"\nDu har valt församlingen: {forsamling_val}")
                print(LINE)
                re_choice = input("Bekräfta med 'Y', välj om med 'N': ").upper().strip()
                print(LINE + "\n")
                
                if re_choice == 'N':
                    continue
                elif re_choice == 'Y':
                    valda_rader = matchande_rader_forsamling
                    break
            else:
                print("\n\t❌ Inga matchande församlingar hittades, försök igen!")
        
        except Exception as fel:
            print(f"❌ Något fel uppstod: {fel}, försök igen!")
    
    # Hämta skattesats från vald församling
    if valda_rader and len(valda_rader[0]) > 4:
        skattesats = float(valda_rader[0][4])
        print(f"\n✓ Skattesatsen för {kommun_val} är {skattesats}%\n")
        print(LINE)
    else:
        skattesats = 30.0
        print(f"\n⚠️  Skattesatsen kunde inte hämtas. Använder standardvärde på {skattesats}%\n")
    
    # Visa valda rader
    if valda_rader:
        print(LINE)
        print("\n\tValda rader som sparats:")
        for rad in valda_rader:
            print(f"\t{rad}")
        print(LINE + "\n")
    else:
        print("\n\t❌ Inga rader har valts!")
    
    return valda_rader, skattesats


# === Huvudmeny ===
def meny(skattesats, valda_rader):
    """
    Visar huvudmenyn och hanterar användarens val.
    
    Args:
        skattesats (float): Skattesats för vald kommun
        valda_rader (list): Data för vald kommun och församling
    """
    while True:
        print("\n" + "="*50)
        print("MENY".center(50))
        print("="*50)
        print("1. Skapa en snygg faktura")
        print("2. Beräkna företagets kostnader")
        print("3. Beräkna nettolön")
        print("4. Beräkna kvarvarande pengar i bolaget")
        print("5. Skriv ut prognos, tabell och diagram")
        print("6. Visa menyn igen")
        print("7. Avsluta programmet")
        print("="*50)
        
        val = input("Välj alternativ (1-7): ").strip()
        
        if val == "1":
            print("\n📄 Skapar snygg faktura...")
            val_1()
        elif val == "2":
            print("\n💰 Beräknar kostnader...")
            val_2(skattesats)
        elif val == "3":
            print("\n💵 Beräknar nettolön...")
            val_3(skattesats, valda_rader)
        elif val == "4":
            print("\n🏦 Beräknar kvarvarande pengar i bolaget...")
            del_4(skattesats, valda_rader)
        elif val == "5":
            print("\n📊 Skapar prognos, tabell och diagram...")
            steg_5_6()
        elif val == "6":
            print("\n🔄 Visar menyn igen...")
            continue
        elif val == "7":
            print("\n👋 Avslutar...")
            avsluta()
        else:
            print("\n❌ Ogiltigt val, försök igen.")


# === Funktion 1: Skapa faktura ===
def val_1():
    """Skapar och visar en faktura baserat på timpris och arbetade timmar."""
    NAMN = "Akre Handel AB"
    MOMS = 25  # Momsprocent
    
    try:
        tim_pris = float(input("\nMata in företagets timpris (exklusive moms): "))
        antal_timmar = float(input("Ange antal arbetade timmar som ska faktureras: "))
        
        # Beräkningar
        brutto_inkomst = tim_pris * antal_timmar
        inkomst_med_moms = brutto_inkomst * (1 + (MOMS / 100))
        moms_belopp = inkomst_med_moms - brutto_inkomst
        
        # Visa faktura
        print("\n" + "="*50)
        print(NAMN.center(50))
        print("-"*50)
        print(f"Arbetade timmar: {antal_timmar} timmar")
        print(f"Timpris: {tim_pris} kr/tim")
        print(f"Totalt exkl. moms: {brutto_inkomst:.2f} kr")
        print(f"Moms ({MOMS}%): {moms_belopp:.2f} kr")
        print("-"*50)
        print(f"Totalt fakturerat: {inkomst_med_moms:.2f} kr")
        print("="*50 + "\n")
        
        return antal_timmar, tim_pris, brutto_inkomst, inkomst_med_moms
    
    except ValueError:
        print("❌ Felaktig inmatning. Ange tal.")
        return None


# === Funktion 2: Beräkna företagskostnader ===
def val_2(skattesats):
    """
    Beräknar och visar företagets totala kostnader för en anställd.
    
    Args:
        skattesats (float): Skattesats för vald kommun
    """
    # Konstanter
    AGA = 31.42  # Arbetsgivaravgift i procent
    TP = 4.5     # Tjänstepension i procent
    SE = 12      # Semesterersättning i procent
    
    try:
        brutto_lon = float(input("\nAnge önskad bruttolön (före skatt): "))
        
        # Beräkningar
        ag_avgifter = brutto_lon * (AGA / 100)
        tp_avgifter = brutto_lon * (TP / 100)
        se_avgifter = brutto_lon * (SE / 100)
        skatt = brutto_lon * (skattesats / 100)
        total_lon = brutto_lon + ag_avgifter + tp_avgifter + se_avgifter
        
        # Visa resultat
        print(f"\n{'='*50}")
        print(f"{'SAMMANSTÄLLNING':^50}")
        print(f"{'='*50}")
        print(f"{'Bruttolön:':<30}{brutto_lon:>18,.2f} kr")
        print(f"{'Arbetsgivaravgift:':<30}{ag_avgifter:>18,.2f} kr")
        print(f"{'Tjänstepension:':<30}{tp_avgifter:>18,.2f} kr")
        print(f"{'Semesterersättning:':<30}{se_avgifter:>18,.2f} kr")
        print(f"{f'Skatt ({skattesats}%):':<30}{skatt:>18,.2f} kr")
        print("-" * 50)
        print(f"{'Total lönekostnad:':<30}{total_lon:>18,.2f} kr")
        print("="*50 + "\n")
    
    except ValueError:
        print("❌ Felaktig inmatning. Ange tal.")


# === Funktion 3: Beräkna nettolön ===
def val_3(skattesats, valda_rader):
    """
    Beräknar nettolön baserat på bruttolön och skattesats.
    
    Args:
        skattesats (float): Skattesats för vald kommun
        valda_rader (list): Data för vald kommun (används ej här)
    
    Returns:
        tuple: (skatt, netto_lon) eller None vid avslut
    """
    while True:
        user_input = input("\nAnge din bruttolön ('q' för att avsluta): ").strip().upper()
        
        if user_input == "Q":
            return None
        
        try:
            bruttolon = float(user_input)
            skatt = bruttolon * skattesats / 100
            netto_lon = bruttolon - skatt
            
            print("\n" + "-"*40)
            print(f"Bruttolön: {bruttolon:,.2f} kr")
            print(f"Skattesats: {skattesats}%")
            print(f"Skatt: {skatt:,.2f} kr")
            print(f"Nettolön: {netto_lon:,.2f} kr")
            print("-"*40 + "\n")
            
            return skatt, netto_lon
        
        except ValueError:
            print("❌ Felaktig inmatning. Ange ett nummer.")


# === Funktion 4: Kvarvarande pengar i bolaget ===
def del_4(skattesats, valda_rader):
    """
    Beräknar kvarvarande pengar i bolaget efter lön och skatt.
    
    Args:
        skattesats (float): Skattesats för vald kommun
        valda_rader (list): Data för vald kommun (används ej här)
    """
    try:
        bruttolon = float(input("\nAnge önskad bruttolön (före skatt): "))
        
        # Beräkningar
        skatt = round(bruttolon * skattesats / 100, 2)
        netto_lon = round(bruttolon - skatt, 2)
        
        # Visa resultat
        print("\n" + "="*50)
        print("SAMMANSTÄLLNING".center(50))
        print("-"*50)
        print(f"Nettolön: {netto_lon:,.2f} kr")
        print(f"Betald skatt: {skatt:,.2f} kr")
        print("-"*50)
        print(f"Resterande pengar: {netto_lon:,.2f} kr")
        print("="*50 + "\n")
    
    except ValueError:
        print("❌ Felaktig inmatning. Ange tal.")


# === Funktion 5 & 6: Prognos med diagram ===
def steg_5_6():
    """
    Skapar ekonomisk prognos för året med tabell och diagram.
    Beräknar inkomst vid 100% och 80% beläggning samt semesterdagar.
    """
    # Konstanter (används inte aktivt men finns för framtida utveckling)
    MOMS = 0.25
    AGA = 0.3142
    TP = 0.045
    SE = 0.12
    SKATT = 0.3
    
    months = ["Januari", "Februari", "Mars", "April", "Maj", "Juni",
              "Juli", "Augusti", "September", "Oktober", "November", "December"]
    
    while True:
        # Hämta bruttolön
        bruttolon_input = input("\nAnge önskad bruttolön (före skatt, 'q' för att avsluta): ").strip()
        
        if bruttolon_input.lower() == "q":
            print("Avslutar prognos...")
            break
        
        try:
            brutto_lon = float(bruttolon_input)
        except ValueError:
            print("❌ Felaktig inmatning. Ange tal.")
            continue
        
        # Hämta timpris
        try:
            tim_pris = float(input("Mata in företagets timpris (exklusive moms): "))
        except ValueError:
            print("❌ Felaktig inmatning. Ange tal.")
            continue
        
        # Initialisera listor och totalsummor
        data = []
        total_100 = 0
        total_80 = 0
        total_semesterdagar = 0
        
        month_names = []
        income_100_values = []
        income_80_values = []
        
        print(f"\n{'='*50}")
        print(f"Exempel baserat på {tim_pris} kr timpris".center(50))
        print(f"{'='*50}\n")
        
        # Loopa genom varje månad
        for month in months:
            try:
                timmar_input = input(f"Ange antal arbetade timmar för {month} ('q' för att avsluta): ").strip()
                
                if timmar_input.lower() == "q":
                    break
                
                antal_timmar = float(timmar_input)
            except ValueError:
                print("❌ Fel inmatning, försök igen")
                continue
            
            # Beräkningar
            brutto_inkomst = tim_pris * antal_timmar
            inkomst_100 = brutto_inkomst
            inkomst_80 = brutto_inkomst * 0.8
            
            # Beräkna intjänade semesterdagar
            intjanade_semesterdagar = berakna_semesterdagar(antal_timmar)
            total_semesterdagar += intjanade_semesterdagar
            
            # Uppdatera totaler
            total_100 += inkomst_100
            total_80 += inkomst_80
            
            # Lagra data
            data.append([month, inkomst_100, inkomst_80, intjanade_semesterdagar])
            month_names.append(month)
            income_100_values.append(inkomst_100)
            income_80_values.append(inkomst_80)
        
        # Visa resultat om data finns
        if data:
            print("\n" + "="*70)
            print("RESULTAT".center(70))
            print("="*70)
            print(f"{'Månad':<15}{'100% Beläggning':>20}{'80% Beläggning':>20}{'Semester':>12}")
            print("-"*70)
            
            for item in data:
                print(f"{item[0]:<15}{item[1]:>18,.2f} kr{item[2]:>18,.2f} kr{item[3]:>10,.1f} d")
            
            print("\n" + "-"*70)
            print(f"{'Total intäkt (100%):':<35}{total_100:>20,.2f} kr")
            print(f"{'Realistisk intäkt (80%):':<35}{total_80:>20,.2f} kr")
            print("-"*70)
            print(f"{'Intjänade semesterdagar:':<35}{total_semesterdagar:>18,.1f} dagar")
            print("="*70 + "\n")
            
            # Fråga om diagram
            svar_diagram = input("Vill du se ett stapeldiagram med prognosen? ('Y'/'N'): ").upper().strip()
            
            if svar_diagram == "Y":
                visa_diagram(month_names, income_100_values, income_80_values)
            
            # Fråga om ny beräkning
            fortsatt = input("\nVill du göra en ny beräkning? ('Y'/'N'): ").upper().strip()
            if fortsatt == "N":
                print("Avslutar prognos...")
                break
        else:
            print("❌ Ingen data att visa.")
            break


def berakna_semesterdagar(timmar):
    """
    Beräknar intjänade semesterdagar baserat på arbetade timmar.
    
    Args:
        timmar (float): Antal arbetade timmar
    
    Returns:
        float: Antal intjänade semesterdagar
    """
    arbetsdagar = timmar / 8
    semesterdagar = arbetsdagar * 0.12
    return semesterdagar


def visa_diagram(month_names, income_100, income_80):
    """
    Skapar och visar stapeldiagram med inkomstprognos.
    
    Args:
        month_names (list): Lista med månadsnamn
        income_100 (list): Inkomst vid 100% beläggning
        income_80 (list): Inkomst vid 80% beläggning
    """
    plt.figure(figsize=(12, 6))
    
    # Skapa X-positioner för staplarna
    x = list(range(len(month_names)))
    width = 0.35
    
    # Skapa staplar
    plt.bar([i - width/2 for i in x], income_100, width, label='100% beläggning', color='#2E86AB')
    plt.bar([i + width/2 for i in x], income_80, width, label='80% beläggning', color='#A23B72')
    
    # Etiketter och titel
    plt.xlabel('Månad', fontsize=12)
    plt.ylabel('Fakturerat belopp (kr)', fontsize=12)
    plt.title('Fakturerat belopp per månad: 100% vs 80% beläggning', fontsize=14, fontweight='bold')
    
    # X-axelns etiketter med rotation för läsbarhet
    plt.xticks(x, month_names, rotation=45, ha='right')
    
    # Lägg till legend och rutnät
    plt.legend(loc='upper left')
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    
    # Justera layout för att undvika överlappning
    plt.tight_layout()
    
    # Visa diagram
    plt.show()


# === Avsluta-funktioner ===
def countdown():
    """Räknar ner från 3 sekunder innan programmet avslutas."""
    min_tid = 3
    for i in range(min_tid, 0, -1):
        sekunder = i % 60
        minuter = int(i / 60) % 60
        timmar = int(i / 3600)
        print(f"{timmar}:{minuter:02}:{sekunder:02}")
        time.sleep(1)


def avsluta():
    """Avslutar programmet med en rolig animation."""
    time.sleep(0.5)
    print("\n💥 Självförstörelse om...")
    countdown()
    print("NU SMÄLLER DET!!!")
    time.sleep(0.5)
    print("\n🎆 * BOOM * 🎆")
    print("\nTack för att du använde programmet! Hej då! 👋\n")
    exit()
