
def exploracion_basica(df):
    print("=== EXPLORACIÓN BÁSICA DEL DATASET ===")
    print("\nPrimeras filas:")
    print(df.head())
    print("\nÚltimas filas:")
    print(df.tail())
    print("\nNúmero de filas y columnas:")
    print(df.shape)
    print("\nInformación general del DataFrame:")
    print(df.info())
    print("\nEstadísticas descriptivas:")
    print(df.describe())
    print("\nColumnas:")
    print(list(df.columns))

def frecuencias_categoricas(df, top=5):
    print("=== FRECUENCIAS DE VARIABLES CATEGÓRICAS ===")
    columnas_categoricas = df.select_dtypes(include="O")
    
    if columnas_categoricas.empty:
        print("No hay columnas categóricas.")
        return
    
    for nombre_columna in columnas_categoricas.columns:
        print(f"\nValores únicos para la columna: {nombre_columna.upper()}")
        print(df[nombre_columna].value_counts(dropna=False).reset_index().head(top))

def identificar_nulos(df):
    print("=== COLUMNAS CON VALORES NULOS ===")
    nulos_por_columna = df.isnull().sum()
    nulos_por_columna = nulos_por_columna[nulos_por_columna > 0]
    if nulos_por_columna.empty:
        print("No se encontraron valores nulos en el dataset.")
    else:
        print(nulos_por_columna)

def imputar_nulos(df):
    print("=== IMPUTACIÓN DE VALORES NULOS ===")
    
    columnas_categoricas = df.select_dtypes(include='object').columns
    for nombre_columna_categorica in columnas_categoricas:
        if df[nombre_columna_categorica].isnull().sum() > 0:
            df[nombre_columna_categorica].fillna("Unknown", inplace=True)
            print(f"Nulos en '{nombre_columna_categorica}' imputados con 'Unknown'")
    
    columnas_numericas = df.select_dtypes(include='number').columns
    for nombre_columna_numerica in columnas_numericas:
        if df[nombre_columna_numerica].isnull().sum() > 0:
            media = df[nombre_columna_numerica].mean()
            df[nombre_columna_numerica].fillna(media, inplace=True)
            print(f"Nulos en '{nombre_columna_numerica}' imputados con la media ({media:.2f})")

def detectar_duplicados(df):
    numero_duplicados = df.duplicated().sum()
    print(f"Filas duplicadas completas en el dataset: {numero_duplicados}")
    if numero_duplicados > 0:
        print("Aquí tienes las filas duplicadas:")
        print(df[df.duplicated()])

def tipos_de_dato(df):
    print("=== TIPOS DE DATO POR COLUMNA ===")
    print(df.dtypes)

def contar_valores_unicos(df):
    print("=== CANTIDAD DE VALORES ÚNICOS POR COLUMNA ===")
    valores_unicos = df.nunique()
    print(valores_unicos)

def resumen_medidas(df):
    print("=== MEDIA, MEDIANA Y MODA DE VARIABLES NUMÉRICAS ===")
    
    columnas_numericas = df.select_dtypes(include='number')
    
    if columnas_numericas.empty:
        print("No hay columnas numéricas en el dataset.")
        return
    
    for nombre_columna in columnas_numericas.columns:
        print(f"\nColumna: {nombre_columna}")
        media = columnas_numericas[nombre_columna].mean()
        mediana = columnas_numericas[nombre_columna].median()
        moda = columnas_numericas[nombre_columna].mode()
        
        print(f"  Media: {media:.2f}")
        print(f"  Mediana: {mediana}")
        if len(moda) == 1:
            print(f"  Moda: {moda[0]}")
        else:
            print(f"  Moda (varias): {list(moda)}")

def mostrar_estadisticas_descriptivas(df):
    print("=== ESTADÍSTICAS DESCRIPTIVAS ===")
    
    # Seleccionar solo columnas numéricas
    columnas_numericas = df.select_dtypes(include='number')
    
    # Calcular describe() y redondear
    resumen = columnas_numericas.describe().round(2)
    
    # Mostrar
    display(resumen)