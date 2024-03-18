class ControleRemoto:
    
    def __init__(self, televisao:str, comodo:str):
        self.televisao = televisao
        self.comodo = comodo
    

    def avancar_canal(self):
        print('Canal avançado!')

    def voltar_canal(self):
        print(f'Alterado para o canal')
              
    def escolher_canal(self, canal):
        print(f'Alterado para o canal {canal}')
    


controle_sala = ControleRemoto(
    televisao='Samsung',
    comodo='Sala',
)

print(controle_sala.comodo)
print(controle_sala.televisao)
print(controle_sala.avancar_canal())
print(controle_sala.escolher_canal('Globo'))