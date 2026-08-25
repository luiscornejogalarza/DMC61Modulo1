import streamlit as st
import numpy as np
if 'caja' not in st.session_state:
    st.session_state.caja = []

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
    # 1. Breve descripción con markdown
    st.header("Ejercicio 1 - Flujo de Caja")
    st.markdown("Registro interactivo de movimientos financieros para calcular ingresos, gastos y el saldo final.") 
    
    # 2. Widgets para ingresar los datos[cite: 1]
    # Usamos columnas para que la interfaz se vea profesional y ordenada
    col1, col2, col3 = st.columns(3)
    with col1:
        concepto = st.text_input("Concepto del movimiento")[cite: 1]
    with col2:
        tipo = st.selectbox("Tipo de movimiento", ["Ingreso", "Gasto"])[cite: 1]
    with col3:
        valor = st.number_input("Valor", min_value=0.0, step=10.0)[cite: 1]
        
    # 3. Botón para agregar movimientos[cite: 1]
    if st.button("Agregar movimiento"):[cite: 1]
        if concepto != "": # Validamos que no envíen campos vacíos
            # Agregamos el movimiento a nuestra lista en memoria
            st.session_state.caja.append({"Concepto": concepto, "Tipo": tipo, "Valor": valor})
            st.success("Movimiento registrado con éxito.")[cite: 1]
        else:
            st.error("Por favor, ingresa un concepto válido antes de guardar.")[cite: 1]
            
    # 4. Mostrar la tabla y los resultados[cite: 1]
    st.markdown("### Tabla de Movimientos Registrados")
    if len(st.session_state.caja) > 0:
        # Convertimos la lista de diccionarios en un DataFrame para mejor visualización
        df_caja = pd.DataFrame(st.session_state.caja)
        st.dataframe(df_caja, use_container_width=True)[cite: 1]
        
        # Cálculos de totales[cite: 1]
        ingresos = df_caja[df_caja['Tipo'] == 'Ingreso']['Valor'].sum()
        gastos = df_caja[df_caja['Tipo'] == 'Gasto']['Valor'].sum()
        saldo_final = ingresos - gastos
        
        # Uso de st.metric() para mostrar los KPIs[cite: 1]
        st.markdown("### Resumen Financiero")
        col_m1, col_m2, col_m3 = st.columns(3)
        col_m1.metric("Total Ingresos", f"${ingresos:.2f}")[cite: 1]
        col_m2.metric("Total Gastos", f"${gastos:.2f}")[cite: 1]
        col_m3.metric("Saldo Final", f"${saldo_final:.2f}")[cite: 1]
        
        # 5. Indicador del estado del flujo de caja[cite: 1]
        if saldo_final >= 0:
            st.success("El flujo de caja está **a favor**.")[cite: 1]
        else:
            st.error("El flujo de caja está **en contra**.")[cite: 1]
    else:
        st.info("Aún no hay movimientos registrados. Ingresa un movimiento en la parte superior.")
