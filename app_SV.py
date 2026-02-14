import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(page_title="San Valentín 💜", page_icon="💜", layout="centered")

# Encabezado principal
st.markdown(
    "<h1 style='text-align: center; color: #6A0DAD;'>Nuestra Historia 💕</h1>",
    unsafe_allow_html=True
)

st.write("Un recorrido por nuestros momentos más especiales 💜")

# Lista de imágenes y mensajes
imagenes = [
    ("Foto1.jpeg", "El inicio de nuestra aventura ✨"),
    ("Foto2.jpeg", "Descubriendo juntos nuevos caminos 🌸"),
    ("Foto3.jpeg", "Risas que iluminan mis días 💫"),
    ("Foto4.jpeg", "Pequeños detalles que significan tanto 💕"),
    ("Foto5.jpeg", "Momentos que guardo en mi corazón 🎁"),
    ("Foto6.jpeg", "Sueños que construimos juntos 🌙"),
    ("Foto7.jpeg", "Siempre tú, siempre nosotros 💜")
]

# Mostrar imágenes intercaladas
for i, (ruta, mensaje) in enumerate(imagenes):
    img = Image.open(ruta)
    col1, col2 = st.columns([1, 1])

    if i % 2 == 0:
        with col1:
            st.image(img, use_column_width=True)
        with col2:
            st.markdown(f"<p style='color: #6A0DAD; font-size: 18px;'>{mensaje}</p>", unsafe_allow_html=True)
    else:
        with col1:
            st.markdown(f"<p style='color: #6A0DAD; font-size: 18px;'>{mensaje}</p>", unsafe_allow_html=True)
        with col2:
            st.image(img, use_column_width=True)

# Mensaje final
st.markdown(
    "<h2 style='text-align: center; color: #B565A7;'>Gracias por ser parte de mi vida 💖</h2>",
    unsafe_allow_html=True
)

