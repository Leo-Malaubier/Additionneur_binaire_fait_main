class port_logic:
    """"
    def __init__(self,Iam):
        if not hasattr(self, Iam):
            raise ValueError(f"la méthode '{Iam}' n'est pas définie dans la classe")
        self.Iam = Iam
    def __getattr__(self,name):
        if name == self.Iam:
            return gatattr(self.__class__, name).__get__(self)
        raise AttributeError(f"Accès interdit à la méthode '{name}'. Seule '{self.allowed_method}' est autorisée.")
        """
    def _or(self,E1,E2):
        if E1== "0" and E2 =="0":
            return "0"
        else:
            return "1"
    def nor(self,E1,E2):
        if E1== "0" and E2 == "0":
            return "1"
        else:
            return "0"
    def xor(self,E1,E2):
        if E1 != E2:
            return "1"
        else:
            return "0"
    def xnor(self,E1,E2):
        if E1 == E2:
            return "1"
        else:
            return "0"
    def _and(self,E1,E2):
        if E1 == "1" and E2 =="1":
            return "1"
        else:
            return "0"

    def nand(self,E1,E2):
        if E1 == "1" and E2 =="1":
            return "0"
        else:
            return "1"

    def _not(self,E):
        if E == "1":
            return "0"
        else:
            return "1"
