#vraag 4 & 5
def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs *(1 - korting)
    aanbieding = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs:.2f} euro"
    return aanbieding

#vraag 6 & 7
def inkomsten_totaal(inkomsten):
    btw = 0.09
    totaal = sum(inkomsten)
    btw_bedrag = totaal * btw
    totaal_incl_btw = totaal * (1+ btw)
    resultaat = f"Het totaal van alle inkomsten van deze week is {totaal_incl_btw:.2f} euro, waarover {btw_bedrag:.2f} euro btw betaald dient te worden."
    return (resultaat)

#vraag 8
def laag_en_hoog(mijn_lijst):
    return max(mijn_lijst), min(mijn_lijst)

#vraag 9 & 10
def gemiddelde(mijn_lijst):
    totaal = sum(mijn_lijst)
    gemiddelde_bedrag = totaal / 2
    totaal_gemiddelde = f"De gemiddelde inkomsten deze week zijn {gemiddelde_bedrag:.2f} euro."
    return totaal_gemiddelde

#vraag 11
def meervoudig(invoer_lijst):
    resultaat = laag_en_hoog(invoer_lijst)
    return resultaat

#vraag 12
from algemene_functies import mijn_functie_2

def combinatie(invoer_lijst_2):
    korte_lijst = meervoudig(invoer_lijst_2)
    resultaat = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return resultaat