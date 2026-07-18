import streamlit as st
import string

# Configuração da página
st.set_page_config(
    page_title="Atividades de PLN",
    page_icon="🤖"
)

# Título
st.title("🤖 Atividades de Processamento de Linguagem Natural")
st.write("Aplicações básicas de PLN utilizando Python e Streamlit")


# Menu lateral
atividade = st.sidebar.selectbox(
    "Escolha uma atividade:",
    [
        "Atividade 1 - Tokenização",
        "Atividade 2 - Frequência de palavras",
        "Atividade 3 - Identificar palavras negativas",
        "Atividade 4 - Remover stopwords",
        "Atividade 5 - Análise de sentimento",
        "Atividade 6 - Identificar palavras-chave",
        "Atividade 7 - Palavras mais frequentes",
        "Atividade 8 - Classificação de setor",
        "Atividade 9 - Limpeza de texto",
        "Atividade 10 - Sentimento com tokenização"
    ]
)


# Entrada do usuário
texto = st.text_area(
    "Digite um texto para análise:",
    height=150
)


# Botão
executar = st.button("Executar análise")


# ==============================
# ATIVIDADE 1
# ==============================

if atividade == "Atividade 1 - Tokenização":

    st.subheader("🔹 Tokenização")

    st.write(
        "Separa um texto em palavras individuais."
    )

    if executar:

        palavras = texto.split()

        st.write("Palavras encontradas:")
        st.write(palavras)



# ==============================
# ATIVIDADE 2
# ==============================

elif atividade == "Atividade 2 - Frequência de palavras":

    st.subheader("🔹 Frequência das palavras")

    if executar:

        palavras = texto.lower().split()

        frequencia = {}

        for palavra in palavras:
            frequencia[palavra] = frequencia.get(palavra, 0) + 1

        st.write("Frequência:")
        st.write(frequencia)



# ==============================
# ATIVIDADE 3
# ==============================

elif atividade == "Atividade 3 - Identificar palavras negativas":

    st.subheader("🔹 Detecção de palavras negativas")

    if executar:

        texto_limpo = texto.lower()

        negativas = [
            "ruim",
            "péssimo",
            "erro"
        ]

        encontrado = False

        for palavra in negativas:

            if palavra in texto_limpo:
                encontrado = True


        if encontrado:

            st.error(
                "Mensagem negativa detectada."
            )

        else:

            st.success(
                "Nenhuma palavra negativa encontrada."
            )



# ==============================
# ATIVIDADE 4
# ==============================

elif atividade == "Atividade 4 - Remover stopwords":

    st.subheader("🔹 Remoção de stopwords")

    if executar:

        stopwords = [
            "de",
            "a",
            "o",
            "para",
            "da",
            "do",
            "e",
            "em"
        ]


        palavras = texto.lower().split()


        resultado = []


        for palavra in palavras:

            if palavra not in stopwords:
                resultado.append(palavra)


        st.write("Texto limpo:")
        st.write(resultado)



# ==============================
# ATIVIDADE 5
# ==============================

elif atividade == "Atividade 5 - Análise de sentimento":

    st.subheader("🔹 Análise de sentimento")


    if executar:

        texto_limpo = texto.lower()


        positivas = [
            "bom",
            "ótimo",
            "excelente",
            "gostei",
            "maravilhoso",
            "perfeito"
        ]


        negativas = [
            "ruim",
            "péssimo",
            "horrível",
            "odiei",
            "problema"
        ]


        if any(p in texto_limpo for p in positivas):

            st.success(
                "Sentimento: Positivo 😀"
            )


        elif any(n in texto_limpo for n in negativas):

            st.error(
                "Sentimento: Negativo 😞"
            )


        else:

            st.info(
                "Sentimento: Neutro 😐"
            )



# ==============================
# ATIVIDADE 6
# ==============================

elif atividade == "Atividade 6 - Identificar palavras-chave":

    st.subheader("🔹 Palavras-chave do chatbot")


    if executar:

        texto_limpo = texto.lower()


        if "cancelar" in texto_limpo:

            st.write(
                "Setor: Cancelamento"
            )


        elif "erro" in texto_limpo:

            st.write(
                "Setor: Suporte Técnico"
            )


        elif "pagamento" in texto_limpo:

            st.write(
                "Setor: Financeiro"
            )


        else:

            st.write(
                "Setor não identificado"
            )



# ==============================
# ATIVIDADE 7
# ==============================

elif atividade == "Atividade 7 - Palavras mais frequentes":

    st.subheader("🔹 Palavras mais frequentes")


    if executar:

        palavras = texto.lower().split()


        frequencia = {}


        for palavra in palavras:

            frequencia[palavra] = (
                frequencia.get(palavra, 0) + 1
            )


        resultado = sorted(
            frequencia.items(),
            key=lambda x: x[1],
            reverse=True
        )


        st.write(resultado)



# ==============================
# ATIVIDADE 8
# ==============================

elif atividade == "Atividade 8 - Classificação de setor":

    st.subheader("🔹 Classificação de atendimento")


    if executar:

        texto_limpo = texto.lower()


        financeiro = [
            "pagamento",
            "pix",
            "boleto",
            "fatura"
        ]


        suporte = [
            "erro",
            "senha",
            "login",
            "sistema"
        ]


        if any(p in texto_limpo for p in financeiro):

            st.success(
                "Categoria: Financeiro"
            )


        elif any(p in texto_limpo for p in suporte):

            st.warning(
                "Categoria: Suporte Técnico"
            )


        else:

            st.info(
                "Categoria não identificada"
            )



# ==============================
# ATIVIDADE 9
# ==============================

elif atividade == "Atividade 9 - Limpeza de texto":

    st.subheader("🔹 Limpeza e normalização")


    if executar:

        texto_limpo = texto.lower()


        texto_limpo = texto_limpo.translate(
            str.maketrans(
                "",
                "",
                string.punctuation
            )
        )


        st.write(
            texto_limpo
        )



# ==============================
# ATIVIDADE 10
# ==============================

elif atividade == "Atividade 10 - Sentimento com tokenização":

    st.subheader("🔹 Tokenização + sentimento")


    st.write(
        "Separa o texto em palavras e analisa o sentimento."
    )


    if executar:

        # Normalização
        texto_limpo = texto.lower()


        texto_limpo = texto_limpo.translate(
            str.maketrans(
                "",
                "",
                string.punctuation
            )
        )


        # Tokenização
        palavras = texto_limpo.split()


        positivas = [
            "bom",
            "ótimo",
            "excelente",
            "gostei",
            "maravilhoso",
            "perfeito"
        ]


        negativas = [
            "ruim",
            "péssimo",
            "horrível",
            "erro",
            "problema",
            "odiei"
        ]


        positivo = 0
        negativo = 0


        for palavra in palavras:


            if palavra in positivas:

                positivo += 1


            elif palavra in negativas:

                negativo += 1



        st.write(
            "Palavras analisadas:"
        )

        st.write(
            palavras
        )


        st.write(
            "Palavras positivas:",
            positivo
        )


        st.write(
            "Palavras negativas:",
            negativo
        )


        if positivo > negativo:

            st.success(
                "Resultado: Sentimento Positivo 😀"
            )


        elif negativo > positivo:

            st.error(
                "Resultado: Sentimento Negativo 😞"
            )


        else:

            st.info(
                "Resultado: Sentimento Neutro 😐"
            )