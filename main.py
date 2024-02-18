class Dia:
    def __init__(self, anyo=1970, mes=1, dia=1):
        self.anyo = anyo
        self.mes = mes
        self.dia = dia
        self.dias_semana = 0
        
    def es_bisiesto(self):
        """
        Determina si el año es bisiesto.
        """
        es_bisiesto = (self.anyo % 4 == 0 and self.anyo % 100 != 0) or (self.anyo % 400 == 0)
        return es_bisiesto
    
    def mes_X_dia(self):
        """
        Determina la cantidad de días para un mes dado.
        """
        meses_30_dias = [4,6,9,11]
        
        if self.mes == 2:
            return 29 if self.es_bisiesto() else 28
        elif self.mes in meses_30_dias:
            return 30
        else:
            return 31

    def control_errores(self):
        """
        Realiza comprobaciones para evitar que los meses y los días estén fuera de rango.
        """
        fin_mes = self.mes_X_dia()
        # Control del limite de los meses en un año
        if self.mes not in range(1, 12 + 1):
            raise ValueError("El mes ingresado es invalido")
        
        # Control del limite de los días de cada mes
        if self.dia not in range(1, fin_mes + 1):
            raise ValueError("El dia ingresado es invalido")

    def ajustar_mes_anyo(self):
        """
        Ajusta el mes y el año para el algoritmo de Zeller si la fecha es en enero o febrero.
        """
        
        if self.mes in [1, 2]:
            self.mes += 12
            self.anyo -= 1 

    def calcular_dia_semana(self):
        self.ajustar_mes_anyo()
        """
        Calcula el día de la semana utilizando el algoritmo de Zeller modificado para años previos y posteriores a 2000.
        """
        A = self.anyo % 100
        B = self.anyo // 100
        C = 2 - B + B // 4
        D = A // 4
        E = 13 * (self.mes + 1) // 5

        if self.anyo < 2000:
            self.dia_semana = (A + C + D + E + self.dia ) % 7 
        else:
            self.dia_semana = (A + C + D + E + self.dia - 1) % 7 
        return self.dia_semana

    def mostrar_semana(self):
        """
        Muestra el día de la semana correspondiente a la fecha.
        """
        dia_semana = self.calcular_dia_semana()
        dias_semana = ["Sábado","Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

        return dias_semana[dia_semana]
    
    def __str__(self):
        """
        Representación de la fecha como una cadena de caracteres.
        """
        return f"{self.dia}/{self.mes}/{self.anyo}"

try:
    # Crear una instancia de la clase Dia
    fecha = Dia(1970, 3, 2)
    fecha.control_errores()

    # Mostrar la fecha
    print("Fecha:", fecha)

    # Mostrar el día de la semana
    print("Día de la semana:", fecha.mostrar_semana())

    print("Número de día de la semana:", fecha.dia_semana)
    
except ValueError as e:
    # Manejar el error si se produce una excepción de valor inválido
    print("Error:", e)
except Exception as e:
    # Manejar cualquier otro tipo de excepción
    print("Se produjo un error inesperado:", e)
