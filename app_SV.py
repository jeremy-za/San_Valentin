import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(page_title="San Valentín 💜", page_icon="💜", layout="wide")

# Fondo lila claro y estilos personalizados
st.markdown("""
    <style>
    .stApp {
        background-color: #f3e6f9; /* tono lila claro */
    }
    .message {
        color: #6A0DAD;
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
st.markdown("<h1 style='text-align: center; color: #6A0DAD;'>💕 Nuestra Historia 💕</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='color: black; font-size: 18px; text-align: center;'>Un pequeño recorrido por nuestros momentos más especiales 💜</p>",
    unsafe_allow_html=True
)

# Lista de imágenes y mensajes con carpeta Fotitos
imagenes = [
    ("Fotitos/Foto2.jpeg", "Que hermoso volver a coincidir contigo, y más increíble aún fue la oportunidad de conocernos y así cultivar algo tan hermoso que hasta hoy atesoro. 🌸"),
    ("Fotitos/Foto3.jpeg", "Que las aventuras vividas sean el punto de partida para todas las cosas que quiero pasar a tu lado. A donde sea, pero siempre a tu lado 🏕️"),
    ("Fotitos/Foto4.jpeg", "Amar pasar tiempo juntos ya es algo habitual en nosotros, pero sin duda, nunca dajaremos de apreciarlo. 💕"),
    ("Fotitos/Foto6.jpeg", "Acompañarnos en cada locura es sin duda la prueba de amor más hermoso que puede existir, compartir momentos especiales a tu lado no tiene comparación. 💛"),
    ("Fotitos/Foto7.jpeg", "Siempre tú, siempre nosotros 💜")
]

# Renderizado intercalado
for i, (ruta, mensaje) in enumerate(imagenes):
    col1, col2 = st.columns([1, 1])
    img = Image.open(ruta)

    if i % 2 == 0:
        # Imagen izquierda, texto derecha
        with col1:
            st.image(img, width=250)
        with col2:
            st.markdown(f"<div class='message-box'><p class='message-text'>{mensaje}</p></div>", unsafe_allow_html=True)
    else:
        # Texto izquierda, imagen derecha
        with col1:
            st.markdown(f"<div class='message-box'><p class='message-text'>{mensaje}</p></div>", unsafe_allow_html=True)
        with col2:
            st.image(img, width=250)

# Mensaje final
st.markdown("<h2 style='text-align: center; color: #B565A7;'>Gracias por ser parte de mi vida, amochito.</h2>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #B565A7;'>💖 ¡Feliz San Valentin! 💖</h2>", unsafe_allow_html=True)
