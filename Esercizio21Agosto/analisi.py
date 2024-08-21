import re

def analisi_parole(stringa):

    stringa1=stringa.lower()
    punteggiatura=","
    stringa_senza_punt=(re.sub(punteggiatura," ",stringa1))
    lista_parole= stringa_senza_punt.split()

    analisi_parole={"ciao":lista_parole.count("ciao"),"sono":lista_parole.count("sono"),"molto":lista_parole.count("molto"),"felice":lista_parole.count("felice")}
    
    return analisi_parole


print(analisi_parole("Ciao ciao,sono molto molto felice"))

    