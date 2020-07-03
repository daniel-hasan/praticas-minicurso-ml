import pandas as pd


def entropia(df_dados:pd.DataFrame, nom_col_classe:str) -> float:
    """
        Calcula a entropia de acordo com df_dados (DataFrame) e a classe. Use a função math.log com
        o log na base 2. Não esqueça de importar o módulo math.

        df_dados: Dados a serem considerados para o calculo da entropia
        nom_col_classe: nome da coluna (em df_dados) que representa a classe
    """
    #substitua os None/0 quando necessario para completar o código
    #ser_count_col armazena, para cada valor da classe, a sua quantidade
    ser_count_col = df_dados[nom_col_classe].value_counts()
    num_total = len(df_dados)
    entropia = 0

    #Navege em ser_count_col para fazer o calculo da entropia
    for val_atr,count_atr in ser_count_col.iteritems():
        #altere os valores de val_prob e entropia para o calculo correto da mesma
        #val_prob deverá ser a proporção de instancias de uma determinada classe
        #caso tenha duvida sobre o iteritems e value_counts, consulte o passo a passo do pandas
        val_prob = None
        entropia += None
    return entropia


def ganho_informacao_condicional(df_dados: pd.DataFrame, val_entropia_y:float, nom_col_classe:str, nom_atributo:str, val_atributo:float) ->float:
    """
    Calcula o GI(Y|nom_atributo=val_atributo), ou seja,
    calcula o ganho de informação do atributo 'nom_atributo' quando ele assume o valor 'val_atributo'.
    O valor de Entropia(Y) já foi calculado e está armazenado em val_entropia_y.
    Dica: A entropia condicional pode ser calculada filtrando o DataFrame df_dados.

    df_dados: Dataframe com os dados a serem analisados.
    val_entropia_y: Entropia(Y) (ver slides)
    nom_col_classe: nome da coluna que representa a classe
    nom_atributo: atributo a ser calculado o ganho de informação
    val_atributo: valor do atributo a ser considerado para este calculo
    """
    #substitua os "None"/0 quando necessario para completar o código
    #.em df_dados_filtrado, filtre o df_dados da forma correta - pensando quais
    #elementos considerar na entropia condicional Entropia(Y|nom_atributo=val_atributo).
    df_dados_filtrado = None

    #use df_dados_filtrado para obter o valor de Entropia(Y|nom_atributo=val_atributo)
    val_ent_condicional = 0
    #use val_ent_condicional para calcular o GI(Y|nom_atributo=val_atributo)
    val_gi = 0

    #para testes:
    #print("GI({classe}| {atr}={val}) = {val_gi}".format(classe=nom_col_classe,atr=nom_atributo,val=val_atributo,val_gi=val_gi))

    return val_gi


def ganho_informacao(df_dados:pd.DataFrame, nom_col_classe:str, nom_atributo:str) -> float:
    """
        Calcula GI(Y| nom_atributo), ou seja, o ganho de informação do atributo nom_atributo.

        df_dados: DataFrame com os dados a serem analisados.
        nom_col_classe: nome da coluna que representa a classe
        nom_atributo: atributo a ser calculado o ganho de informação
        val_atributo: valor do atributo a ser considerado para este calculo
    """
    #Muito similar ao codigo da entropia, mas aqui você deverá navegar sobre
    #os possiveis valores do atributo nom_atributo para calcular o infoGain
    #(usando a função ganho_informacao_condicional)
    #substitua os "None"/0 quando necessario para completar o código

    #atenção nessa linha abaixo, qual é o valor que temos que colocar em None?
    #o que precisamos contabilizar dessa vez?
    ser_count_col = df_dados[None].value_counts()

    val_entropia_y = None

    num_total = len(df_dados)
    val_info_gain = 0
    for val_atr,count_atr in None:
        val_prob = None
        val_info_gain += None

        #print("GI("+nom_col_classe+"| "+nom_atributo+"="+val_atr+") = "+str(val_gi_val))

    return val_info_gain
