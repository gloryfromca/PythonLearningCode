class Parent(object):

    @staticmethod
    def staticSayHello():
        print ("Parent static")

    @classmethod
    def classSayHello(anything):  #这里是anything
        if anything == Boy:
            print ("Boy sayHello")
        elif anything == Girl:
            print ("girl sayHello")


class Boy(Parent):
     pass

class Girl(Parent):
    pass

if __name__ == '__main__':
    Boy.staticSayHello()
    Girl.staticSayHello()
    Boy.classSayHello()
    Girl.classSayHello()