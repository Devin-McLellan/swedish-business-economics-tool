"""
Ekonomiprogram - Huvudfil
Ett program för ekonomiska beräkningar baserat på svenska skattesatser.

Författare: [Kevin McLellan]
Datum: 2026-01-13
"""

import time
import matplotlib.pyplot as plt
import numpy as np
import csv
import ekonomi_funktioner as ef


def main():
    """
    Huvudfunktion för ekonomiprogrammet.
    
    Startar programmet genom att:
    1. Visa välkomstmeddelande
    2. Låta användaren välja kommun från skattetabellen
    3. Starta huvudmenyn med valda inställningar
    """
    # Visar välkomstext när programmet startar
    ef.welcome()
    
    # Låt användaren välja kommun från skattetabell
    # valda_rader innehåller all data för den valda kommunen
    # skattesats är kommunens procentsats
    valda_rader, skattesats = ef.val_kommun(filnamn='skattetabell.csv')
    
    # Kontrollera om skattesatsen hittades
    # Om skattesatsen saknas (None) används ett standardvärde på 30%
    if skattesats is None:
        print("⚠️  Skattesatsen kunde inte hämtas. Använder standardvärde på 30%")
        skattesats = 30.0
    
    # Starta huvudmenysystemet där användaren kan välja olika funktioner
    ef.meny(skattesats, valda_rader)


if __name__ == "__main__":
    main()
