import sys
import os

# Notizen
# Fachauswahl: 0 = Zurück zum Hauptmenü funktioniert nicht
# Schleife bei Fachauswahl 
# Ausnahmebehandlung

# Listen
ListeAWPSchriftlich = []
ListeAWPMuendlich = []
ListeITSSchriftlich = []
ListeITSMuendlich = []
ListeVSSchriftlich = []
ListeVSMuendlich = []
ListeBWPSchriftlich = []
ListeBWPMuendlich = []
ListeEnglischSchriftlich = []
ListeEnglischMuendlich = []
ListeSportSchriftlich = []
ListeSportMuendlich = []
ListeDeutschSchriftlich = []
ListeDeutschMuendlich = []
ListeReligionSchriftlich = []
ListeReligionMuendlich = []
ListeSozialkundeSchriftlich = []
ListeSozialkundeMuendlich = []

# cls = clear() Funktion
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# Hauptmenü und Auswahl
def Hauptmenue():
    cls()
    print("----------------------Menüführung----------------------")
    print("-------------------------------------------------------")
    print()
    print("<1> Noteneingabe")
    print("<2> Noten ausgeben")
    print("<3> Notenschnitt berechnen")
    print("<0> Programm beenden")
    print("Bitte geben sie Ihre Wahl ein:")

    iAuswahl = int(input())
    return iAuswahl

# Fachauswahl
def FaecherAuswahl():
    print("Fächerauswahl")
    print("<1> AWP")
    print("<2> ITS")
    print("<3> VS")
    print("<4> BWP")
    print("<5> Englisch")
    print("<6> Sport")
    print("<7> Deutsch")
    print("<8> Religion")
    print("<9> Sozialkunde")
    print("<0> Zurück zum Hauptmenü")

    iFach = int(input())
    return iFach

# Notenart
def Notenart():
    print("Schriftliche (s) oder mündliche (m) Noten?")
    while True:
        cNotenart = input()
        if TestNotenart(cNotenart) == 0:
            break
    return cNotenart

# Test Notenart
# SPÄTER MIT AUSNAHMENBEHANDLUNG ERSETZEN
def TestNotenart(cNotenart):
    i = 0
    if cNotenart == 's' or cNotenart == 'm':
        i = 0
    else:
        print("Bitte 's' oder 'm' eingeben.")
        i = 1

    return i

# Auswahl um die richtige Liste zu erstellen
def Auswahl(iFach, cNotenart):
    #AWP
    if iFach == 1:
        global ListeAWPSchriftlich
        global ListeAWPMuendlich
        if cNotenart == 's':
            ListeAWPSchriftlich = ListeErstellen(cNotenart)
        elif cNotenart == 'm':
            ListeAWPMuendlich = ListeErstellen(cNotenart)

    # ITS
    elif iFach == 2:
        global ListeITSSchriftlich
        global ListeITSMuendlich
        if cNotenart == 's':
            ListeITSSchriftlich = ListeErstellen(cNotenart)
        elif cNotenart == 'm':
            ListeITSMuendlich = ListeErstellen(cNotenart)
    # VS
    elif iFach == 3:
        global ListeVSSchriftlich
        global ListeVSMuendlich
        if cNotenart == 's':
            ListeVSSchriftlich = ListeErstellen(cNotenart)
        elif cNotenart == 'm':
            ListeVSMuendlich = ListeErstellen(cNotenart)

    # BWP
    elif iFach == 4:
        global ListeBWPSchriftlich
        global ListeBWPMuendlich
        if cNotenart == 's':
            ListeBWPSchriftlich = ListeErstellen(cNotenart)
        elif cNotenart == 'm':
            ListeBWPMuendlich = ListeErstellen(cNotenart)

    # Englisch
    elif iFach == 5:
        global ListeEnglischSchriftlich
        global ListeEnglischMuendlich
        if cNotenart == 's':
            ListeEnglischSchriftlich = ListeErstellen(cNotenart)
        elif cNotenart == 'm':
            ListeEnglischMuendlich = ListeErstellen(cNotenart)

    # Sport
    elif iFach == 6:
        global ListeSportSchriftlich
        global ListeSportMuendlich
        if cNotenart == 's':
            ListeSportSchriftlich = ListeErstellen(cNotenart)
        elif cNotenart == 'm':
            ListeSportMuendlich = ListeErstellen(cNotenart)

    # Deutsch
    elif iFach == 7:
        global ListeDeutschSchriftlich
        global ListeDeutschMuendlich
        if cNotenart == 's':
            ListeDeutschSchriftlich = ListeErstellen(cNotenart)
        elif cNotenart == 'm':
            ListeDeutschMuendlich = ListeErstellen(cNotenart)

    # Religion
    elif iFach == 8:
        global ListeReligionSchriftlich
        global ListeReligionMuendlich
        if cNotenart == 's':
            ListeReligionSchriftlich = ListeErstellen(cNotenart)
        elif cNotenart == 'm':
            ListeReligionMuendlich = ListeErstellen(cNotenart)

    # Sozialkunde
    elif iFach == 9:
        global ListeSozialkundeSchriftlich
        global ListeSozialkundeMuendlich
        if cNotenart == 's':
            ListeSozialkundeSchriftlich = ListeErstellen(cNotenart)
        elif cNotenart == 'm':
            ListeSozialkundeMuendlich = ListeErstellen(cNotenart)

    # Zurück zum Hauptmenü
    # ENDLOSSCHLEIFE DIE ZU RICHTIGER EINGABE ZWINGT in Faecher()!!!!
    else:
        main()

