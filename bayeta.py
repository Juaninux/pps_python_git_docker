from prueba_mongo import consultar, add as mongo_add

def frotar(n_frases: int = 1) -> list:
    return consultar(n_frases)

def insertar(frases: list) -> int:
    return mongo_add(frases)
