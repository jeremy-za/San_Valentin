import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(page_title="San Valentín 💜", page_icon="💜", layout="wide")
##6A0DAD
# Fondo lila claro y estilos personalizados
st.markdown("""
    <style>
    .stApp {
        background-color: #f3e6f9; /* tono lila claro */
    }
    .message {
        color: #ffffff; 
        font-size: 18px;
        text-align: center;
        margin-top: 10px;
    }
    .content {
        background-color: #ffffff;
        padding: 10px;
        border-radius: 10px;
        border: 2px solid #B565A7;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Encabezado principal
st.markdown("<h1 style='text-align: center; color: #6A0DAD;'>Nuestra Historia 💕</h1>", unsafe_allow_html=True)
st.write("Un recorrido por nuestros momentos más especiales 💜")

# Lista de imágenes y mensajes con carpeta Fotitos
imagenes = [
    ("Fotitos/Foto1.jpeg", "El inicio de nuestra aventura ✨"),
    ("Fotitos/Foto2.jpeg", "Descubriendo juntos nuevos caminos 🌸"),
    ("Fotitos/Foto3.jpeg", "Risas que iluminan mis días 💫"),
    ("Fotitos/Foto4.jpeg", "Pequeños detalles que significan tanto 💕"),
    ("Fotitos/Foto5.jpeg", "Momentos que guardo en mi corazón 🎁"),
    ("Fotitos/Foto6.jpeg", "Sueños que construimos juntos 🌙"),
    ("Fotitos/Foto7.jpeg", "Siempre tú, siempre nosotros 💜")
]

# Renderizado intercalado
for i, (ruta, mensaje) in enumerate(imagenes):
    col1, col2 = st.columns([1, 1])
    img = Image.open(ruta)

    if i % 2 == 0:
        # Imagen izquierda, texto derecha
        with col1:
            st.image(img, width=250)  # imagen más pequeña
        with col2:
            st.markdown(f"<div class='content'><p class='message'>{mensaje}</p></div>", unsafe_allow_html=True)
    else:
        # Texto izquierda, imagen derecha
        with col1:
            st.markdown(f"<div class='content'><p class='message'>{mensaje}</p></div>", unsafe_allow_html=True)
        with col2:
            st.image(img, width=250)

# Mensaje final
st.markdown("<h2 style='text-align: center; color: #B565A7;'>Gracias por ser parte de mi vida 💖</h2>", unsafe_allow_html=True)