# Liste erstellen
def ListeErstellen(cNotenart):
    Liste = []
    if cNotenart == 's':
        print("Bitte Anzahl der schriftlichen Noten eingeben.")
    elif cNotenart == 'm':
        print("Bitte Anzahl der mündlichen Noten eingeben.")
    
    n = int(input())
    for i in range(0, n):
       i += 1
       print("Bitte die " + str(i) + ". Note eingeben:")
       i -= 1
       i = int(input())
       Liste.append(i)

    return Liste
            
# Auswahl für die Notenausgabe
def AuswahlAusgabe(iFach, cNotenart):
    # AWP
    if iFach == 1:
        NotenAusgeben(ListeAWPSchriftlich, ListeAWPMuendlich, cNotenart)
    # ITS
    elif iFach == 2:
        NotenAusgeben(ListeITSSchriftlich, ListeITSMuendlich, cNotenart)
    # VS
    elif iFach == 3:
        NotenAusgeben(ListeVSSchriftlich, ListeVSMuendlich, cNotenart)
    # BWP
    elif iFach == 4:
        NotenAusgeben(ListeBWPSchriftlich, ListeBWPMuendlich, cNotenart)
    # Englisch
    elif iFach == 5:
        NotenAusgeben(ListeEnglischSchriftlich, ListeEnglischMuendlich, cNotenart)
    # Sport
    elif iFach == 6:
        NotenAusgeben(ListeSportSchriftlich, ListeSportMuendlich, cNotenart)
    # Deutsch
    elif iFach == 7:
        NotenartAugeben(ListeDeutschSchriftlich, ListeDeutschMuendlich, cNotenart)
    # Religion
    elif iFach == 8:
        NotenAusgeben(ListeReligionSchriftlich, ListeReligionMuendlich, cNotenart)
    # Sozialkunde
    elif iFach == 9:
        NotenAusgeben(ListeSozialkundeSchriftlich, ListeSozialkundeMuendlich, cNotenart)

# Noten ausgeben
def NotenAusgeben(ListeSchriftlich, ListeMuendlich, cNotenart):
    if cNotenart == 's':
        i = len(ListeSchriftlich)
        print(i)
        for j in range(0, i):
            print("Die Note an der Position " + str(j) + " ist:")
            print(ListeSchriftlich[j])
    elif cNotenart == 'm':
        i = len(ListeMuendlich)
        for j in range(0, i):
            print("Die Note an der Position " + str(j) + " ist:")
            print(ListeMuendlich[j])
    a = input()

def AuswahlDurchschnittBerechnen(iFach):
    # AWP
    if iFach == 1:
        DurchschnittBerechnen(ListeAWPSchriftlich, ListeAWPMuendlich)
    # ITS
    elif iFach == 2:
        DurchschnittBerechnen(ListeITSSchriftlich, ListeITSMuendlich)
    # VS
    elif iFach == 3:
        DurchschnittBerechnen(ListeVSSchriftlich, ListeVSMuendlich)
    # BWP
    elif iFach == 4:
        DurchschnittBerechnen(ListeBWPSchriftlich, ListeBWPMuendlich)
    # Englisch
    elif iFach == 5:
        DurchschnittBerechnen(ListeEnglischSchriftlich, ListeEnglischMuendlich)
    # Sport
    elif iFach == 6:
        DurchschnittBerechnen(ListeSportSchriftlich, ListeSportMuendlich)
    # Deutsch
    elif iFach == 7:
        DurchschnittBerechnen(ListeDeutschSchriftlich, ListeDeutschMuendlich)
    # Religion
    elif iFach == 8:
        DurchschnittBerechnen(ListeReligionSchriftlich, ListeReligionMuendlich)
    # Sozialkunde
    elif iFach == 9:
        DurchschnittBerechnen(ListeSozialkundeSchriftlich, ListeSozialkundeMuendlich)

