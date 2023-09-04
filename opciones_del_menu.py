import os
import datetime
import time
from rich import print
from rich.table import Table

def comprobar_precio(servicio):
    while True:
        try:
            while True:
                precio_del_servicio = float(input(f'Precio del servicio {servicio}: '))
                if precio_del_servicio > 0:
                    break
                else:
                    print('El precio tiene que ser mayor a 0\n')
        except ValueError:
            print('Ese no es un número válido. Intenta de nuevo\n')
        except Exception as ex:
            print(f'Ocurrió el error: {ex}. Intente de nuevo\n')
        else:
            break
    
    return precio_del_servicio

def comprobar_fecha():
    fecha_actual = datetime.date.today()
    print('[#9999FF](No posterior a la fecha actual)[/#9999FF]')
    while True:
        try:
            while True:
                fecha_proporcionada = input('Fecha de la nota (dd/mm/aaaa): ')
                fecha_de_nota = datetime.datetime.strptime(fecha_proporcionada,"%d/%m/%Y").date()
                if fecha_de_nota <= fecha_actual:
                        break
                else:
                    print('La fecha no puede ser posterior a la actual del sistema\n')
        except ValueError:
            print('Tipo de formato no válido. Intente de nuevo\n')
        except Exception as error:
            print(f'Ocurrió un problema: {error}\n')
        else:
            break
    
    return fecha_de_nota


class RegistrarNota:
    def __init__(self, folio):

        os.system('cls')

        self.detalles_de_nota()
        self.detalles_de_nota_a_str()
        self.retornar_datos()
        self.mostrar_nota(folio)
                

    def detalles_de_nota(self):
        print('[#7AFFFF]--Registro de la Nota--[#/7AFFFF]\n')

        self.fecha_de_nota = comprobar_fecha()

        print('\n[#9999FF](Separados por comas)[#/9999FF]')
        self.servicios = input('Servicios a realizar: ')

        self.monto_total = 0
        self.servicios_y_precio = {}

        print('\n([#9999FF]En número entero o con decimales, mayor a cero)[#/9999FF]')

        for servicio in self.servicios.split(','):
            servicio = servicio.strip()

            precio_del_servicio = comprobar_precio(servicio)

            self.servicios_y_precio[servicio] = precio_del_servicio
            self.monto_total += precio_del_servicio

        self.nombre_del_cliente = input('\nNombre del cliente: ')

    def detalles_de_nota_a_str(self):
        self.detallesNota = '[#9999FF]|[/#9999FF] '
        for servicio, precio in self.servicios_y_precio.items():
            self.detallesNota += f'{servicio}: {precio} [#9999FF]|[/#9999FF] '
        

    def retornar_datos(self):

        datos_recolectados = (self.fecha_de_nota, self.nombre_del_cliente, self.monto_total ,self.detallesNota)

        return datos_recolectados


    def mostrar_nota(self, folio):
        os.system('cls')

        nota = Table(title='[#7AFFFF]--Nueva nota registrada--[/#7AFFFF]', )
    
        nota.add_column("Detalles", justify="left", style="#9999FF")
        nota.add_column("Datos", justify="left", style="white")

        nota.add_row('Folio', f'{folio}')
        nota.add_row('Fecha', f'{self.fecha_de_nota}')
        nota.add_row('Nombre del cliente', f'{self.nombre_del_cliente}')
        nota.add_row('Monto a pagar', f'{self.monto_total}')
        nota.add_row('Detalle de nota', f'{self.detallesNota}')

        print(nota, '\n')
    
    def aceptacion_de_nota(self):
        while True:
            aceptar = input('| a - Aceptar | c - Cancelar |\n\n')
            print()
            if aceptar.upper() in ('A', 'ACEPTAR'):
                for i in range(3):
                    time.sleep(.3)
                    print('[green].[/green]', end='  ')

                print('[green]Nota aceptada[/green]')
                time.sleep(.8)

                return True
            
            elif aceptar.upper() in ('C', 'CANCELAR'):
                for i in range(3):
                    time.sleep(.3)
                    print('[red].[/red]', end='  ')

                print('[red]Nota cancelada[/red]')
                time.sleep(.8)

                return False
            else:
                print('Opción no válida. Intente de nuevo')