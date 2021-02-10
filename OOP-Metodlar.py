class Yazılımcı():

    def __init__(self,isim,soyisim,maaş,diller):
        self.isim = isim
        self.soyisim = soyisim
        self.maaş = maaş
        self.diller = diller

    def BilgileriGöster(self):
        print("""
        Yazılımcı objesinin özellikleri
        
        İsim: {}
        
        Soyisim: {}
        
        Maaş: {}
        
        Bildiği Diller: {}
        """.format(self.isim,self.soyisim,self.maaş,self.diller))

yazılımcı1 = Yazılımcı("Emirhan","Mutlu",5000,["Python","Java","C","C++"])

yazılımcı2 = Yazılımcı("Ahmet","Aydın",4000,["HTML","CSS","Javascript"])

yazılımcı1.BilgileriGöster()
yazılımcı2.BilgileriGöster()
