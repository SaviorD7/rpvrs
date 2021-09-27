import Pyro4

class Server(object):
    @Pyro4.expose
    def welcomeMessage(self, name):
        return ("Hi, " + str (name))

    @Pyro4.expose    
    def multiplication(self, a, b):

        return(int(a,2) & int(b,2))

    @Pyro4.expose
    def comprassion(self, a, b):
        return(a==b)


    @Pyro4.expose
    def evaluate(self, a, b):
        return((b % 2 == 0) or (a % 2 == 0))     

    @Pyro4.expose
    def stringComprassion(serf, a, b):
        return(a == b)

    




def startServer():
	   
    server = Server()
	   
    daemon = Pyro4.Daemon()
	   
    ns = Pyro4.locateNS()
	   
    uri = daemon.register(server)
	   
    ns.register("server", uri)
	   
    print("Ready. Object uri =", uri)
    daemon.requestLoop()


if __name__ == "__main__":
    startServer()