from Porte_logic import port_logic
class calc(port_logic):
    def inverse(self,nb):
        result=[]
        for i in range(7,-1,-1):
            binar = self._not(nb[i])
            result.append(binar)
        return ''.join(reversed(result))[-8:]
    def add(self,b1,b2):#1bit
        sum = self.xor(b1,b2)
        carryover = self._and(b1,b2)
        return sum,carryover
    def full_add(self,b1,b2,carryover): #1bit avec calcule de retenue
        sum1, carry1 = self.add(b1,b2)
        sum2, carry2 = self.add(sum1,carryover)
        carry_out = self._or(carry1, carry2)
        return sum2, carry_out

    def adder_8bit(self,nb1,nb2):
        carryover = "0"
        result=[]
        for i in range(7,-1,-1):
            a = nb1[i]
            b = nb2[i]
            sum, carryover = self.full_add(a,b,carryover)
            result.append(sum)
        if carryover:
            result.append(carryover)
        return ''.join(reversed(result))[-8:]

    def sub_8bit(self,nb1,nb2): #-soustraction: on prend notre nombre binaire, on l'inverse et on ajoute +1
        nb2 = self.inverse(nb2)
        nb2 = self.adder_8bit(nb2,"00000001") #+1
        return self.adder_8bit(nb1,nb2)

    def mult_8bit(self,nb1,nb2):
        print("attention, si le nombre est trop grand, il y a un risque d'overflo")
        value = "00000000"
        for i in range(7,-1,-1):
            if nb2[i] == "1":
                #print(f"addition de nb1:{nb1} et nb2:{value}")
                value = self.adder_8bit(nb1,value)
            nb1= nb1 + "0"
            nb1 = nb1[1:]
        return value

    def div_8bit(self,nb1,nb2):
        pass
        #return result,carryover
"""
if __name__ == "__main__":

    bin = "00000001"
    bin1 = "00000011"
    clacule = calc()

    result=clacule.adder_8bit(bin,bin1)

    print(f"Résultat d'exécution : {result}")
"""
