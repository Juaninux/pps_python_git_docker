from pymongo import MongoClient
import os

DB_NAME = "bayeta"
COL_NAME = "frases_auspiciosas"

def instanciar():
    mongo_uri = os.environ.get("MONGO_URI", "mongodb://localhost:27017/")
    cliente = MongoClient(mongo_uri)
    bd = cliente[DB_NAME]
    coleccion = bd[COL_NAME]
    return cliente, coleccion


def inicializar(datos):
    cliente, frases_auspiciosas = instanciar()
    try:
        if frases_auspiciosas.count_documents({}) == 0:
            frases_auspiciosas.insert_many(datos)
    finally:
        cliente.close()


def consultar(n_frases: int):
    cliente, frases_auspiciosas = instanciar()
    try:
        frases_aleatorias = list(
            frases_auspiciosas.aggregate(
                [{"$sample": {"size": n_frases}}]
            )
        )
        return [f["frase"] for f in frases_aleatorias]
    finally:
        cliente.close()


# -------- BLOQUE DE PRUEBA --------
if __name__ == "__main__":

    datos = [
        {"frase": "El éxito es como un fantasma, muchos hablan de él, pero pocos lo han visto de verdad"},
        {"frase": "La aventura de hoy es la historia de terror del mañana"},
        {"frase": "La felicidad es como un rayo de sol, disfrútala antes de que el cambio climático la arruine"},
        {"frase": "Enfrenta tus miedos, o pídeles alquiler por vivir en tu cabeza"},
        {"frase": "Recuerda, cada pequeño cambio cuenta. Especialmente los errores en tu declaración de la renta"},
        {"frase": "Aprovecha las oportunidades, son como los autobuses, los que no llegan tarde simplemente no pasan"},
        {"frase": "Ser agradecido está bien, pero no paga las facturas"},
        {"frase": "La creatividad es como jugar a la ruleta rusa, nunca sabes cuándo te tocará una 'buena' idea"},
        {"frase": "Ríe y el mundo reirá contigo. Llora, y te darán una cuenta de Twitter"},
        {"frase": "Sigue tu corazón, pero recuerda llevar tu cerebro contigo"}
    ]

    inicializar(datos)

    frases = consultar(3)

    for frase in frases:
        print(frase)
