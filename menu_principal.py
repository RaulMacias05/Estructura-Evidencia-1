import os
from rich import print
import time
import opciones_del_menu as odm

class Menu_principal:
    def __init__(self) -> None:
        self.notas_registradas = {}
        self.notas_canceladas = {}
        self.folios = {}

        while True:
            self.mostrar_menu()

            match self.eleccion_del_menu:
                case 1:
                    self.registrar_una_nota()
                case 2:
                    self.consultas_y_reportes()
                case 3:
                    self.cancelar_una_nota()
                case 4:
                    self.recuperar_una_nota()
                case 5:
                    if self.salir_del_sistema():
                        break

    def mostrar_menu(self):

        os.system('cls')

        print(f'''
[#9999FF]REGISTRO Y MANIPULACIÓN DE NOTAS[/#9999FF]

[#7AFFFF]--Menú Principal--[/#7AFFFF]

1 - Registrar una nota
2 - Consultas y reportes
3 - Cancelar una nota
4 - Recuperar una nota
5 - Salir del sistema
              
''')

        while True:
            try:
                self.eleccion_del_menu = int(input('Elija una opción (indicando su respectivo número): '))
            except ValueError:
                print('Opción no válida. Intente de nuevo')
            else:
                if self.eleccion_del_menu > 0 and self.eleccion_del_menu <= 5:
                    break
                else:
                    print('Opción no válida. Intente de nuevo')

    def registrar_una_nota(self):
        folio = max(self.folios, default=1000) + 1
        self.folios[folio] = ''

        registro_de_nota = odm.RegistrarNota(folio)
        datos_registrados = registro_de_nota.retornar_datos()
        nota_aceptada = registro_de_nota.aceptacion_de_nota()
         
        if nota_aceptada == True:
            self.notas_registradas[folio] = datos_registrados
        if nota_aceptada == False:
            self.notas_canceladas[folio] = datos_registrados

    def consultas_y_reportes(self):
        odm.ConsultasYReportes(self.notas_registradas)

    def cancelar_una_nota(self):
        odm.CancelarNota(self.notas_registradas, self.notas_canceladas)

    def recuperar_una_nota(self):
        odm.RecuperarNota(self.notas_canceladas, self.notas_registradas)

    def salir_del_sistema(self):
        while True:
            salir = input("¿Desea salir definitivamente del programa? Al salir las notas se resetearan por completo\n| a - Aceptar | c - Cancelar |\n")

            if salir.upper() in ('A', 'ACEPTAR'):
                print("\nGracias por su visita, vuelva pronto")
                return True
            
            elif salir.upper() in ('C', 'CANCELAR'):
                print("\nVolviendo al menú principal")
                for i in range(3):
                    print('.', end=' ')
                    time.sleep(.3)
                time.sleep(.3)
                return False
                
            else:
                print('Opción no válida. Intente de nuevo\n')

Menu_principal()