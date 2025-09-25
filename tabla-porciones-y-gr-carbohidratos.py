
import streamlit as st

# Datos extraídos y organizados en un diccionario
carb_data = {
    "Vegetales": {
        "Papa": {"porcion": "1 unidad chica ó 100 g", "carbs": 15},
        "Choclo en grano": {"porcion": "½ taza ó ½ lata", "carbs": 15},
        "Choclo entero": {"porcion": "½ unidad", "carbs": 15},
        "Mandioca": {"porcion": "½ unidad chica o 100 g", "carbs": 30},
        "Batata": {"porcion": "½ unidad chica o 100 g", "carbs": 30},
        "Purée de batata": {"porcion": "½ taza", "carbs": 30},
        "Purée de papa": {"porcion": "½ taza", "carbs": 15},
        "Purée de papas instantáneo": {"porcion": "2 cucharadas soperas", "carbs": 15},
        "Calabaza": {"porcion": "1 taza (cocida) ó 2 rodajas gruesas", "carbs": 15},
        "Zapallo": {"porcion": "1 taza (cocida) ó 2 rodajas gruesas", "carbs": 15},
        "Palta": {"porcion": "1 unidad mediana", "carbs": 15},
        "Remolacha": {"porcion": "1 taza cocida ó 1 unidad grande de 150 g", "carbs": 15},
        "Zanahoria": {"porcion": "1 unidad grande", "carbs": 15}
    },
    "Frutas Frescas": {
        "Ananá": {"porcion": "1 compotera ó 2 rodajas finas", "carbs": 15},
        "Banana": {"porcion": "200 g ó 1 unidad chica", "carbs": 15},
        "Cerezas": {"porcion": "15 unidades", "carbs": 15},
        "Ciruelas": {"porcion": "2 unidades medianas", "carbs": 15},
        "Damascos": {"porcion": "3 unidades grandes", "carbs": 15},
        "Duraznos": {"porcion": "1 unidad mediana (150 g aprox)", "carbs": 15},
        "Frutillas": {"porcion": "1 taza de granos", "carbs": 15},
        "Granada": {"porcion": "½ taza de granos", "carbs": 15},
        "Melón": {"porcion": "1 rodaja de 200 g", "carbs": 15},
        "Mandarina": {"porcion": "1 unidad grande ó 2 chiquitas", "carbs": 15},
        "Mango": {"porcion": "1 unidad chica de 250 g", "carbs": 30},
        "Manzana": {"porcion": "1 unidad aprox (150 g)", "carbs": 15},
        "Moras / Arándanos": {"porcion": "1 compotera ó ½ taza", "carbs": 15},
        "Naranja": {"porcion": "1 unidad mediana", "carbs": 15},
        "Peras": {"porcion": "1 unidad chica de 100 g", "carbs": 15},
        "Pomelo": {"porcion": "½ unidad grande", "carbs": 15},
        "Sandía": {"porcion": "2 compoteras", "carbs": 15},
        "Uvas": {"porcion": "12 unidades (chicas) ó 10 (grandes)", "carbs": 15},
        "Kiwi": {"porcion": "2 unidades chiquitas", "carbs": 15},
        "Higos": {"porcion": "2 unidades chiquitas", "carbs": 15},
        "Frambuesas": {"porcion": "½ taza ó 1 compotera", "carbs": 15}
    },
    "Frutas Desecadas": {
        "Ciruelas": {"porcion": "3 unidades", "carbs": 15},
        "Damascos": {"porcion": "3 unidades", "carbs": 15},
        "Higos secos": {"porcion": "2 unidades", "carbs": 15},
        "Duraznos": {"porcion": "1 unidad", "carbs": 15},
        "Peras": {"porcion": "1 unidad", "carbs": 15},
        "Manzanas": {"porcion": "1 unidad", "carbs": 15},
        "Pasas de uva": {"porcion": "1 pocillo (25 g)", "carbs": 15},
        "Frutas secas": {"porcion": "10-15 unidades (30 g)", "carbs": 15}
    },
    "Frutas en Conserva o Enlatadas": {
        "Purée de manzana": {"porcion": "½ taza de té", "carbs": 15},
        "Ananá en lata, dietético": {"porcion": "2 rodajas", "carbs": 15},
        "Cóctel de frutas, dietético": {"porcion": "1 compotera", "carbs": 15},
        "Duraznos en lata, dietéticos": {"porcion": "2 mitades", "carbs": 15}
    },
    "Cereales y Pastas": {
        "Avena (cocida)": {"porcion": "½ taza ó 2 cucharadas soperas", "carbs": 15},
        "Almíbar de maíz o harina de mandioca": {"porcion": "1 cucharada sopera (aprox 20 g)", "carbs": 15},
        "Arroz blanco o integral cocido": {"porcion": "1 taza", "carbs": 45},
        "Arroz blanco o integral cocido": {"porcion": "1 cucharada de servir", "carbs": 15},
        "Arroz blanco o integral cocido": {"porcion": "½ plato", "carbs": 30},
        "Arroz blanco o integral cocido": {"porcion": "1 pocillo tipo café", "carbs": 15},
        "Arroz blanco o integral cocido": {"porcion": "1 cucharada sopera", "carbs": 15},
        "Canelones": {"porcion": "1 unidad grande", "carbs": 15},
        "Harina": {"porcion": "2 cucharadas soperas", "carbs": 15},
        "Masa de panqueque": {"porcion": "2 unidades (25 g c/u)", "carbs": 15},
        "Noquis": {"porcion": "10-12 unidades", "carbs": 15},
        "Noquis de sémola": {"porcion": "2 unidades (20 g)", "carbs": 15},
        "Pasta cocida (fideos, polenta, y otros pastas)": {"porcion": "½ plato playo", "carbs": 30},
        "Pasta cocida (fideos, polenta, y otros pastas)": {"porcion": "½ taza", "carbs": 15},
        "Pasta cocida (fideos, polenta, y otros pastas)": {"porcion": "1 plato hondo colmado", "carbs": 75},
        "Raviolis": {"porcion": "½ plato ó 20 unidades", "carbs": 30},
        "Capelletini de jamón y queso": {"porcion": "3/4 taza", "carbs": 40},
        "Láminas para lasaña": {"porcion": "3 láminas", "carbs": 30}
    },
    "Panes": {
        "Pan de molde blanco tipo lactal integral": {"porcion": "1 rebanada de 25 g aprox", "carbs": 15},
        "Pan de molde blanco tipo lactal integral": {"porcion": "1 unidad (50 g)", "carbs": 30},
        "Pan árabe o pita": {"porcion": "1 unidad grande (50 g)", "carbs": 30},
        "Pan francés en rodajas": {"porcion": "2 unidades", "carbs": 15},
        "Sandwich de miga": {"porcion": "1 triángulo", "carbs": 15},
        "Tortilla de maíz ó tipo burrito": {"porcion": "1 unidad", "carbs": 15},
        "Pancto de salvado": {"porcion": "1 unidad de 25 g aprox", "carbs": 15},
        "Pan de pancho": {"porcion": "1 unidad", "carbs": 30},
        "Pan de fajitas": {"porcion": "1 unidad", "carbs": 20},
        "Pan de francones": {"porcion": "2 rodajas finas", "carbs": 15},
        "Pan tipo pebete": {"porcion": "1 unidad de 50 g aprox", "carbs": 30}
    },
    "Otros Cereales": {
        "Barra de cereal": {"porcion": "1 unidad", "carbs": 15},
        "Copitos de desayuno azucarados o de chocolate": {"porcion": "1/4 de taza", "carbs": 15},
        "Copos de maíz, trigo, arroz, simples": {"porcion": "1/4 de taza", "carbs": 15},
        "Pororó con azúcar/tutúca": {"porcion": "2 tazas", "carbs": 15},
        "Pochoclo o pororó sin azúcar/tutúca": {"porcion": "3 tazas", "carbs": 15},
        "Cuadraditos de avena": {"porcion": "1/4 de taza", "carbs": 15}
    },
    "Galletitas": {
        "Galletitas con cereales": {"porcion": "3 unidades", "carbs": 15},
        "Galletitas rectangulares paquetes individuales": {"porcion": "Paquete de 40 g", "carbs": 30},
        "Galletita marinera, grande": {"porcion": "1 unidad", "carbs": 15},
        "Galletitas de agua, grandes": {"porcion": "2-3 unidades", "carbs": 15},
        "Galletitas de agua, chiquitas": {"porcion": "5 unidades", "carbs": 15},
        "Bizcochitos de grasa": {"porcion": "3 unidades", "carbs": 15},
        "Galletas de arroz o grandes/integrales/dulces (redondas)": {"porcion": "4 unidades", "carbs": 15},
        "Galletitas de maíz": {"porcion": "3 unidades", "carbs": 15},
        "Grisines/Talitas": {"porcion": "5 unidades chiquitas", "carbs": 15},
        "Mini tostadas": {"porcion": "5 unidades", "carbs": 15},
        "Mini tostadas": {"porcion": "½ taza de té", "carbs": 20},
        "Galletitas tipo bizcochitos": {"porcion": "6 unidades chiquitas", "carbs": 15}
    },
    "Alimentos Salados e Ingredientes de Copetin": {
        "Tapas de empanaditas": {"porcion": "2 unidades", "carbs": 15},
        "Snacks/Saladitos": {"porcion": "3 unidades", "carbs": 15},
        "Papas fritas/chichos/Pallitos salados": {"porcion": "Paquete chico (50 g aprox)", "carbs": 30},
        "Maní": {"porcion": "½ taza", "carbs": 10},
        "Papas fritas": {"porcion": "Paquete chico", "carbs": 25},
        "Papas fritas": {"porcion": "Paquete mediano", "carbs": 35},
        "Pizza a la piedra": {"porcion": "1/8 de unidad grande", "carbs": 15},
        "Masa de tarta": {"porcion": "1 porción (1/8 de tarta)", "carbs": 15},
        "Tapa de empanada": {"porcion": "1 unidad", "carbs": 15}
    },
    "Galletitas y Otros Dulces": {
        "Galleta tipo": {"porcion": "1 unidad (18 g)", "carbs": 15},
        "Galleta rellena chica (redonda)": {"porcion": "2 unidades", "carbs": 15},
        "Galleta simple (cuadrada)": {"porcion": "3 unidades", "carbs": 15},
        "Galleta rellena, grande (cuadrada)": {"porcion": "1 unidad", "carbs": 15},
        "Galletitas simples, chiquitas (rectangular)": {"porcion": "5 unidades", "carbs": 15},
        "Vainilla": {"porcion": "1 unidad", "carbs": 15},
        "Magdalenas": {"porcion": "1 unidad", "carbs": 15},
        "Obleas simples": {"porcion": "4 unidades", "carbs": 15},
        "Muffin": {"porcion": "1 unidad", "carbs": 30},
        "Budín de chocolate": {"porcion": "1 rebanada", "carbs": 30},
        "Budín de vainilla ó limón": {"porcion": "1 rebanada", "carbs": 15},
        "Factura con dulce": {"porcion": "1 unidad mediana", "carbs": 30},
        "Medialuna": {"porcion": "1 unidad", "carbs": 15},
        "Medialuna grande": {"porcion": "1 unidad", "carbs": 30},
        "Pan dulce": {"porcion": "1 rebanada chica", "carbs": 15},
        "Scones grandes": {"porcion": "1 unidad de 30 g aprox", "carbs": 15},
        "Scones chicos": {"porcion": "3 unidades (10 g cada uno)", "carbs": 15},
        "Tarta de frutas": {"porcion": "1 porción (1/8)", "carbs": 30},
        "Palmento": {"porcion": "1 unidad de 35 g aprox", "carbs": 15},
        "Bizcochuelo sin relleno": {"porcion": "1 porción", "carbs": 15},
        "Galletitas dulces, dietéticas": {"porcion": "4 unidades chiquitas", "carbs": 15},
        "Galletas de arroz, redondas": {"porcion": "2 unidades grandes", "carbs": 15},
        "Galletas de arroz, dulces integrales de avena o salvado": {"porcion": "4 unidades grandes", "carbs": 15},
        "Churros": {"porcion": "1 unidad", "carbs": 30}
    },
    "Lácteos y Derivados": {
        "Leche fermentada ácida": {"porcion": "1 unidad (100 cc)", "carbs": 15},
        "Leche fermentada": {"porcion": "1 unidad (100 cc)", "carbs": 8},
        "Leche fluida, entera o descremada": {"porcion": "1 taza (250 cc)", "carbs": 15},
        "Leche en polvo, entera": {"porcion": "3 g aprox (aproximadamente)", "carbs": 15},
        "Yogur bebible": {"porcion": "1 vaso de 200 cc", "carbs": 15},
        "Yogur bebible, dietético": {"porcion": "1 vaso de 200 cc", "carbs": 30},
        "Yogur dietético, compacto": {"porcion": "1 unidad", "carbs": 10},
        "Flan/postre, dietético": {"porcion": "1 compotera de 150 g", "carbs": 15},
        "Flan/postre": {"porcion": "1 unidad de 70 g", "carbs": 15},
        "Postre lácteo simple": {"porcion": "1 unidad de 120 g", "carbs": 25},
        "Yogur dietético con granola": {"porcion": "1 unidad de 170 g", "carbs": 25},
        "Yogur entero con cereales": {"porcion": "1 unidad de 170 g", "carbs": 45},
        "Flan infantil de leche o chocolate": {"porcion": "1 pote de 110 g", "carbs": 25},
        "Flan comercial con caramelo": {"porcion": "1 pote de 110 g", "carbs": 25},
        "Flan tipo casero, dietético": {"porcion": "1 porción", "carbs": 30},
        "Postre dietético de chocolate, crema americana, dulce de leche, tipo flan": {"porcion": "1 pote de 100 g", "carbs": 20},
        "Leche chocolatada, entera": {"porcion": "1 vaso de 200 cc", "carbs": 30},
        "Leche entera, chocolatada, dietética": {"porcion": "1 vaso de 150 cc", "carbs": 15},
        "Yogur dietético con colchón de frutas": {"porcion": "1 pote de 180 g", "carbs": 20},
        "Yogur tipo griego": {"porcion": "1 pote de 100 g", "carbs": 15},
        "Yogur con cereales": {"porcion": "1 vaso", "carbs": 25}
    },
    "Azúcar, Dulces y Golosinas": {
        "Azúcar": {"porcion": "3 cucharadas tipo té ó 6 sobreritos", "carbs": 15},
        "Dulce compacto": {"porcion": "1/2 porción (como 1/2 baraja)", "carbs": 30},
        "Dulce de batata, dietético": {"porcion": "2 cucharadas soperas", "carbs": 15},
        "Dulce de membrillo, dietético": {"porcion": "1 porción (1/2 baraja)", "carbs": 15},
        "Dulces o jaleas": {"porcion": "1½ cucharadas tipo té", "carbs": 15},
        "Gelatina común": {"porcion": "2 tazas (200 cc)", "carbs": 15},
        "Miel": {"porcion": "2 cucharadas soperas", "carbs": 15},
        "Mermelada de frutas": {"porcion": "3 cucharadas soperas", "carbs": 15},
        "Alfajor de chocolate": {"porcion": "1 unidad", "carbs": 30},
        "Barra de cereal, dietética": {"porcion": "1 unidad chica (14 g)", "carbs": 15},
        "Caramelo": {"porcion": "3 unidades", "carbs": 15},
        "Barras de chocolate y cereales, dietética": {"porcion": "1 unidad", "carbs": 15},
        "Chocolate de taza": {"porcion": "1 barrita", "carbs": 15},
        "Galleta rellena de chocolate": {"porcion": "3 cucharadas de té", "carbs": 15},
        "Turrón de almendras": {"porcion": "Porción de 20 g", "carbs": 15},
        "Merengue": {"porcion": "1 unidad chica", "carbs": 15},
        "Turrón de maní": {"porcion": "1 unidad chica (25 g)", "carbs": 15},
        "Turrón de maní": {"porcion": "1 unidad (30 g)", "carbs": 30},
        "Huevo de pascua": {"porcion": "1 unidad de 25 g", "carbs": 15},
        "Alfajor de galleta de arroz": {"porcion": "1 unidad", "carbs": 15},
        "Cucurucho tipo barquillo": {"porcion": "1 unidad", "carbs": 15}
    },
    "Helados": {
        "Casata de tres gustos": {"porcion": "1 unidad (125 g)", "carbs": 15},
        "Helado Bombón": {"porcion": "2 unidades (27 g c/u)", "carbs": 15},
        "Helado": {"porcion": "1 unidad (135 g)", "carbs": 15},
        "Helado de vainilla": {"porcion": "1 unidad", "carbs": 15},
        "Helado": {"porcion": "1 bocha", "carbs": 15}
    },
    "Algunas Comidas Regionales": {
        "Chipá": {"porcion": "1 unidad grande", "carbs": 30},
        "Empanada árabe": {"porcion": "1 unidad", "carbs": 30},
        "Empanada (de humita o tapa de empanadas)": {"porcion": "1 unidad", "carbs": 30},
        "Humita en chala": {"porcion": "1 porción", "carbs": 30},
        "Locro": {"porcion": "1 plato hondo", "carbs": 75},
        "Tamales": {"porcion": "2 unidades", "carbs": 15},
        "Tortas fritas": {"porcion": "1 unidad grande", "carbs": 30},
        "Choclo o tortilla": {"porcion": "1 unidad", "carbs": 15},
        "Sushi tipo roll": {"porcion": "1 pieza", "carbs": 5},
        "Sushi tipo Nigiri": {"porcion": "1 pieza", "carbs": 5},
        "Ensalada Rusa": {"porcion": "½ plato", "carbs": 30},
        "Milanesas": {"porcion": "1 unidad mediana", "carbs": 15}
    },
    "Bebidas": {
        "Gaseosa común": {"porcion": "1 vaso chico (150 cc)", "carbs": 15},
        "Cerveza": {"porcion": "1 vaso grande tipo chop (300 cc)", "carbs": 15},
        "Sidra etílica blanca y champagne dulce": {"porcion": "1 copa tipo (120 cc)", "carbs": 15},
        "Jugo de naranja o melo natural": {"porcion": "½ vaso (100 cc)", "carbs": 15},
        "Jugo natural": {"porcion": "1 copa tipo", "carbs": 15},
        "Jugo comercial": {"porcion": "1 vaso (200 cc)", "carbs": 15},
        "Jugo comercial, dietético": {"porcion": "1 vaso (200 cc)", "carbs": 5},
        "Bebida energizante": {"porcion": "250 cc", "carbs": 15}
    }
}

# Configuración de la aplicación Streamlit
st.title("Consulta de Carbohidratos por Alimento")
st.write("Selecciona una categoría y un alimento para ver la información nutricional.")

# Selección de categoría
category = st.selectbox("Categoría", list(carb_data.keys()))

# Selección de alimento dentro de la categoría
food_options = list(carb_data[category].keys())
food = st.selectbox("Alimento", food_options)

# Mostrar información
if food:
    food_info = carb_data[category][food]
    st.write(f"**Porción:** {food_info['porcion']}")
    st.write(f"**Gramos de carbohidratos:** {food_info['carbs']}")

# Nota adicional
st.write("**Nota:** Los valores son aproximados y pueden variar según la marca o preparación. Consulta a un nutricionista para un manejo personalizado.")

# Instrucciones para ejecución
st.write("**Instrucciones:** Ejecuta este script con Streamlit (`streamlit run app.py`) para ver la aplicación en tu navegador local.")