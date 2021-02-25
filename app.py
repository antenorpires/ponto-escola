import PySimpleGUI as psg

class TelaPy:
    def __init__(self):
        psg.theme('DarkAmber')
        layout=[[psg.Text('MATRÍCULA:'),psg.InputText(),psg.Button('ENTRAR')]]
        window=psg.Window('ÁREA DE ACESSO',layout)
        self.button,self.values=window.Read()
    def Iniciar(self):
        print(self.values)
tela=TelaPy()
tela.Iniciar()

class Aluno:	
	#lista=["Antenor Pires","antenor@gtdsi.com","(88)98818-2978"]
	#print ("\n--- Iniciando Lista ---\nNome:",lista[0],"\nE-mail:",lista[1],"\nCelular:",lista[2],"\n--- Fim da Lista ---")
	
	def setNome(self,nome):
		self.nome=nome		
	def getNome(self):
		return self.nome
		
	def setEmail(self,email):
		self.email=email
	def getEmail(self):
		return self.email
		
	def setCelular(self,celular):
		self.celular=celular		
	def getCelular(self):
		return self.celular
		
#print("\n--- Início da Instância ---")	
#a=Aluno()
#a.setNome("Antenor Pires")
#a.setEmail("antenor@gtdsi.com")
#a.setCelular("(88)98818-2978")
#print("Nome:", a.getNome(), "\nE-mail:", a.getEmail(), "\nCelular:", a.getCelular())
#print("--- Fim da Instância ---")