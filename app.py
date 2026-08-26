import streamlit as st
import numpy as np
import pandas as pd
if 'caja' not in st.session_state:
    st.session_state.caja = []
if 'registro_numpy' not in st.session_state:
    st.session_state.registro_numpy = []
if 'historial_funciones' not in st.session_state:
    st.session_state.historial_funciones = []
if 'servidores_crud' not in st.session_state:
    st.session_state.servidores_crud = {}
    
# Sidebar
st.sidebar.title("Módulos")
menu = st.sidebar.selectbox(
    "Seleccione una sección:", 
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"])
    
# Home

if menu == "Home":
    st.title("Proyecto Aplicado en Streamlit")
    st.image("Python_logo1.png", width=300)
    st.subheader("Módulo 1 - Python Fundamentals")
    st.write("**Estudiante:** Luis Marco Cornejo Galarza")
    st.write("**Año:** 2026")
    st.markdown("Soy biólogo de formación, actualmente aplicando mis habilidades analíticas hacia la ingeniería de datos.")
    st.write("**Descripción:** Aplicación interactiva que integra variables, estructuras de datos, widgets, funciones, clases y lógica de programación en una interfaz interactiva.")
    st.write("**Tecnologías:** Python, Streamlit, Pandas, NumPy")

#Ejercicio 1 - Flujo de caja

elif menu == "Ejercicio 1":
    # Descripción con 
    st.header("Ejercicio 1 - Flujo de Caja")
    st.markdown("Registro interactivo de movimientos financieros para calcular ingresos, gastos y el saldo final.") 
    
    # Widgets para ingresar los datos
    col1, col2, col3 = st.columns(3)
    with col1:
        concepto = st.text_input("Concepto del movimiento")
    with col2:
        tipo = st.selectbox("Tipo de movimiento", ["Ingreso", "Gasto"])
    with col3:
        valor = st.number_input("Valor", min_value=0.0, step=10.0)
        
    # Botón para agregar movimientos
    if st.button("Agregar movimiento"):
        if concepto != "": 
            st.session_state.caja.append({"Concepto": concepto, "Tipo": tipo, "Valor": valor})
            st.success("Movimiento registrado.")
        else:
            st.error("Ingresa un concepto válido.")
            
    # Mostrar la tabla y los resultados
    st.markdown("### Tabla de Movimientos Registrados")
    if len(st.session_state.caja) > 0:
        df_caja = pd.DataFrame(st.session_state.caja)
        st.dataframe(df_caja, use_container_width=True)
        
        # Cálculos de totales
        ingresos = df_caja[df_caja['Tipo'] == 'Ingreso']['Valor'].sum()
        gastos = df_caja[df_caja['Tipo'] == 'Gasto']['Valor'].sum()
        saldo_final = ingresos - gastos
        
        st.markdown("### Resumen Financiero")
        col_m1, col_m2, col_m3 = st.columns(3)
        col_m1.metric("Total Ingresos", f"${ingresos:.2f}")
        col_m2.metric("Total Gastos", f"${gastos:.2f}")
        col_m3.metric("Saldo Final", f"${saldo_final:.2f}")
        
        # Indicador del flujo de caja
        if saldo_final >= 0:
            st.success("El flujo de caja **Positivo**.")
        else:
            st.error("El flujo de caja **en contra**.")
    else:
        st.info("Aún no hay movimientos registrados.")

#  Ejercicio 2 – Registro con NumPy, arrays y DataFrame

elif menu == "Ejercicio 2":
    # Descripción
    st.header("Ejercicio 2 - Registro con NumPy")
    st.markdown("Formulario interactivo para registrar productos. Los datos se capturan en arreglos (arrays) de NumPy y se estructuran dinámicamente en un DataFrame.")
    
    # Formulario de ingreso de datos estructurado en columnas
    col1, col2 = st.columns(2)
    with col1:
        producto = st.text_input("Nombre del producto")
        precio = st.number_input("Precio unitario", min_value=0.0, step=1.0)
    with col2:
        categoria = st.selectbox("Categoría", ["Herramientas", "Insumos", "Servicios", "Otros"])
        cantidad = st.number_input("Cantidad", min_value=1, step=1)
        
    # Botón para agregar nuevo registro
    if st.button("Agregar Registro"):
        if producto != "":
            # Cálculo del total 
            total = precio * cantidad
            
            # Almacenar la fila como un array de NumPy
            nuevo_array = np.array([producto, categoria, precio, cantidad, total])
            
            # Guardamos el array en la memoria de la sesión
            st.session_state.registro_numpy.append(nuevo_array)
            st.success("Registro agregado.")
        else:
            st.error("Ingresa el nombre del producto para continuar.")
            
    # La tabla en DataFrame actualizada
    st.markdown("### Base de Datos de Registros")
    if len(st.session_state.registro_numpy) > 0:
        # Requisito clave: Convertir la lista de arrays en un DataFrame
        df_numpy = pd.DataFrame(st.session_state.registro_numpy, columns=["Producto", "Categoría", "Precio", "Cantidad", "Total"])
        
        # Mostrar el DataFrame en pantalla
        st.dataframe(df_numpy, use_container_width=True)
    else:
        st.info("No hay registros, agrega el primer producto usando el formulario.")


# EJERCICIO 3 - Uso de funciones (Módulo Salud)

elif menu == "Ejercicio 3":
    st.header("Ejercicio 3 - Uso de Funciones")
    st.markdown("Cálculo de indicadores de salud y registro histórico de pacientes.")
    
    # Molde de la función de Salud
    def calcular_imc(peso_kg, altura_m):
        if peso_kg <= 0 or altura_m <= 0:
            raise ValueError("El peso y la altura deben ser mayores que cero.")
            
        imc = peso_kg / (altura_m ** 2)
        
        if imc < 18.5:
            clasificacion = "Bajo peso"
        elif imc < 25:
            clasificacion = "Peso normal"
        elif imc < 30:
            clasificacion = "Sobrepeso"
        elif imc < 35:
            clasificacion = "Obesidad"
        elif imc < 40:
            clasificacion = "Obesidad grado II"
        elif imc < 50:
            clasificacion = "Obesidad Morbida"
        elif imc < 60:
            clasificacion = "Super obesidad"
        elif imc < 66:
            clasificacion = "Supersuper obesidad"
        else:
            clasificacion = "Triple obesidad"
            
        return {
            "imc": round(imc, 2),
            "clasificacion": clasificacion
        }

    # Selector de función
    funcion_seleccionada = st.selectbox("Seleccione la función a utilizar:", ["Calcular Índice de Masa Corporal (IMC)"])
    
    # Widgets 
    st.markdown("### Ingrese los datos del paciente:")
    col1, col2 = st.columns(2)
    with col1:
        peso = st.number_input("Peso (kg)", min_value=1.0, value=70.0, step=0.5)
    with col2:
        altura = st.number_input("Altura (m)", min_value=0.5, value=1.70, step=0.01)
        
    # 4. Botón para ejecutar
    if st.button("Ejecutar Cálculo"):
        try:
            # Ejecutar función y mostrar el resultado en pantalla
            resultado = calcular_imc(peso, altura)
            st.success("Cálculo realizado con éxito.")
            st.write("**Resultados obtenidos:**")
            st.write(f"- IMC: {resultado['imc']}")
            st.write(f"- Clasificación: {resultado['clasificacion']}")
            
            # Guardar un histórico de resultados
            nuevo_resultado = {
                "Peso (kg)": peso,
                "Altura (m)": altura,
                "IMC": resultado['imc'],
                "Clasificación": resultado['clasificacion']
            }
            st.session_state.historial_funciones.append(nuevo_resultado)
            
        except ValueError as e:
            st.error(f"Error en el cálculo: {e}")
            
    # Tabla histórica
    st.markdown("### Histórico de Cálculos")
    if len(st.session_state.historial_funciones) > 0:
        df_historial = pd.DataFrame(st.session_state.historial_funciones)
        st.dataframe(df_historial, use_container_width=True)
    else:
        st.info("No hay cálculos registrados en el histórico aún.")

# EJERCICIO 4: Uso de clases con CRUD

elif menu == "Ejercicio 4":
    st.header("Ejercicio 4 - Clases y Operaciones CRUD")
    st.markdown("Gestión de infraestructura simulando un sistema de monitoreo de servidores (Crear, Leer, Actualizar, Eliminar).")
    
    # 1. Molde de la clase (Orientación a Objetos)
    class Servidor:
        def __init__(self, nombre, tiempo_total_h, tiempo_caida_h, almacenamiento_total_gb, almacenamiento_usado_gb):
            self.nombre = nombre
            self.tiempo_total_h = tiempo_total_h
            self.tiempo_caida_h = tiempo_caida_h
            self.almacenamiento_total_gb = almacenamiento_total_gb
            self.almacenamiento_usado_gb = almacenamiento_usado_gb

        def calcular_disponibilidad(self):
            if self.tiempo_total_h == 0: 
                return 0
            return ((self.tiempo_total_h - self.tiempo_caida_h) / self.tiempo_total_h) * 100

        def resumen(self):
            return {
                "Servidor": self.nombre,
                "Disponibilidad (%)": round(self.calcular_disponibilidad(), 2),
                "Almacen. Total (GB)": self.almacenamiento_total_gb,
                "Almacen. Usado (GB)": self.almacenamiento_usado_gb
            }

    # 2. Uso de st.tabs para organizar las operaciones de manera profesional
    tab_crear, tab_leer, tab_actualizar, tab_eliminar = st.tabs(["Crear", "Leer", "Actualizar", "Eliminar"])

    # --- C: CREAR ---
    with tab_crear:
        st.subheader("Registrar Nuevo Servidor")
        col_c1, col_c2 = st.columns(2)
        with col_c1:
            c_nombre = st.text_input("Identificador del Servidor")
            c_t_total = st.number_input("Tiempo total operando (h)", min_value=1.0, value=720.0)
        with col_c2:
            c_t_caida = st.number_input("Tiempo de caída (h)", min_value=0.0, value=0.0)
            c_a_total = st.number_input("Almacenamiento Total (GB)", min_value=1.0, value=1000.0)
            c_a_usado = st.number_input("Almacenamiento Usado (GB)", min_value=0.0, value=100.0)
            
        if st.button("Crear Registro"):
            if c_nombre == "":
                st.error("El identificador no puede estar vacío.")
            elif c_nombre in st.session_state.servidores_crud:
                st.warning("El servidor ya existe. Use la pestaña 'Actualizar'.")
            else:
                # Instanciamos el objeto y lo guardamos en el diccionario
                nuevo_serv = Servidor(c_nombre, c_t_total, c_t_caida, c_a_total, c_a_usado)
                st.session_state.servidores_crud[c_nombre] = nuevo_serv
                st.success(f"Servidor '{c_nombre}' creado con éxito.")

    # --- R: LEER ---
    with tab_leer:
        st.subheader("Visualización de Infraestructura")
        if len(st.session_state.servidores_crud) > 0:
            # Extraemos el resumen de cada objeto y lo convertimos a DataFrame
            datos = [obj.resumen() for obj in st.session_state.servidores_crud.values()]
            df_servidores = pd.DataFrame(datos)
            st.dataframe(df_servidores, use_container_width=True)
        else:
            st.info("No hay servidores registrados en la base de datos temporal.")

    # --- U: ACTUALIZAR ---
    with tab_actualizar:
        st.subheader("Modificar Servidor Existente")
        if len(st.session_state.servidores_crud) > 0:
            opciones = list(st.session_state.servidores_crud.keys())
            a_nombre = st.selectbox("Seleccione el servidor a actualizar:", opciones)
            
            col_a1, col_a2 = st.columns(2)
            with col_a1:
                a_t_total = st.number_input("Nuevo Tiempo total (h)", min_value=1.0, value=720.0)
                a_t_caida = st.number_input("Nuevo Tiempo de caída (h)", min_value=0.0, value=0.0)
            with col_a2:
                a_a_total = st.number_input("Nuevo Almacenamiento Total (GB)", min_value=1.0, value=1000.0)
                a_a_usado = st.number_input("Nuevo Almacenamiento Usado (GB)", min_value=0.0, value=150.0)
                
            if st.button("Actualizar Registro"):
                # Sobrescribimos el objeto existente con los nuevos valores
                serv_actualizado = Servidor(a_nombre, a_t_total, a_t_caida, a_a_total, a_a_usado)
                st.session_state.servidores_crud[a_nombre] = serv_actualizado
                st.success(f"Datos de '{a_nombre}' actualizados correctamente.")
        else:
            st.info("Registre un servidor primero para poder actualizarlo.")

    # --- D: ELIMINAR ---
    with tab_eliminar:
        st.subheader("Dar de Baja Servidor")
        if len(st.session_state.servidores_crud) > 0:
            opciones_e = list(st.session_state.servidores_crud.keys())
            e_nombre = st.selectbox("Seleccione el servidor a eliminar:", opciones_e)
            
            if st.button("Eliminar Registro"):
                del st.session_state.servidores_crud[e_nombre]
                st.success(f"Servidor '{e_nombre}' eliminado del sistema.")
        else:
            st.info("No hay servidores para eliminar.")
