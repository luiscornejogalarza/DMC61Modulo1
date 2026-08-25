import streamlit as st
import numpy as np

#sidebar
st.sidebar.title("Parámetros")
menu = st.sidebar.selectbox(
    "Seleccione una sección:", 
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"])
    
#Home

if menu == "Home":
    st.title("Proyecto Aplicado en Streamlit")
    st.image("Python_logo1.png", width=300)
    st.subheader("Módulo 1 - Python Fundamentals")
    st.write("**Estudiante:** Luis Marco Cornejo Galarza")
    st.write("**Año:** 2026")
    st.markdown("Soy biólogo de formación, actualmente aplicando mis habilidades analíticas hacia la ingeniería de datos.")
    st.write("**Descripción:** Aplicación interactiva que integra variables, estructuras de datos, widgets, funciones, clases y lógica de programación en una interfaz interactiva.")
    st.write("**Tecnologías:** Python, Streamlit, Pandas, NumPy")

#Ejercicio 1 :Flujo de caja

elif menu == "Ejercicio 1":
    st.header("Ejercicio 1 - Flujo de Caja")
    st.write("Registra movimientos financieros.") #[cite: 1]
    
    concepto = st.text_input("Concepto") #[cite: 1]
    tipo = st.selectbox("Tipo de movimiento", ["Ingreso", "Gasto"]) #[cite: 1]
    valor = st.number_input("Valor", min_value=0.0) #[cite: 1]
    
    if st.button("Agregar Movimiento"): #[cite: 1]
        st.session_state.caja.append({"Concepto": concepto, "Tipo": tipo, "Valor": valor})
        st.success("Agregado") #[cite: 1]
        
    if st.session_state.caja:
        df_caja = pd.DataFrame(st.session_state.caja)
        st.dataframe(df_caja) #[cite: 1]
        
        ingresos = df_caja[df_caja['Tipo'] == 'Ingreso']['Valor'].sum()
        gastos = df_caja[df_caja['Tipo'] == 'Gasto']['Valor'].sum()
        saldo = ingresos - gastos
        
        st.metric("Total Ingresos", f"${ingresos}") #[cite: 1]
        st.metric("Total Gastos", f"${gastos}") #[cite: 1]
        st.metric("Saldo Final", f"${saldo}") #[cite: 1]
        
        if saldo >= 0:
            st.success("Flujo a favor") #[cite: 1]
        else:
            st.error("Flujo en contra") #[cite: 1]
