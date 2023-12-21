def idade_do_usuario(data_nascimento_str):
    from datetime import datetime

    # data_nascimento = datetime.strptime(data_nascimento_str, "%d-%m-%Y").date()
    data_nascimento = data_nascimento_str
    hoje = datetime.now().date()
    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
    
    return idade
