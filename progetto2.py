#parte 1

nome_M='Mario'
cognome_M='Rossi'
eta_M=45
CodiceFiscale_M='RSSMRA80H12G337L'
peso_M=78.5
analisi_M=['ferritina','glicemia','colesterolo']

nome_L='Luigi'
cognome_L='Rossi'
eta_L=40
CodiceFiscale_L='RSSLGI85M23G337T'
peso_L=82
analisi_L=['ECG','PSA','colesterolo']

nome_C='Cristina'
cognome_C='Bianchi'
eta_C=22
CodiceFiscale_C='BNCCRS03R71F205A'
peso_C=60.5
analisi_C=['glicemia','ferritina','vitamina D']

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
        print(f'\n{paziente.nome} {paziente.cognome} visitato/a dal/dalla Dott./Dott.ssa {self.nome} {self.cognome}')

class analisi:
    def __init__(self,paziente,controllo,risultato):
        self.controllo=controllo
        self.risultato=risultato
        self.paziente=paziente
    def valuta(self,norma):
        if self.risultato>norma[0] and self.risultato<norma[1]:
            print(f'Sig/Sig.ra {self.paziente.nome}, sono arrivati i risultati del test per {self.controllo} ed è tutto in ordine\n')
        else:
            print(f'Sig/Sig.ra {self.paziente.nome}, sono arrivati i risultati del test per {self.controllo} e purtroppo non sono buoni\n')

#Tina=paziente(nome_C,cognome_C,eta_C,CodiceFiscale_C,peso_C,analisi_C)
#print(Tina.scheda_personale())

#Dott_Mario=medico('Mario','Mario','medico di base')

#Dott_Mario.visita_paziente(Tina)                                           test per le classi
#ferritina_C=analisi(Tina,Tina.analisi_effettuate[1],82)
#ferritina_C.valuta([13,150])

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
        return f'\nRisultati analisi del sig/sir.ra {self.nome}:\n{self.risultati_analisi}\nMedia: {media}\nMax: {max}\nMin: {min}\nStd: {std}\n'

#Tina=neo_paziente(nome_C,cognome_C,eta_C,CodiceFiscale_C,peso_C,analisi_C,np.array([80,82,63]))
def nuova_scheda(self):
        return f'\nNome: {self.nome}\nCognome: {self.cognome}\nEta: {self.eta}\nCF: {self.CF}\nPeso: {self.peso}\nAnalisi effettuate: {self.analisi_effettuate}\nRisultai analisi: {self.risultati_analisi}'
neo_paziente.scheda_personale=nuova_scheda
#print(Tina.scheda_personale())

#Dott_Mario=medico('Mario','Mario','medico di base')
#Dott_Mario.visita_paziente(Tina)
#print(f"Sono arrivati i risultati delle analisi: {Tina.risultati_analisi}\n",Tina.statistiche_analisi())           test per le classi

#parte 5

print("\n---------------------\npazienti:\n---------------------")

Tina=neo_paziente(nome_C,cognome_C,eta_C,CodiceFiscale_C,peso_C,analisi_C,np.array([80,82,63]))
Mario=neo_paziente(nome_M,cognome_M,eta_M,CodiceFiscale_M,peso_M,analisi_M,np.array([300,120,180]))
Luigi=neo_paziente(nome_L,cognome_L,eta_L,CodiceFiscale_L,peso_L,analisi_L,np.array([70,2.2,230]))
Dario=neo_paziente('Dario','Lampa',88,'LMPDRA37A20H163T',90,['ECG','vitamina d','glicemia'],np.array([67,45,150]))
Dina=neo_paziente('Dina','Lampa',37,'LMPDNA88T04H501N',71.3,['PSA','colesterolo','ferritina'],np.array([2.0,230,80]))

print(Tina.scheda_personale())
print(Mario.scheda_personale())
print(Luigi.scheda_personale())
print(Dario.scheda_personale())
print(Dina.scheda_personale())

print("\n---------------------\npresi in cura da:\n---------------------")

Dott_Mario=medico('Mario','Mario','medico di base')
Dott_Pino=medico('Pino','Silvestri','cardiologo')
Dott_ssa_Sofia=medico('Sofia','Denaltro','chirurgia')

Dott_Mario.visita_paziente(Tina)
Dott_Mario.visita_paziente(Mario)
Dott_Pino.visita_paziente(Dario)
Dott_Pino.visita_paziente(Luigi)
Dott_ssa_Sofia.visita_paziente(Dina)

print("\n---------------------\nconclusioni:\n---------------------")

glicemia_T=analisi(Tina,Tina.analisi_effettuate[0],Tina.risultati_analisi[0])
ferritina_T=analisi(Tina,Tina.analisi_effettuate[1],Tina.risultati_analisi[1])
vitaminaD_T=analisi(Tina,Tina.analisi_effettuate[2],Tina.risultati_analisi[2])

ferritina_M=analisi(Mario,Mario.analisi_effettuate[0],Mario.risultati_analisi[0])
glicemia_M=analisi(Mario,Mario.analisi_effettuate[1],Mario.risultati_analisi[1])
colesterolo_M=analisi(Mario,Mario.analisi_effettuate[2],Mario.risultati_analisi[2])

ECG_L=analisi(Luigi,Luigi.analisi_effettuate[0],Luigi.risultati_analisi[0])
PSA_L=analisi(Luigi,Luigi.analisi_effettuate[1],Luigi.risultati_analisi[1])
colesterolo_L=analisi(Luigi,Luigi.analisi_effettuate[2],Luigi.risultati_analisi[2])

ECG_Da=analisi(Dario,Dario.analisi_effettuate[0],Dario.risultati_analisi[0])
vitaminaD_Da=analisi(Dario,Dario.analisi_effettuate[1],Dario.risultati_analisi[1])
glicemia_Da=analisi(Dario,Dario.analisi_effettuate[2],Dario.risultati_analisi[2])

PSA_Di=analisi(Dina,Dina.analisi_effettuate[0],Dina.risultati_analisi[0])
colesterolo_Di=analisi(Dina,Dina.analisi_effettuate[1],Dina.risultati_analisi[1])
ferritina_Di=analisi(Dina,Dina.analisi_effettuate[2],Dina.risultati_analisi[2])

print(Tina.statistiche_analisi())
glicemia_T.valuta([70,99])
ferritina_T.valuta([13,200])
vitaminaD_T.valuta([30,100])

print(Mario.statistiche_analisi())
ferritina_M.valuta([20,400])
glicemia_M.valuta([70,99])
colesterolo_M.valuta([0,200])

print(Luigi.statistiche_analisi())
ECG_L.valuta([60,100])
PSA_L.valuta([0,2.5])
colesterolo_L.valuta([0,200])

print(Dario.statistiche_analisi())
ECG_Da.valuta([60,100])
vitaminaD_Da.valuta([30,100])
glicemia_Da.valuta([70,99])

print(Dina.statistiche_analisi())
colesterolo_Di.valuta([0,200])
PSA_Di.valuta([0,2.5])
ferritina_Di.valuta([13,200])