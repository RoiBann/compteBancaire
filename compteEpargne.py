from compte import Compte


class CompteEpargne(Compte):

    def __init__(self, pourcentage_interets):
        self._pourcentage_interets = pourcentage_interets

    def get_pourcentage_interets(self):
        return self._pourcentage_interets

    def set_pourcentage_interets(self):
        return self._pourcentage_interets