class Main:
    def __init__(self, att1="public", att2="private (within class)"):
        self.publ_att = att1
        self.__priv_att = att2  # use 2x underscore as a convention
        self._prot_att = "protected (within inherited classes)"  # use 1x underscore as a convention

    def get_priv_att(self):
        return self.__priv_att

    def set_priv_att(self):
        self.__priv_att = "setted private (within class)"


class Main2(Main):
    def get_prot_att(self):
        return self._prot_att

    def set_prot_att(self):
        self._prot_att = "setted protected (within inherited classes)"


main = Main()
print(main.publ_att)
print(main.get_priv_att())

main2 = Main2()
print(main2.get_prot_att())

print("\n###Hacking attributes directly:")
main.publ_att = "hacked"
main.__priv_att = "hacked"
main._prot_att = "hacked"
print(main.publ_att)
print(main.get_priv_att())
print(main2.get_prot_att())

print("\n###Setters:")
main.set_priv_att()
main2.set_prot_att()
print(main.get_priv_att())
print(main2.get_prot_att())


class Main3:
    def __init__(self, attribute1, attribute2):
        self.__attribute1 = attribute1
        self.__attribute2 = attribute2

    @property
    def attribute1(self):
        return self.__attribute1

    @property
    def attribute2(self):
        return self.__attribute2

    @attribute1.setter
    def attribute1(self, value):
        self.__attribute1 = value

    @attribute2.setter
    def attribute2(self, value):
        self.__attribute2 = value

    @attribute1.deleter
    def attribute1(self):
        print("attribute deleted")
        del self.__attribute1

    @attribute2.deleter
    def attribute2(self):
        print("attribute deleted")
        del self.__attribute2


main3 = Main3("attribute1", "attribute2")
print("\n###Encapsulation w/ property:")
print(main3.attribute1)
print(main3.attribute2)
main3.attribute1 = "changed"
main3.attribute2 = "changed"
print(main3.attribute1)
print(main3.attribute2)
del main3.attribute1
del main3.attribute2
