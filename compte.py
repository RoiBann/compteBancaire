class Compte:

    def __init__(self, numero_compte, nom_proprietaire, solde):
        self._numero_compte = numero_compte
        self._nom_proprietaire = nom_proprietaire
        self._solde = solde
    def play(self):
        print('coucou')