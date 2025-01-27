import time
from calculateur import calc
from controller import controller
#retenue = carryover
class main:
    def __init__(self):
        self.controller = controller()
        self.calculateur = calc()
        self.run()
    def run(self):
        while True:
            try:
                task = input("donner moi quelque chose a faire: ")
                if task == "ADD" or task =="SUB" or task=="MULT":
                    nb1 = input("donner moi un premier nombre bianire: ")
                    nb1=self.controller.verif(nb1)
                    nb2= input("donner moi un second nombre bianire: ")
                    nb2=self.controller.verif(nb2)
                    if task =="ADD":
                        print(self.calculateur.adder_8bit(nb1,nb2))
                    if task == "SUB":
                        print(self.calculateur.sub_8bit(nb1,nb2))
                    if task == "MULT":
                        print(self.calculateur.mult_8bit(nb1,nb2))
                elif task == "END":
                    return False
                else:
                    print("commande non reconnue")
            except Exception as e:
                print(f"Erreur main : {e}")

if __name__ == "__main__":
    salut = main()
    """
    bin = "001"
    bin1 = "0011"
    clacule = calc()
    st=time.time()
    result=clacule.adder_8bit(bin,bin1)
    et = time.time()
    execution_time = et - st
    print(f"Résultat d'exécution : {result} en {execution_time:.10f} secondes")
    """
