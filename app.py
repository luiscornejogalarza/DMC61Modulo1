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
if 'pacientes_crud' not in st.session_state:
        st.session_state.pacientes_crud = {}
    
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
    st.markdown("Gestión de datos utilizando la clase `Paciente` con lógica de clasificación avanzada para implementar las operaciones CRUD.")
    
    # 1. Molde de la clase (Con la lógica de negocio enriquecida)
    class Paciente:
        def __init__(self, nombre, peso_kg, altura_m):
            self.nombre = nombre
            self.peso_kg = peso_kg
            self.altura_m = altura_m

        def calcular_imc(self):
            return self.peso_kg / (self.altura_m ** 2)

        def clasificacion_imc(self):
            # Lógica de clasificación avanzada incorporada en el método de la clase
            imc = self.calcular_imc()
            if imc < 18.5:
                return "Bajo peso"
            elif imc < 25:
                return "Peso normal"
            elif imc < 30:
                return "Sobrepeso"
            elif imc < 35:
                return "Obesidad"
            elif imc < 40:
                return "Obesidad grado II"
            elif imc < 50:
                return "Obesidad Morbida"
            elif imc < 60:
                return "Super obesidad"
            elif imc < 66:
                return "Supersuper obesidad"
            else:
                return "Triple obesidad"

        def resumen(self):
            return {
                "Nombre": self.nombre,
                "Peso (kg)": self.peso_kg,
                "Altura (m)": self.altura_m,
                "IMC": round(self.calcular_imc(), 2),
                "Estado": self.clasificacion_imc()
            }

    # Inicialización local de seguridad
    if 'pacientes_crud' not in st.session_state:
        st.session_state.pacientes_crud = {}

    # 2. Uso de st.tabs para organizar las operaciones
    tab_crear, tab_leer, tab_actualizar, tab_eliminar = st.tabs(["Crear", "Leer", "Actualizar", "Eliminar"])

    # --- C: CREAR ---
    with tab_crear:
        st.subheader("Registrar Nuevo Paciente")
        c_nombre = st.text_input("Nombre del Paciente")
        
        col_c1, col_c2 = st.columns(2)
        with col_c1:
            c_peso = st.number_input("Peso (kg)", min_value=1.0, value=70.0)
        with col_c2:
            c_altura = st.number_input("Altura (m)", min_value=0.5, value=1.70)
            
        if st.button("Crear Registro"):
            if c_nombre == "":
                st.error("El nombre no puede estar vacío.")
            elif c_nombre in st.session_state.pacientes_crud:
                st.warning("El paciente ya existe. Use la pestaña 'Actualizar'.")
            else:
                nuevo_paciente = Paciente(c_nombre, c_peso, c_altura)
                st.session_state.pacientes_crud[c_nombre] = nuevo_paciente
                st.success(f"Paciente '{c_nombre}' creado con éxito.")

    # --- R: LEER ---
    with tab_leer:
        st.subheader("Base de Datos de Pacientes")
        if len(st.session_state.pacientes_crud) > 0:
            datos = [obj.resumen() for obj in st.session_state.pacientes_crud.values()]
            st.dataframe(pd.DataFrame(datos), use_container_width=True)
        else:
            st.info("No hay pacientes registrados en el sistema.")

    # --- U: ACTUALIZAR ---
    with tab_actualizar:
        st.subheader("Modificar Datos Existentes")
        if len(st.session_state.pacientes_crud) > 0:
            opciones = list(st.session_state.pacientes_crud.keys())
            a_nombre = st.selectbox("Seleccione el paciente a actualizar:", opciones)
            
            col_a1, col_a2 = st.columns(2)
            with col_a1:
                a_peso = st.number_input("Nuevo Peso (kg)", min_value=1.0, value=70.0)
            with col_a2:
                a_altura = st.number_input("Nueva Altura (m)", min_value=0.5, value=1.70)
                
            if st.button("Actualizar Registro"):
                # Sobrescribimos el objeto existente
                paciente_actualizado = Paciente(a_nombre, a_peso, a_altura)
                st.session_state.pacientes_crud[a_nombre] = paciente_actualizado
                
                # Opcional pero recomendado: un pequeño mensaje temporal antes de recargar
                st.toast(f"Datos de '{a_nombre}' actualizados correctamente.") 
                
                # Forzamos la recarga inmediata de la interfaz
                st.rerun() 
        else:
            st.info("Registre un paciente primero para poder actualizarlo.")

    # --- D: ELIMINAR ---
    with tab_eliminar:
        st.subheader("Dar de Baja a un Paciente")
        if len(st.session_state.pacientes_crud) > 0:
            opciones_e = list(st.session_state.pacientes_crud.keys())
            e_nombre = st.selectbox("Seleccione el paciente a eliminar:", opciones_e)
            
            if st.button("Eliminar Registro"):
                del st.session_state.pacientes_crud[e_nombre]
                st.success(f"Paciente '{e_nombre}' eliminado del sistema.")
                st.rerun() # <--- Fuerza la recarga inmediata de la interfaz
        else:
            st.info("No hay pacientes para eliminar.")
