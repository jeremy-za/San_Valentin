import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(page_title="San Valentín 💜", page_icon="💜", layout="wide")

# Estilos personalizados con CSS
st.markdown("""
    <style>
    .timeline {
        display: flex;
        flex-direction: column;
        align-items: center;
        position: relative;
    }
    .timeline::before {
        content: '';
        position: absolute;
        width: 4px;
        background-color: #B565A7;
        top: 0;
        bottom: 0;
        left: 50%;
        margin-left: -2px;
    }
    .container {
        padding: 20px;
        position: relative;
        width: 50%;
    }
    .left {
        left: 0;
    }
    .right {
        left: 50%;
    }
    .content {
        background-color: #f9f9f9;
        padding: 15px;
        border-radius: 10px;
        border: 2px solid #B565A7;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
    }
    .content img {
        width: 100%;
        border-radius: 10px;
    }
    .message {
        text-align: center;
        color: #6A0DAD;
        font-size: 18px;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Encabezado principal
st.markdown("<h1 style='text-align: center; color: #6A0DAD;'>Nuestra Historia 💕</h1>", unsafe_allow_html=True)
st.write("Un recorrido por nuestros momentos más especiales, paso a paso 💜")

# Lista de imágenes y mensajes
imagenes = [
    ("images/img1.jpg", "El inicio de nuestra aventura ✨"),
    ("images/img2.jpg", "Descubriendo juntos nuevos caminos 🌸"),
    ("images/img3.jpg", "Risas que iluminan mis días 💫"),
    ("images/img4.jpg", "Pequeños detalles que significan tanto 💕"),
    ("images/img5.jpg", "Momentos que guardo en mi corazón 🎁"),
    ("images/img6.jpg", "Sueños que construimos juntos 🌙"),
    ("images/img7.jpg", "Siempre tú, siempre nosotros 💜")
]

# Renderizado de la línea de tiempo
st.markdown("<div class='timeline'>", unsafe_allow_html=True)

for i, (ruta, mensaje) in enumerate(imagenes):
    lado = "left" if i % 2 == 0 else "right"
    st.markdown(f"<div class='container {lado}'><div class='content'>", unsafe_allow_html=True)
    img = Image.open(ruta)
    st.image(img, use_column_width=True)
    st.markdown(f"<p class='message'>{mensaje}</p>", unsafe_allow_html=True)
    st.markdown("</div></div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Mensaje final
st.markdown("<h2 style='text-align: center; color: #B565A7;'>Gracias por ser parte de mi vida 💖</h2>", unsafe_allow_html=True)
