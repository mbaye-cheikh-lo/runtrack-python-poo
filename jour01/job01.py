class Livre:
    def __init__(self,titre,auteur,npages):
        self.__titre=titre
        self.__auteur=auteur
        self.__npage=npages
        self.__disponible=True
    def get_titre(self):
        return self.__titre
    def get_auteur(self):
        return self.__auteur
    def get_npages(self):
        return self.__npage
    
    def set_titre(self,nouveau_titre):
        self.__titre=nouveau_titre
    def set_auteur(self,nouveau_auteur):
        self.__auteur=nouveau_auteur
    def set_npages(self,nouveau_npage):
        if isinstance(nouveau_npage,str) and nouveau_npage>0:
            self.__npage=nouveau_npage
        else:
            print("ERREUR")

    # def get_disponible(self):
    #     return self.__disponible
    
    def verification(self):
        return self.__disponible
    
    def emprunter(self):
        if self.verification():
            self.__disponible=False
            print("le livre est emprunté")
        else:
            print("le livre n'est pas disponible")

    def rendre(self):
        if  not self.verification():
            self.__disponible=True
            print("le livre a ete rendu")
        else:
            print("le livre est disponible")

