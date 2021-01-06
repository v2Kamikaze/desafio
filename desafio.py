motoboys = {
    1: {
        "taxa": 2.0,
        "exclusividade": None,
        "pedidos_entregues": {
            "lojas": [],
            "numero_de_pedidos": 0,
            "valor_recebido": 0.0,
        },
    },
    2: {
        "taxa": 2.0,
        "exclusividade": None,
        "pedidos_entregues": {
            "lojas": [],
            "numero_de_pedidos": 0,
            "valor_recebido": 0.0,
        },
    },
    3: {
        "taxa": 2.0,
        "exclusividade": None,
        "pedidos_entregues": {
            "lojas": [],
            "numero_de_pedidos": 0,
            "valor_recebido": 0.0,
        },
    },
    4: {
        "taxa": 2.0,
        "exclusividade": 1,
        "pedidos_entregues": {
            "lojas": [],
            "numero_de_pedidos": 0,
            "valor_recebido": 0.0,
        },
    },
    5: {
        "taxa": 3.0,
        "exclusividade": None,
        "pedidos_entregues": {
            "lojas": [],
            "numero_de_pedidos": 0,
            "valor_recebido": 0.0,
        },
    }
}

lojas = {
    1: {"pedidos": {1: 50, 2: 50, 3: 50}, "porcentagem": 0.05},
    2: {"pedidos": {1: 50, 2: 50, 3: 50, 4: 50}, "porcentagem": 0.05},
    3: {"pedidos": {1: 50, 2: 50, 3: 100}, "porcentagem": 0.15}
}

def pagamento_por_pedido(motoboy, val_pedido, porc):
    """
        A função retorna o valor que o motoboy irá receber pelo pedido,
        baseado na taxa fixa cobrada pelo motoboy, o valor do pedido e a porcentagem
        paga pelo restaurante por cada pedido.

        :param motoboy: int
        :param val_pedido: float
        :param porc: float

        :retorna float 

    """  
    return motoboys[motoboy]["taxa"] + val_pedido * porc


def retirar_pedido(pedidos):
    """
        A função irá retirar o último pedido inserido no dicionário de pedidos e retornar o valor desse pedido.

        :param pedidos: dict
        :retorna float

    """
    return pedidos.popitem()[1]
    

def contabilizar_entrega(pedido_retirado, motoboy_atual, loja_atual):
    """
        A função irá inserir as informações da última entrega do motoboy no dicionário de pedidos entregues.

        :param pedido_retirado: float
        :param motoboy_atual: int
        :param loja_atual: int

    """
    motoboy = motoboys[motoboy_atual]
    porcentagem = lojas[loja_atual]["porcentagem"]
    pagamento = pagamento_por_pedido(motoboy_atual, pedido_retirado, porcentagem)
    # Adicionando as informações do pedido nos pedidos entregues do motoboy.
    if loja_atual not in motoboy["pedidos_entregues"]["lojas"]:
        motoboy["pedidos_entregues"]["lojas"].append(loja_atual)
    motoboy["pedidos_entregues"]["numero_de_pedidos"] += 1
    motoboy["pedidos_entregues"]["valor_recebido"] += pagamento


def rodizio_de_pedidos():
    """
        A função rodizio_de_pedidos irá criar uma fila com os motoboys, como a fila de um caixa,
        inicialmente cada motoboy irá para uma loja das 3 e pegará um produto, excluindo o motoboy que tiver exclusividade
        em uma loja específica. Cada vez que um motoboy retirar um pedido, ele volta pro fim da fila, simulando que ele foi fazer
        a entrega.
        O rodízio será feito de modo que cada motoboy irá pegar apenas um pedido por vez enquanto houverem pedidos.
    """
    num_pedidos = len([pedido for loja in lojas for pedido in lojas[loja]["pedidos"]])
    loja_atual = 1
    motoboy_atual = 1
    while num_pedidos > 0:
        pedidos = lojas[loja_atual]["pedidos"]
        if len(pedidos) > 0: 
            if motoboys[motoboy_atual]["exclusividade"] == None:
                pedido_retirado = retirar_pedido(pedidos)
                contabilizar_entrega(pedido_retirado, motoboy_atual, loja_atual)
                num_pedidos -= 1
                motoboy_atual += 1
                loja_atual += 1
                if motoboy_atual > 5:
                    motoboy_atual = 1
                if loja_atual > 3:
                    loja_atual = 1   
            else:
                loja_exclusiva = motoboys[motoboy_atual]["exclusividade"]
                pedidos_exclusivos = lojas[loja_exclusiva]["pedidos"]
                if len(pedidos_exclusivos) > 0:
                    pedido_retirado = retirar_pedido(pedidos_exclusivos)
                    contabilizar_entrega(pedido_retirado, motoboy_atual, loja_exclusiva)
                    num_pedidos -= 1
                    motoboy_atual += 1
                    loja_atual += 1
                    if loja_atual > 3:
                            loja_atual = 1 
                    if motoboy_atual > 5:
                        motoboy_atual = 1 
                else: 
                    motoboy_atual += 1
                    loja_atual += 1
                    if loja_atual > 3:
                            loja_atual = 1 
                    if motoboy_atual > 5:
                        motoboy_atual = 1 
        else: 
            loja_atual += 1
            if loja_atual > 3:
                loja_atual = 1 
    
def info_motoboy(moto):
    """
        Rececebe o número de um motoboy e imprime no console as informações de um motoboy específico.

        :param moto: int
    """
    motoboy = motoboys[moto]
    lojas = ','.join([str(m) for m in motoboy["pedidos_entregues"]["lojas"]])
    num_pedidos =  motoboy["pedidos_entregues"]["numero_de_pedidos"]
    valor_recebido =  motoboy["pedidos_entregues"]["valor_recebido"]
    print(f"O motoboy {moto} recebeu os pedidos das lojas {lojas} em um total de {num_pedidos} pedidos e recebeu um valor total de {valor_recebido:.2f} R$.")

def mostrar_entregas(num_motoboy = None):
    """
        Imprime no console as informações de todos os motoboys ou de um específico
        caso o parâmetro num_motoboy seja passado.

        :param num_motoboy: int
    """
    if num_motoboy != None:
        info_motoboy(num_motoboy)
    else:
        for moto in motoboys:
            info_motoboy(moto)
        



motoboy_escolhido = input("Motoboy a ser escolhido [1,2,3,4,5] ou só Enter para passar.\n")

rodizio_de_pedidos()
if motoboy_escolhido == '':
    mostrar_entregas()
else: 
    mostrar_entregas(int(motoboy_escolhido))
