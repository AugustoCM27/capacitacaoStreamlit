import streamlit as st

tab_text, tab_media, tab_buttons, tab_charts = st.tabs(['Elementos textuais',
                                                        'Mídia',
                                                        'Botões interativos',
                                                        'Gráficos'])
with tab_text:
  # Display Text
  st.title("st.title() - Isso é um título")
  st.header("st.header() - Isso é um cabeçalho")
  st.subheader("st.subheader() - Isso é um sub-cabeçalho")
  st.text("st.text() - Aqui você pode escrever o que quiser, é um texto")
  st.write("st.write() - Outra forma de escrever, mas com algumas opções adicionais...")
  
  expander = st.expander("Qual a diferença entre st.text e st.write?")
  expander.write("st.text: principalmente usado para exibir texto simples, em fonte monoespaçada e não permite a inserção de elementos interativos")  
  expander.write("st.write: mais flexível e versátil, permite exibir outros conteúdos como imagens, tabelas, gráficos, etc.")
  
  st.latex("st.latex() - sin^2(x) + cos^2(x) = 1")
  st.code("st.code() - print('Hello World')")
  
  st.text("Algumas opções adicionais:")
  expander = st.expander("Você pode criar uma caixa de texto que se expande!")
  expander.write("Basta criar uma variável para sua caixa, como var=st.expander()")
  expander.write("Depois, é só utilizar: var.write() para adicionar o que você quiser!")
  
  expander = st.expander("Como adicionar um link clicável?")
  expander.write("[Google](https://www.google.com)")
  expander.write("Adicionar o que você quer que seja clicável entre [] e o link em seguida em ()")
  expander.write("Exemplo: '['texto']''(link)'")

with tab_media:
  # Display media
  st.title("Algumas formas de adicionar conteúdos de mídia ao seu site")
  expander = st.expander("Imagens - st.image()")
  expander.write("st.image(arquivo/caminho da imagem)")
  expander.image("ligads2023.jpg")

  expander = st.expander("Vídeos - st.video()")
  expander.write("st.video('arquivo/caminho / URL')")
  expander.video("https://www.youtube.com/watch?v=uQGxv-5lwTQ&list=PL-xocjZqCGjlJLqt7P7qqY-yxncdvKsLr")
  
with tab_buttons:
  # Widgets
  st.title("As principais funções de interatividade estão expostas aqui!")
  
  expander = st.expander("st.button()")
  expander.write("Basta fornecer o texto que o botão vai conter!")
  expander.button("Isso é um botão, clique aqui!")

  expander = st.expander("st.checkbox()")
  expander.write("É só colocar o texto que se refere à caixa de seleção!")
  expander.checkbox("Isso é uma caixa de seleção!")

  expander = st.expander("st.radio()")
  expander.write("Você precisa fornecer o texto que introduz as opções e as opções de seleção em uma lista!")
  expander.write("st.radio('Texto de introdução', [lista de opções])")
  expander.radio("Esses são botões de seleção única!", ['Opção 1', 'Opção 2', 'Opção 3'])

  expander = st.expander("st.selectbox()")
  expander.write("Forneça o texto que acompanha a caixa e as opções no formato de lista!")
  expander.write("st.selectbox('Texto de introdução', [lista de opções])")
  expander.selectbox("Isso é uma caixa de seleção, você precisa fornecer as opções para que o usuário selecione uma!", ['Opção 1', 'Opção 2'])

  expander = st.expander("st.multiselect()")
  expander.write("Essa função permite que você selecione mais de uma opção!")
  expander.write("st.multiselect('Texto de introdução', [lista de opções])")
  expander.multiselect("Você pode seleciona mais de uma opção!", ["Op1", "Op2", "Op3"])

  expander = st.expander("st.slider()")
  expander.write("O slider permite criar um controle deslizante, que vai de um valor mínimo até um máximo!")
  expander.write("st.slider('Texto', 'min', 'max')")
  expander.slider("Deslize até o ano que você deseja:", 2020, 2023)

  expander = st.expander("st.text_input()")
  expander.write("Função para que o usuário escreva algo (string)")
  expander.text_input("Digite o que você quiser!")

  expander = st.expander("st.number_input()")
  expander.write("Função para que o usuário forneça um número")
  expander.number_input("Escreva um número!")

  expander = st.expander("st.color_picker()")
  expander.write("Função para que o usuário escolha uma cor")
  expander.color_picker("Escolha uma cor")
          
  expander = st.expander("st.file_uploader()")
  expander.write("O usuário pode fazer o upload de um arquivo, que seu código irá tratar!")
  expander.file_uploader("Faça o upload de um arquivo")
  
  st.write("Para adicionar respostas e variações de acordo com o que o usuário seleciona, basta atribuir as funções expostas em variáveis e verificar a condição dos widgets com um 'if'.")
  st.code("Exemplo: resposta = st.radio('Opções', [Op1, Op2, Op3]")
  st.code("if resposta == Op1: ....")

with tab_charts:
  st.title("Como expor suas análises de dados?")
  st.subheader("O streamlit possui suporte à diversas bibliotecas comuns para análises de dados em Python, como matplotlib, seaborn, plotly, bokeh, pydeck e muitas outras!")

  data = {'Nome': ['Alice', 'Bob', 'Carol', 'David', 'Eve'], 'Idade': [25, 30, 22, 28, 35], 'Pontuação': [85, 70, 90, 65, 78]}
  df = pd.DataFrame(data)

  st.write("Para expor uma base de dados você pode utilizar o comando 'st.write(df)' normalmente. O resultado será esse:")
  st.write(df)

  expander = st.expander("st.line_chart()")
  expander.line_chart(data=df, x='Nome', y='Idade')
  

              



