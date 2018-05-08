
enemigo_elegido = input("Contra cuual quieres luchar? (Sangri / Dark / Crac): ")


vida_taner = 100
vida_enemigo = 0
ataque_enemigo = 0


if enemigo_elegido == "Sangri:":
    vida_enemigo = 90
    nombre_enemigo == "Sangri"
    ataque_enemigo = 8
elif enemigo_elegido == "Dark:":
    vida_enemigo = 80
    nombre_enemigo = "Dark"
    ataque_enemigo = 9
elif enemigo_elegido == "Crac:":
    vida_enemigo = 70
    nombre_enemigo = "Crac"
    ataque_enemigo = 10
//asdasdsassdad
#fases



while vida_taner > 0 and vida_enemigo > 0:
    ataque_elegido = input("Que ataque quieres usar (Punetazo / Patada)")

    if ataque_elegido == "Punetazo":
        vida_enemigo -= 12
    if ataque_elegido == "Patada":
        vida_enemigo -= 10



    if vida_enemigo <= 0:
    print("Has ganado")



    if vida_taner <= 0:
    print ("Has perdido")




print("El combate ha terminado")
