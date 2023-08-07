import streamlit as st

# Display Text
st.title("st.title() - Isso é um título")
st.header("st.header() - Isso é um cabeçalho")
st.subheader("st.subheader() - Isso é um sub-cabeçalho")
st.text("st.text() - Aqui você pode escrever o que quiser, é um texto")
st.write("st.write() - Outra forma de escrever, mas com algumas opções adicionais...")

expander = st.expander("Qual a diferença entre st.text e st.write?")
expander.write("st.text: Este método é principalmente usado para exibir texto simples. 
  Ele exibe o texto em uma fonte monoespaçada (como Courier) e não permite formatação avançada 
  ou inserção de elementos interativos.")

st.latex("st.latex() - sin^2(x) + cos^2(x) = 1")
st.code("st.code() - print('Hello World')")

st.text("Algumas opções adicionais:")
expander = st.expander("Você pode criar uma caixa de texto que se expande!")
expander.write("Basta criar uma variável para sua caixa através de st.expander()")
expander.write("Depois, é só utilizar: expander.write() para adicionar o que você quiser!")

