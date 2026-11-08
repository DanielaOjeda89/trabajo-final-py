import json, os
from pathlib import Path

class StockInvalidoError(Exception):
    """
    Excepción personalizada para indicar que el stock es inválido.

    """
    pass

class PrecioInvalidoError(Exception):
    """
    Excepción personalizada para indicar que el precio es inválido.

    """
    pass

class DispositivoEcologico:
    nombre: str
    __stock: int  
    __precio: float

    def __init__(self, nombre: str, stock: int, precio: float):
        self.nombre = nombre
        self.stock = stock
        self.precio = precio 

    @property
    def stock(self): return self.__stock

    @stock.setter
    def stock(self, valor):
        try:
            valor_valido = int(valor)

            if (valor) < 0:  
                raise StockInvalidoError("El valor a asignar al stock no puede ser negativo.")
            self.__stock = valor_valido
        except TypeError:
            raise StockInvalidoError("El valor ingresado para stock no puede ser nulo.")
        except ValueError: 
            raise StockInvalidoError("El tipo de dato para stock debe ser un número entero.")

    @property
    def precio(self): return self.__precio

    @precio.setter
    def precio(self, val):
        try:
            self.__precio = float(val)
            if (val) < 0:
                raise PrecioInvalidoError("El precio no puede ser negativo.")
        except ValueError:
            raise PrecioInvalidoError("El precio debe ser un número decimal.")
        except TypeError:
            raise PrecioInvalidoError("El precio no puede ser nulo.")


    def ficha_tecnica_comercial(self, imprimir: bool = False) -> str:
        ficha = f"Nombre: {self.nombre}\nStock: {self.stock}\nPrecio: ${self.precio:.2f}"

        if imprimir:
            print(ficha)
        return ficha

    def to_dict(self) -> dict:
        return {
            "nombre": self.nombre,
            "stock": self.stock,
            "precio": self.precio
        }


class PanelSolar(DispositivoEcologico):
    potencia: float

    def __init__(self, nombre: str, stock: int, precio: float, potencia: float):
        super().__init__(nombre, stock, precio)
        self.potencia = potencia

    def ficha_tecnica_comercial(self, imprimir: bool = False) -> str: 
        ficha = super().ficha_tecnica_comercial()
        ficha += f"\nPotencia: {self.potencia} W"

        if imprimir:
            print(ficha)
        return ficha

    def to_dict(self):
        dict = super().to_dict()
        dict["potencia"] = self.potencia
        return dict 


#Persistencia y gestión del Catálogo: 

class GestorInventario: 
    @staticmethod
    def guardar_dispositivo(lista_dispositivos: list[DispositivoEcologico | PanelSolar], directorio_archivo: str = "prueba") -> bool:
        Path(directorio_archivo).mkdir(exist_ok=True)

        with open(directorio_archivo + "/catalogo_ecotech.json", "w") as archivo:
            lista_dispositivos_serializados = []
            for dispositivo in lista_dispositivos:
                lista_dispositivos_serializados.append(dispositivo.to_dict())
            json.dump(lista_dispositivos_serializados, archivo, indent=4) 



dispositivo1 = DispositivoEcologico("Fotocelula", 5, 150.0)
dispositivo2 = DispositivoEcologico("LED", 10, 200.0)

panel1 = PanelSolar("Panel Solar 100W", 3, 500.,80.0)
panel2 = PanelSolar("Panel Solar 200W", 2, 800.,150.0)
panel3 = PanelSolar("Panel Solar 300W", 1, 1200.,250.0)


try:
    panel1.stock = -100
except StockInvalidoError as e:
    print(f"Error al modificar el stock del dispositivo por un valor negativo : {e}")

lista_dispositivos: list[DispositivoEcologico | PanelSolar] = [
    dispositivo1, 
    dispositivo2, 
    panel1, 
    panel2, 
    panel3
]

for dispositivo in lista_dispositivos:
    dispositivo.ficha_tecnica_comercial(True)
    

GestorInventario.guardar_dispositivo(lista_dispositivos)

