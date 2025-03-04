import streamlit as st
from utils import crear_empleados

# Crear los empleados
gerente, jefes, empleados = crear_empleados()

# UI con Streamlit
st.title("Sistema de Gestión de Recursos Humanos")

st.header("Gerente")
st.write(f"👔 {gerente.get_resumen()} - Estado: {gerente.get_estado()}")

st.header("Jefes de Área")
for jefe in jefes:
    st.subheader(jefe.get_resumen())
    st.text(f"Jefe inmediato: {jefe.get_jefe_inmediato()}")
    for empleado in jefe.subordinados:
        st.text(f"  - {empleado.get_resumen()} (Jefe inmediato: {empleado.get_jefe_inmediato()})")

st.header("Lista de Todos los Empleados")
for empleado in empleados:
    st.text(f"🔹 {empleado.get_resumen()} - Estado: {empleado.get_estado()}")
