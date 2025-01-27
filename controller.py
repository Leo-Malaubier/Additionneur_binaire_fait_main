class controller: #ajouter la vérification d'utilisation de nombre binaire uniquement.
    def complete(self,nb):
        if len(nb)<8 :
            print("resizing ",len(nb))
            nb = nb.zfill(8)
        return nb
    def verif_out_of_range(self,nb):
        if len(nb)>8:
            print("nb out of range !")
            return False
        else:
            return True

    def verif(self,nb1,nb2=None):
        if nb2 != None:
            if not self.verif_out_of_range(nb1):
                return
            if not self.verif_out_of_range(nb2):
                return
            nb1 = self.complete(nb1)
            nb2 = self.complete(nb2)
            return nb1,nb2
        else:
            if not self.verif_out_of_range(nb1):
                return
            nb1 = self.complete(nb1)
            return nb1
