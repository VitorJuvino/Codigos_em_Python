
class Conta:
    pass

def	__init__(self,	numero,	titular,	saldo,	limite):
	self.numero	=	numero
	self.titular	=	titular
	self.saldo	=	saldo
	self.limite	=	limite


def	deposita(self,	valor):
	
    self.saldo	+=	valor

def	saca(self,	valor):

	self.saldo	-=	valor
				

def	extrato(self):

    print("numero:	{}	\nsaldo:	{}".format(self.numero,	self.saldo))
    