def DurchschnittBerechnen(ListeSchriftlich, ListeMuendlich):
    dDurchschnittsNote = 0.0
    iZeugnisNote = 0
    # Test ob Listen existieren
    if not ListeSchriftlich:
        print("Die Liste für die schriftlichen Noten ist leer, Bitte über das Hauptmenü erstellen.")
        input()
        return
    if not ListeMuendlich:
        print("Die Liste für die mündlichen Noten ist leer. Bitte über das Hauptmenü erstellen.")
        input()
    
    # Größe bestimmen
    iAnzahlSchriftlicherNoten = len(ListeSchriftlich)
    iAnzahlMuendlicherNoten = len(ListeMuendlich)

    # Aufsummieren
    dSummeSchriftlich = sum(ListeSchriftlich)
    dSummeMuendlich = sum(ListeMuendlich)

    # Ausgabe Durchschnitt und Zeugnisnote
    if iAnzahlMuendlicherNoten >= (iAnzahlSchriftlicherNoten*2):
        dDurchschnittsNote = (((dSummeSchriftlich / iAnzahlSchriftlicherNoten) + (dSummeMuendlich / iAnzahlMuendlicherNoten)) / 2)
        iZeugnisNote = KonvertiereInZeugnisNote(dDurchschnittsNote)
        print("Notendurchschnitt: " + str(dDurchschnittsNote) + "; Zeugnisnote: " + str(iZeugnisNote))
        input()
    else:
        dDurchschnittsNote = (((dSummeSchriftlich / iAnzahlSchriftlicherNoten * 2) + (dSummeMuendlich / iAnzahlMuendlicherNoten)) / 3)
        iZeugnisNote = KonvertiereInZeugnisNote(dDurchschnittsNote)
        print("Notendurchschnitt: " + str(dDurchschnittsNote) + "; Zeugnisnote: " + str(iZeugnisNote))
        input()

def KonvertiereInZeugnisNote(dDurchschnittsNote):
    iNote = 0
    if dDurchschnittsNote >= 1.0 and dDurchschnittsNote < 1.5:
        iNote = 1
    elif dDurchschnittsNote >= 1.5 and dDurchschnittsNote < 2.5:
        iNote = 2
    elif dDurchschnittsNote >= 2.5 and dDurchschnittsNote < 3.5:
        iNote = 3
    elif dDurchschnittsNote >= 3.5 and dDurchschnittsNote <= 4.0:
        iNote = 4
    elif dDurchschnittsNote > 4.0 and dDurchschnittsNote <= 5.0:
        iNote = 5
    elif dDurchschnittsNote > 5.0 and dDurchschnittsNote <= 6.0:
        iNote = 6
    else:
        print("Notendurchschnitt ist außerhalb eines sinnvollen Bereiches.")

    return iNote

# Steuerung des Programms
def main():
    iAuswahl = 1
    while iAuswahl != 0:
        iAuswahl = Hauptmenue()
        # Noteneingabe
        if iAuswahl == 1:
            # Fachauswahl
            iFach = FaecherAuswahl()
            # Auswahl Notenart
            cNotenart = Notenart()
            # Listen erstellen
            Auswahl(iFach, cNotenart)
        # Noten ausgebens
        elif iAuswahl == 2:
            # Fachauswahl
            iFach = FaecherAuswahl()
            # Notenart
            cNotenart = Notenart()
            # Noten ausgeben
            AuswahlAusgabe(iFach, cNotenart)
        # Notenschnitt berechnen
        elif iAuswahl == 3:
            # Fachauswahl
            iFach = FaecherAuswahl()
            # Auswahl für die Berechnung
            AuswahlDurchschnittBerechnen(iFach)
        if iAuswahl == 0:
            break
            

if __name__ == "__main__":
    main()
