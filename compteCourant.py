from compte import Compte


class CompteCourant (Compte):

    def __init__(self, autorisation_decouvert, pourcentage_agios):
        self._autorisation_decouvert = autorisation_decouvert
        self._pourcentage_agios = pourcentage_agios

    def appliquer_agios(self):
        return

    def get_autorisation_decouvert(self):
        return self._autorisation_decouvert

    def get_pourcentage_agios(self):
        return self._pourcentage_agios

    def set_appliquer_agios(self):
        return  self.appliquer_agios()

    def set_autorisation_decouvert(self):
        return self._autorisation_decouvert

    def set_pourcentage_agios(self):
        return self._pourcentage_agios




