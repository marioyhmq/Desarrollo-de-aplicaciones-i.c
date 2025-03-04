import streamlit as st
from src.utils import crear_empleados, formatear_datos

def main():
    st.title("Gestión de Empleados - Business Corporation")
    empleados = crear_empleados()
    df = formatear_datos(empleados)
    
    st.write("Lista de empleados:")
    st.table(df)
    
if __name__ == "__main__":
    main()
