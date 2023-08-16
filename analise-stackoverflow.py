import joblib
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import seaborn as sns
import matplotlib.pyplot as plt


# Carregando os dados e convertendo a coluna YearsCodePro para float
dataset = pd.read_csv("dataset_processado.csv")
dataset["YearsCodePro"] = dataset["YearsCodePro"].astype("float", errors="ignore")


# Função geral para nossas análises
def Analisar(variavel_um, variavel_dois, data=dataset):
    ''' 
        Função para analisar duas variáveis de um dataset
        
        Por exemplo: Analisar("Country", "Salary")
        Esse comando irá analisar a média salarial por país e
        retornará-los em ordem decrescente.
    '''

    # Agrupando os dados e calculando a mediana
    analise = data.groupby(variavel_um)[variavel_dois].median()

    # Ordenando os valores de forma decrescente (01) e resetando o índice (02)
    analise = analise.sort_values(ascending=False) # (01)
    analise = analise.reset_index() # (02)

    return analise


# Configurando a página
st.set_page_config(layout="wide", page_title="Exemplo STREAMLIT - LIGA DS")


# Inserindo imagem centralizada
logo_url = "https://i.imgur.com/FRUhSqn.png"


# Vamos criar 7 colunas e colocar a imagem no centro da coluna do meio
_,_,_,_,logo,_,_,_,_ = st.columns(9)
logo.image(logo_url)


# Vamos criar 3 colunas e colocar a imagem no centro da coluna do meio
_,menu,_ = st.columns(3)


# Definindo um título
menu.title("Análise de dados do Stack Overflow 2023 👨‍💻")
menu.markdown("---")

# INTRODUÇÃO:
menu.markdown("## Introdução:")

# Definindo um subtítulo
menu.markdown("""
            Olá! 👋👋👋👋

            Este é um exemplo de análise de dados utilizando Streamlit. 
            Streamlit é uma biblioteca Python de código aberto que permite
            criar complexas visualizações de dados de maneira simples e
            rápida.
            
            Neste exemplo, vamos usar Streamlit para criar um simples
            aplicativo que nos permite visualizar e interagir com um simples
            conjunto de dados de salários de desenvolvedores. O conjunto de
            dados contém informações sobre a área de atuação, localização, 
            nível de formação e tempo de experiência na área.
            
            Vamos usar Streamlit para criar gráficos que nos permite visualizar
            os dados de maneira interativa. Também vamos usar Streamlit para criar
            um simples aplicativo que permite que você preveja seu próprio salário. """)


# ANALISES:
menu.markdown("---")
menu.markdown("## Análises:")


# CASO 01. Análise de salário por país
st.markdown("#### 01. Analisando o salário por países:")
analise_salario_pais = Analisar("Country", "Salary")

colA, colB = st.columns(2)

colA.text("  Os 10 países com maiores salários:  ")
colA.dataframe(analise_salario_pais.head(10), use_container_width = True)

colB.text("  Gráfico de barra com os salários em ordem crescente  ")
colB.bar_chart(data = analise_salario_pais, x= "Country", y="Salary", 
                use_container_width = True, height=500)

analise_coordenada = dataset.groupby(["LATITUDE", "LONGITUDE"])["Salary"].median()


valores = analise_coordenada.values
# processando coordenadas
coordenadas = analise_coordenada.index
latitude    = coordenadas.get_level_values(0)
longitude   = coordenadas.get_level_values(1)

st.map(pd.DataFrame({"lat":latitude, "lon":longitude, "salario":valores}), size="salario")



# CASO 02. Análise de salário por área de atuação
st.markdown("#### 02. Analisando o salário por área de atuação:")
analise_salario_area = Analisar("DevType", "Salary")

colA, colB = st.columns(2)

colA.text("  As 10 áreas com maiores salários:  ")
colA.dataframe(analise_salario_area.head(10), use_container_width = True)

colB.text("  Gráfico de barra com os salários")
colB.bar_chart(data = analise_salario_area, x= "DevType", y="Salary",
                use_container_width = True, height=500)


st.markdown("-----")


# CASO 03. Análise de salário por área de atuação
st.markdown("#### 03. Analisando o salário por anos de atuação:")

st.text("  Gráfico de linha com os anos de experiência em função do salário:  ")

analise_salario_anos = Analisar("YearsCodePro", "Salary")

st.line_chart(data = analise_salario_anos, x= "YearsCodePro", y="Salary",
                use_container_width = True, height=500)
st.markdown("-----")


# PREVISÃO DE SALÁRIOS
st.markdown("#### Prevendo salários 💸")

st.text("  Insira seus dados para fazer uma previsão de salário:  ")

_, center, _ = st.columns(3)

# Criando os widgets para inserção de dados
center.slider("Anos de experiência", 0, 50, 25, key="anos_experiencia")
center.selectbox("Área de atuação", (dataset["DevType"].unique()), key="area_atuacao")
center.selectbox("País", (dataset["Country"].unique()), key="pais")

if center.button("Prever salário", key="prever_salario", use_container_width=True):

    # Obtendo dados inseridos pelo usuário
    anos_exp = st.session_state.anos_experiencia
    area_atuacao = st.session_state.area_atuacao
    pais = st.session_state.pais

    # Carregando Label Encoders e o modelo
    load_label_encoder_area = joblib.load("area_encoder.pkl")
    load_label_encoder_pais = joblib.load("pais_encoder.pkl")
    modelo = joblib.load("modelo.pkl")

    area_encoded = load_label_encoder_area.transform([area_atuacao])
    pais_encoded = load_label_encoder_pais.transform([pais])

    # Vetor de entrada para o modelo
    input_vector = np.array((int(pais_encoded), int(area_encoded), anos_exp))

    # Fazendo predições
    predict = modelo.predict([input_vector])
    
    salario_minimo = round((float(predict) - 47666), 2)
    salario_mensal_cvt = (salario_minimo / 12) * 4.90

    _, center_predict, _ = st.columns(3)

    center_predict.markdown("""
            ## Previsões prontas 🎉🎉
            ##### Seu salário seria aproximadamente {:.2f} reais / mês.""".format(salario_mensal_cvt))
    
    
st.write("----")
st.write("""OBS: Como simplificamos muito o dataset, as previsões não são muito precisas. Acima
                exibi o salário mínimo, que é o salário previsto pela IA subtraído pelo erro absoluto médio, que
                é de 47666 dólares.""")
    

    

