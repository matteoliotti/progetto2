#parte 1

nome_M='Mario'
cognome_M='Rossi'
eta_M=45
CodiceFiscale_M='RSSMRA80H12G337L'
peso_M=78.5
analisi_M=['emocromo','glicemia','colesterolo']

nome_L='Luigi'
cognome_L='Rossi'
eta_L=40
CodiceFiscale_L='RSSLGI85M23G337T'
peso_L=82
analisi_L=['ECG','Antigene Prostatico Specifico','colesterolo']

nome_C='Crisina'
cognome_C='Bianchi'
eta_C=22
CodiceFiscale_C='BNCCRS03R71F205A'
peso_C=60.5
analisi_C=['glicemia','ferritina','vitamina D']             #cambiati per poter lavorare più comodamente con l'array

#parte 2
class paziente:
    def __init__(self,nome,cognome,eta,CF,peso,analisi_effettuate):
        self.nome=nome
        self.cognome=cognome
        self.eta=eta
        self.CF=CF
        self.peso=peso
        self.analisi_effettuate=analisi_effettuate
    def scheda_personale(self):
        return f'\nNome: {self.nome}\nCognome: {self.cognome}\nEta: {self.eta}\nCF: {self.CF}\nPeso: {self.peso}\nAnalisi effettuate: {self.analisi_effettuate}\n'

class medico:
    def __init__(self,nome,cognome,specializzazione):
        self.nome=nome
        self.cognome=cognome
        self.specializzazione=specializzazione
    def visita_paziente(self,paziente):
        print(f'\nIl Dott. {self.nome} {self.cognome} sta al momento visitando, {paziente.nome} {paziente.cognome}\n')

class analisi:
    def __init__(self,controllo,risultato):
        self.controllo=controllo
        self.risultato=risultato
    def valuta(self,norma):
        if self.risultato>norma[0] and self.risultato<norma[1]:
            print(f'\nSono arrivati i risultati del test per {self.controllo} ed è tutto in ordine\n')
        else:
            print(f'\nSono arrivati i risultati del test per {self.controllo} e purtroppo non sono buoni\n')

#Tina=paziente(nome_C,cognome_C,eta_C,CodiceFiscale_C,peso_C,analisi_C)
#print(Tina.scheda_personale())
#Dott_Mario=medico('Mario','Mario','medico di base')
#Dott_Mario.visita_paziente(Tina)                                           test per le classi
#ferritina=analisi('ferritina',82)
#ferritina.valuta([13,150])

#parte 3

import numpy as np

risultati_ferritina=np.random.randint(0,501,(10))
media_f=np.mean(risultati_ferritina)
max_f=np.max(risultati_ferritina)
min_f=np.min(risultati_ferritina)
std_f=np.std(risultati_ferritina)

#print(f'\n{risultati_ferritina}\n\nLa media dei valori è:{media_f}, da un minimo di {min_f}, ad un massimo di {max_f} con uno squarto quadratico medio di {std_f}\n')

#parte 4

class neo_paziente(paziente):
    def __init__(self,nome,cognome,eta,CF,peso,analisi_effettuate,risultati_analisi):
        self.nome=nome
        self.cognome=cognome
        self.eta=eta
        self.CF=CF
        self.peso=peso
        self.analisi_effettuate=analisi_effettuate
        self.risultati_analisi=risultati_analisi
    def statistiche_analisi(self):
        media=np.mean(self.risultati_analisi)
        max=np.max(self.risultati_analisi)
        min=np.min(self.risultati_analisi)
        std=np.std(self.risultati_analisi)
        return f'\nMedia: {media}\nMax: {max}\nMin: {min}\nStd: {std}\n'

risultati_C=np.array([80,82,63])

#Tina=neo_paziente(nome_C,cognome_C,eta_C,CodiceFiscale_C,peso_C,analisi_C,risultati_C)
#def nuova_scheda(self):
#        return f'\nNome: {self.nome}\nCognome: {self.cognome}\nEta: {self.eta}\nCF: {self.CF}\nPeso: {self.peso}\nAnalisi effettuate: {self.analisi_effettuate}\nRisultai analisi: {self.risultati_analisi}\n'
#neo_paziente.scheda_personale=nuova_scheda
#print(Tina.scheda_personale())

#Dott_Mario=medico('Mario','Mario','medico di base')
#Dott_Mario.visita_paziente(Tina)
#print(f"Sono arrivati i risultati delle analisi: {Tina.risultati_analisi}\n",Tina.statistiche_analisi())           test per le classi