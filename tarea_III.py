class Conductor:
    def __init__(self, id_conductor, nombre):
        self.id_conductor = id_conductor
        self.nombre = nombre
        self.horarios = []  # Lista de horarios asignados al conductor

    def asignar_horario(self, horario):
        if horario in self.horarios:
            return False
        self.horarios.append(horario)
        return True

class Bus:
    def __init__(self, id_bus, placa):
        self.id_bus = id_bus
        self.placa = placa
        self.rutas = []  # Lista de rutas asignadas al bus
        self.horarios = []  # Lista de horarios del bus
        self.conductor_asignado = None

    def agregar_ruta(self, ruta):
        self.rutas.append(ruta)

    def registrar_horario(self, horario):
        self.horarios.append(horario)

    def asignar_conductor(self, conductor, horario):
        if horario not in self.horarios:
            return "El horario no está registrado para este bus."
        if conductor.asignar_horario(horario):
            self.conductor_asignado = conductor
            return "Conductor asignado correctamente."
        return "El conductor ya tiene un horario asignado en ese rango."

def menu():
    buses = []
    conductores = []
    while True:
        print("\nGestión de Buses")
        print("1. Agregar Bus")
        print("2. Agregar Ruta a Bus")
        print("3. Registrar Horario a Bus")
        print("4. Agregar Conductor")
        print("5. Agregar Horario a Conductor")
        print("6. Asignar Bus a Conductor")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            id_bus = input("Ingrese ID del Bus: ")
            placa = input("Ingrese placa del Bus: ")
            buses.append(Bus(id_bus, placa))
            print("Bus agregado exitosamente.")

        elif opcion == "2":
            id_bus = input("Ingrese ID del Bus: ")
            ruta = input("Ingrese ruta: ")
            bus = next((b for b in buses if b.id_bus == id_bus), None)
            if bus:
                bus.agregar_ruta(ruta)
                print("Ruta agregada exitosamente.")
            else:
                print("Bus no encontrado.")

        elif opcion == "3":
            id_bus = input("Ingrese ID del Bus: ")
            horario = input("Ingrese horario (HH:MM-HH:MM): ")
            bus = next((b for b in buses if b.id_bus == id_bus), None)
            if bus:
                bus.registrar_horario(horario)
                print("Horario agregado exitosamente.")
            else:
                print("Bus no encontrado.")

        elif opcion == "4":
            id_conductor = input("Ingrese ID del Conductor: ")
            nombre = input("Ingrese nombre del Conductor: ")
            conductores.append(Conductor(id_conductor, nombre))
            print("Conductor agregado exitosamente.")

        elif opcion == "5":
            id_conductor = input("Ingrese ID del Conductor: ")
            horario = input("Ingrese horario (HH:MM-HH:MM): ")
            conductor = next((c for c in conductores if c.id_conductor == id_conductor), None)
            if conductor:
                if conductor.asignar_horario(horario):
                    print("Horario asignado correctamente al conductor.")
                else:
                    print("El horario ya está asignado al conductor.")
            else:
                print("Conductor no encontrado.")

        elif opcion == "6":
            id_bus = input("Ingrese ID del Bus: ")
            id_conductor = input("Ingrese ID del Conductor: ")
            horario = input("Ingrese horario a asignar (HH:MM-HH:MM): ")
            bus = next((b for b in buses if b.id_bus == id_bus), None)
            conductor = next((c for c in conductores if c.id_conductor == id_conductor), None)
            if bus and conductor:
                print(bus.asignar_conductor(conductor, horario))
            else:
                print("Bus o Conductor no encontrado.")

        elif opcion == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()