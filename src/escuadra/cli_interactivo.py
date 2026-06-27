"""
Modo interactivo (REPL) para Escuadra CLI
"""

from escuadra.modulos.sistemas.herramienta_calculadora_subred import herramienta_calculadora_subred
from escuadra.modulos.civil.herramienta_diseno_vial import herramienta_diseno_vial


def listar_herramientas():
    return [
        "Calculadora de Subred (IP/CIDR)",
        "Diseño Vial (Pendiente + Peralte)"
    ]


def ejecutar_interactivo():
    print("\n=== ESCUADRA MODO INTERACTIVO ===\n")

    herramientas = listar_herramientas()

    for i, h in enumerate(herramientas, start=1):
        print(f"{i}. {h}")

    opcion = int(input("\nSelecciona una herramienta: "))

    if opcion == 1:
        print("\n--- Calculadora de Subred ---")
        ip = input("IP: ")
        cidr = input("CIDR: ")

        resultado = herramienta_calculadora_subred(ip, cidr)
        print("\nRESULTADO:\n")
        print(resultado)

    elif opcion == 2:
        print("\n--- Diseño Vial ---")
        ei = float(input("Elevación inicial: "))
        ef = float(input("Elevación final: "))
        dh = float(input("Distancia horizontal: "))
        v = float(input("Velocidad de diseño (km/h): "))
        r = float(input("Radio de curva: "))

        resultado = herramienta_diseno_vial(ei, ef, dh, v, r)
        print("\nRESULTADO:\n")
        print(resultado)

    else:
        print("Opción inválida")