# -*- coding: utf-8 -*-
"""
Actualiza precio, imagen_url y descripcion de cada producto
con datos reales de mercado colombiano.

Uso:
    python manage.py actualizar_datos
    python manage.py actualizar_datos --preview   (solo muestra lo que haria)
"""

from django.core.management.base import BaseCommand
from catalogo.models import Producto
from decimal import Decimal

# ────────────────────────────────────────────────────────────────────────────
# DATOS POR PRODUCTO
# Clave = fragmento del nombre en mayusculas (se hace match parcial)
# Orden importa: los mas especificos van primero
# ────────────────────────────────────────────────────────────────────────────
DATOS_PRODUCTOS = [

    # ===== ARMARIOS =====
    {
        "match": ["ARMARIO DE TELA(JL- 01)", "ARMARIO DE TELA(JL- 02)", "ARMARIO DE TELA(JL- 03)"],
        "precio": Decimal("55000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_611788-MCO75346743457_032024-O.webp",
        "descripcion_corta": "Armario organizador de tela plegable con varios compartimentos y barra colgante.",
        "descripcion": "Armario de tela plegable ideal para organizar ropa, zapatos y accesorios. Fabricado en acero resistente con cubierta de tela no tejida de alta durabilidad. De facil montaje y desmontaje, perfecto para dormitorios, habitaciones infantiles y closets pequenos. Capacidad de carga hasta 30 kg. Incluye barra colgante y multiples estantes.",
    },
    {
        "match": ["ARMARIO DE TELA(JL- 04)", "ARMARIO DE TELA(JL- 05)"],
        "precio": Decimal("65000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_611788-MCO75346743457_032024-O.webp",
        "descripcion_corta": "Armario organizador de tela grande con multiple espacio de almacenamiento.",
        "descripcion": "Armario de tela de gran capacidad con diseno practico y resistente. Estructura metalica reforzada con cubierta en tela no tejida. Incluye zona de colgado, cajones y estantes. Facil de armar sin herramientas. Ideal para cualquier ambiente del hogar.",
    },
    {
        "match": ["ARMARIO DE NINO (JL-06)", "ARMARIO DE NINO AZUL (JL-13)", "ARMARIO DE NINO BLANCO (JL-18)", "ARMARIO DE NINO AZUL (JL- 19)", "ARMARIO DE NINO CARROS (JL-20)"],
        "precio": Decimal("68000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_856375-MCO75219985614_032024-O.webp",
        "descripcion_corta": "Armario infantil divertido con disenos especiales para ninos.",
        "descripcion": "Armario organizador infantil con divertidos estampados pensados para los mas pequenos del hogar. Estructura de acero segura y ligera con cubierta de tela resistente. Incluye barra para colgar ropa, estantes y zona de almacenamiento. Facil montaje sin herramientas. Disponible en varios disenos.",
    },
    {
        "match": ["ARMARIO DE NINA  (JL-07)", "ARMARIO DE PRINCESA (JL-17)"],
        "precio": Decimal("68000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_856375-MCO75219985614_032024-O.webp",
        "descripcion_corta": "Armario infantil con diseno de princesa, perfecto para ninas.",
        "descripcion": "Armario organizador disenado especialmente para ninas con motivos de princesa y colores delicados. Estructura robusta en acero con cubierta de tela de alta calidad. Incluye barra de ropa, estantes y cajones. Seguro, sin bordes cortantes. Facil montaje sin herramientas.",
    },
    {
        "match": ["ARMARIO ZAPATERO NEGRO (JL- 08)", "ARMARIO ZAPATERO NEGRO (JL- 15)"],
        "precio": Decimal("72000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_953506-MCO75010929637_032024-O.webp",
        "descripcion_corta": "Organizador de zapatos vertical negro con multiple niveles de almacenamiento.",
        "descripcion": "Armario zapatero vertical en color negro con varios niveles de almacenamiento para calzado. Fabricado en acero con recubrimiento en polvo resistente a la corrosion. Ideal para entrada, dormitorio o closet. Capacidad para 12 a 16 pares de zapatos segun el modelo. Estructura robusta y de facil armado.",
    },
    {
        "match": ["ARMARIO ZAPATERO BLANCO(JL- 09)", "ARMARIO ZAPATERO BLANCO (JL - 12)"],
        "precio": Decimal("72000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_953506-MCO75010929637_032024-O.webp",
        "descripcion_corta": "Organizador de zapatos vertical blanco, moderno y practico.",
        "descripcion": "Armario zapatero de diseno minimalista en color blanco. Estructura metalica resistente con acabado en polvo. Organiza eficientemente el calzado de toda la familia. Ideal para pasillos, dormitorios y cuartos de almacenamiento. Facil montaje, sin herramientas especiales.",
    },
    {
        "match": ["ARMARIO ZAPATERO ROSADO (JL - 10)"],
        "precio": Decimal("72000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_953506-MCO75010929637_032024-O.webp",
        "descripcion_corta": "Organizador de zapatos rosado, elegante y practico para el hogar.",
        "descripcion": "Armario zapatero en color rosado con diseno moderno y funcional. Estructura de acero con acabado en polvo de alta durabilidad. Mantiene el calzado organizado y accesible. Capacidad para multiples pares de zapatos. Facil ensamblaje sin herramientas.",
    },
    {
        "match": ["ARMARIO ZAPATERO AZUL (JL - 11)"],
        "precio": Decimal("72000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_953506-MCO75010929637_032024-O.webp",
        "descripcion_corta": "Zapatero vertical azul de alta capacidad para toda la familia.",
        "descripcion": "Armario zapatero en color azul con diseno practico y moderno. Fabricado en acero resistente con acabado en polvo. Ideal para organizar el calzado de adultos y ninos. Multiples niveles de almacenamiento. Armado simple, sin herramientas especializadas.",
    },
    {
        "match": ["ARMARIO DE 10 CAJONES(JL-14)"],
        "precio": Decimal("95000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_834036-MCO75093695553_032024-O.webp",
        "descripcion_corta": "Armario organizador con 10 cajones de tela para ropa y accesorios.",
        "descripcion": "Armario modular con 10 cajones de tela para una organizacion eficiente de ropa interior, calcetines, accesorios y mas. Estructura metalica robusta con cajones deslizantes de tela resistente. Compacto y de facil acceso. Ideal para dormitorios y closets donde se necesita orden sin ocupar mucho espacio.",
    },
    {
        "match": ["ARMARIO DE 16 CAJONES (JL-16)"],
        "precio": Decimal("115000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_834036-MCO75093695553_032024-O.webp",
        "descripcion_corta": "Gran armario con 16 cajones de tela, maximo espacio de organizacion.",
        "descripcion": "Armario modular con 16 cajones de tela para la maxima organizacion del hogar. Ideal para ropa, accesorios, papeleria y mas. Estructura metalica de alta resistencia con cajones deslizantes. Facil de armar y desmontar. Perfecto para dormitorios, oficinas y cuartos de almacenamiento.",
    },
    {
        "match": ["ARMARIO DE NEGRO (JL-21)", "ARMARIO DE BALNCO (JL- 23)"],
        "precio": Decimal("85000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_611788-MCO75346743457_032024-O.webp",
        "descripcion_corta": "Armario organizador de gran capacidad con barra y multiples estantes.",
        "descripcion": "Armario de tela de gran capacidad para adultos con barra colgante y multiples estantes de almacenamiento. Estructura de acero reforzada. Facil montaje sin herramientas. Ideal para dormitorios, habitaciones de servicio y espacios de almacenamiento.",
    },
    {
        "match": ["ARMARIO DE HOMBRE ARANA (JL-22)"],
        "precio": Decimal("68000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_856375-MCO75219985614_032024-O.webp",
        "descripcion_corta": "Armario infantil con diseno de Hombre Arana, ideal para ninos.",
        "descripcion": "Armario organizador infantil con el disenado emblematico del Hombre Arana. Fabricado con estructura metalica segura y cubierta de tela de alta calidad. Incluye barra de ropa, estantes y zona de almacenamiento. Totalmente seguro para ninos, sin bordes peligrosos. Facil montaje.",
    },

    # ===== RELOJES =====
    {
        "match": ["RELOJ CAJA AZUL"],
        "precio": Decimal("42000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_714657-MCO74748979701_022024-O.webp",
        "descripcion_corta": "Smartwatch con caja azul, multiples funciones y pantalla HD.",
        "descripcion": "Reloj inteligente con elegante caja azul, pantalla tactil de alta resolucion y multiples funciones de salud: monitor de frecuencia cardiaca, contador de pasos, monitor de sueno y notificaciones de smartphone. Compatible con Android e iOS. Bateria de larga duracion. Resistente al sudor.",
    },
    {
        "match": ["RELOJ CAJA NARANJA CON BLANCO"],
        "precio": Decimal("42000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_714657-MCO74748979701_022024-O.webp",
        "descripcion_corta": "Smartwatch naranja y blanco, deportivo y lleno de funciones.",
        "descripcion": "Reloj inteligente deportivo en llamativa combinacion naranja y blanco. Pantalla tactil clara con modo siempre encendido. Funciones de salud: ritmo cardiaco, oxigenacion en sangre, contador de pasos y calorias. Compatible con iOS y Android. Resistente al sudor, ideal para actividad fisica.",
    },
    {
        "match": ["RELOJ CAJA VERDE"],
        "precio": Decimal("42000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_714657-MCO74748979701_022024-O.webp",
        "descripcion_corta": "Smartwatch de caja verde, estilo deportivo y multiples sensores.",
        "descripcion": "Reloj inteligente con caja verde deportiva y pantalla de alta definicion. Incluye sensor de ritmo cardiaco, monitor de sueno, contador de pasos y resistencia al agua. Notificaciones de llamadas, mensajes y redes sociales. Compatible con iOS y Android. Correa intercambiable.",
    },
    {
        "match": ["T900PROMAX"],
        "precio": Decimal("58000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_625472-MCO75272424178_032024-O.webp",
        "descripcion_corta": "Smartwatch T900 Pro Max con pantalla AMOLED grande y NFC.",
        "descripcion": "El T900 Pro Max es un smartwatch premium con pantalla AMOLED de gran formato, NFC para pagos contactless y amplio conjunto de funciones de salud y deporte. Mide ritmo cardiaco, presion arterial, oxigenacion en sangre y sueno. Mas de 100 modos deportivos. Bateria de hasta 7 dias. Compatible con Android e iOS.",
    },
    {
        "match": ["T900"],
        "precio": Decimal("45000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_625472-MCO75272424178_032024-O.webp",
        "descripcion_corta": "Smartwatch T900 con gran pantalla y multiples funciones deportivas.",
        "descripcion": "Smartwatch T900 con pantalla tactil de gran tamano y diseno elegante. Monitor de ritmo cardiaco, contador de pasos, calorias y distancia. Mas de 8 modos deportivos. Notificaciones inteligentes para llamadas y mensajes. Bateria de larga duracion. Compatible con Android e iOS.",
    },
    {
        "match": ["C900"],
        "precio": Decimal("45000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_714657-MCO74748979701_022024-O.webp",
        "descripcion_corta": "Smartwatch C900, pantalla grande con funciones completas de salud.",
        "descripcion": "Smartwatch C900 con pantalla de alta definicion y funciones integrales de monitoreo de salud. Mide ritmo cardiaco, presion arterial y nivel de oxigeno en sangre. Incluye modos deportivos, recordatorios de actividad y notificaciones. Bateria de varios dias. Compatible con Android e iOS.",
    },
    {
        "match": ["BIG 2.0"],
        "precio": Decimal("48000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_625472-MCO75272424178_032024-O.webp",
        "descripcion_corta": "Smartwatch BIG 2.0 con pantalla extra grande y diseno sport.",
        "descripcion": "Smartwatch BIG 2.0 con pantalla de tamano extra grande para una visualizacion clara de toda la informacion. Monitor de salud completo: ritmo cardiaco, oxigenacion, sueno y pasos. Diseno deportivo con correa resistente. Compatible con Android e iOS. Bateria de larga duracion.",
    },

    # ===== BELLEZA =====
    {
        "match": ["DRILL DE UNAS"],
        "precio": Decimal("35000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_722803-MCO74498571684_022024-O.webp",
        "descripcion_corta": "Torno electrico para unas con multiples velocidades y accesorios.",
        "descripcion": "Drill electrico para manicura y pedicura profesional con velocidad regulable de hasta 30.000 rpm. Incluye multiples cabezales intercambiables para limar, pulir y dar forma a las unas. Motor silencioso y de bajo calentamiento. Ideal para uso domiciliario y profesional. Compacto y facil de usar.",
    },
    {
        "match": ["LAMPARA DE UNAS 72 W"],
        "precio": Decimal("42000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_954345-MCO74631913745_022024-O.webp",
        "descripcion_corta": "Lampara UV/LED 72W de curado rapido para esmaltes de gel.",
        "descripcion": "Lampara de unas UV/LED de 72 watts con curado ultra rapido en tan solo 30 segundos. Compatible con todos los tipos de gel, shellac y esmaltes de base UV. Sensor automatico de manos. Pantalla LCD con temporizador. Ligera y compacta, ideal para uso en casa y salon.",
    },
    {
        "match": ["LAMPARA DE UNAS LUNA"],
        "precio": Decimal("38000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_954345-MCO74631913745_022024-O.webp",
        "descripcion_corta": "Lampara UV/LED diseno luna para gel y esmaltes, curado eficiente.",
        "descripcion": "Lampara de unas con diseno semiluna en UV/LED, perfecta para curar geles y esmaltes semipermanentes. Amplia apertura que permite curar los 5 dedos simultaneamente. Temporizador integrado de 30, 60 y 90 segundos. Compacta y portatil. Ideal para uso domiciliario.",
    },
    {
        "match": ["LAMPARA DE UNAS 268 W"],
        "precio": Decimal("75000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_954345-MCO74631913745_022024-O.webp",
        "descripcion_corta": "Lampara profesional UV/LED 268W para curado ultrarapido de gel.",
        "descripcion": "Lampara profesional de unas UV/LED de 268 watts de alta potencia. Curado completo en 10 segundos. Amplia camara que permite curar manos y pies. Pantalla LCD con temporizador y ajuste de intensidad. Construccion premium, ideal para salones de belleza de alta demanda.",
    },
    {
        "match": ["LAMPARA DE UNAS"],
        "precio": Decimal("35000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_954345-MCO74631913745_022024-O.webp",
        "descripcion_corta": "Lampara UV/LED para curado de esmaltes de gel y unas acrilicas.",
        "descripcion": "Lampara UV/LED para curado de esmaltes de gel, shellac y resinas. Curado rapido y uniforme gracias a sus LEDs de alta potencia. Sensor automatico de manos. Incluye temporizador ajustable. Compacta y portatil. Ideal para uso domiciliario y profesional.",
    },
    {
        "match": ["SECADOR VERDE"],
        "precio": Decimal("55000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_641507-MCO74978024455_032024-O.webp",
        "descripcion_corta": "Secador de cabello verde de alta potencia con tecnologia ionica.",
        "descripcion": "Secador de cabello de alta potencia con tecnologia ionica para reducir el frizz y el encrespamiento. Dos velocidades y tres temperaturas ajustables. Boquilla concentradora incluida. Motor DC de larga vida util. Asa ergonomica antideslizante. Perfecto para uso diario en el hogar.",
    },
    {
        "match": ["SECADOR NUEVO", "SECADOR NEGRO"],
        "precio": Decimal("60000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_641507-MCO74978024455_032024-O.webp",
        "descripcion_corta": "Secador de cabello profesional de alta potencia con ionizador.",
        "descripcion": "Secador de cabello profesional con motor de alta potencia y tecnologia ionica avanzada. Tres temperaturas y dos velocidades para adaptarse a todo tipo de cabello. Incluye boquilla y difusor. Funcion de aire frio para fijar el estilo. Cable giratorio de 1.8 metros.",
    },
    {
        "match": ["SECADOR CEPILLO"],
        "precio": Decimal("65000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_641507-MCO74978024455_032024-O.webp",
        "descripcion_corta": "Cepillo secador 2 en 1 para secar y estilizar simultaneamente.",
        "descripcion": "Cepillo secador 2 en 1 que seca y estiliza el cabello en un solo paso. Cerdas de jabalina y nylon para un acabado profesional. Tecnologia ionica para reducir el frizz. Temperatura ajustable. Ideal para dar volumen y suavidad al cabello sin dano termico excesivo.",
    },
    {
        "match": ["DUO"],
        "precio": Decimal("75000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_641507-MCO74978024455_032024-O.webp",
        "descripcion_corta": "Set duo plancha y secador de cabello profesional todo en uno.",
        "descripcion": "Set profesional duo que incluye plancha y secador de cabello de alta potencia. Ambos equipos con tecnologia ionica y ceramica para un acabado brillante y sin frizz. Temperatura ajustable. Ideal como regalo o para completar el kit de estilismo en casa.",
    },
    {
        "match": ["PINZA DE ONDAS"],
        "precio": Decimal("48000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_841459-MCO74769437208_022024-O.webp",
        "descripcion_corta": "Pinza rizadora de ondas para crear rizos definidos y naturales.",
        "descripcion": "Pinza rizadora para crear ondas y rizos perfectos. Placa ceramica con recubrimiento de turmalina para distribucion uniforme del calor. Temperatura ajustable hasta 230 C. Calentamiento rapido en 30 segundos. Proteccion termica automatica. Ideal para todo tipo de cabello.",
    },
    {
        "match": ["PINZA DE CORONA"],
        "precio": Decimal("52000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_841459-MCO74769437208_022024-O.webp",
        "descripcion_corta": "Pinza de corona para ondas grandes y rizos amplios, efecto playa.",
        "descripcion": "Pinza de corona para crear ondas y rizos grandes de efecto playa. Su diseno especial permite una mayor anchura de rizo para resultados naturales y voluminosos. Recubrimiento ceramico de titanio. Temperatura ajustable. Sistema de seguridad automatico por sobrecalentamiento.",
    },
    {
        "match": ["PEINETA DE CALOR"],
        "precio": Decimal("38000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_841459-MCO74769437208_022024-O.webp",
        "descripcion_corta": "Peineta termica para alisar y peinar cabello rizado y afro.",
        "descripcion": "Peineta de calor electrica ideal para cabello rizado, crespo y afro. Dientes de acero inoxidable resistentes al calor. Temperatura ajustable para distintos tipos de cabello. Calentamiento rapido y uniforme. Asa ergonomica con proteccion termica. Transforma el cabello rizado en liso sedoso.",
    },
    {
        "match": ["CALLOS ROSADA"],
        "precio": Decimal("28000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_791099-MCO75234517282_032024-O.webp",
        "descripcion_corta": "Lima electrica rosada para eliminar callosidades de manos y pies.",
        "descripcion": "Lima electrica de pedicura en color rosado con cabezales abrasivos intercambiables para eliminar callosidades, pieles duras y asperezas de pies y manos. Motor silencioso de alta rotacion. Uso en seco o humedo. Compacta y portatil. Ideal para pedicura en casa.",
    },
    {
        "match": ["CALLOS BLANCA"],
        "precio": Decimal("28000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_791099-MCO75234517282_032024-O.webp",
        "descripcion_corta": "Lima electrica blanca para eliminar callosidades y pieles duras.",
        "descripcion": "Lima electrica de pedicura en color blanco con cabezales de lijado de diferente granulometria. Elimina eficientemente callosidades, pieles muertas y asperezas. Motor silencioso. Uso en seco o con agua. Compacta y de facil limpieza. Ideal para pedicura profesional en casa.",
    },
    {
        "match": ["CEPILLO FACIAL"],
        "precio": Decimal("35000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_947451-MCO74721264993_022024-O.webp",
        "descripcion_corta": "Cepillo electrico facial de limpieza profunda con cabezales intercambiables.",
        "descripcion": "Cepillo electrico para limpieza facial profunda con tecnologia de vibracion sonica. Cabezales intercambiables para diferentes tipos de piel. Elimina el doble de impurezas que el lavado manual. Impermeable para uso en la ducha. Bateria recargable via USB. Incluye base de carga.",
    },

    # ===== HOGAR =====
    {
        "match": ["ORAL IRRIGATOR"],
        "precio": Decimal("58000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_789914-MCO74827671524_022024-O.webp",
        "descripcion_corta": "Irrigador oral electrico para limpieza dental profunda y encias.",
        "descripcion": "Irrigador oral electrico con chorro de agua a presion regulable para una higiene dental completa. Elimina la placa bacteriana y restos de alimentos entre los dientes y en la linea de las encias. Deposito de agua extraible. Multiples boquillas incluidas. Recargable via USB. Impermeable.",
    },
    {
        "match": ["CEPILLO NINO"],
        "precio": Decimal("18000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_947451-MCO74721264993_022024-O.webp",
        "descripcion_corta": "Cepillo dental suave para ninos con mango ergonomico colorido.",
        "descripcion": "Cepillo dental infantil con cerdas extra suaves que cuidan el esmalte y las encias sensibles de los ninos. Mango ergonomico de facil agarre con disenos divertidos. Cabezal pequeno adaptado a la boca infantil. Ideal para establecer habitos de higiene desde la infancia.",
    },
    {
        "match": ["CEPILLO DE ADULTO"],
        "precio": Decimal("22000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_947451-MCO74721264993_022024-O.webp",
        "descripcion_corta": "Cepillo dental de adulto con cerdas suaves y mango ergonomico.",
        "descripcion": "Cepillo dental de adulto con cerdas suaves de alta calidad que limpian eficientemente sin dañar el esmalte ni las encias. Mango antideslizante ergonomico. Cabezal con acceso a zonas posteriores de dificil alcance. Ideal para uso diario dos veces al dia.",
    },
    {
        "match": ["CEPILLO DE LAVAR"],
        "precio": Decimal("25000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_613282-MCO74893547694_022024-O.webp",
        "descripcion_corta": "Cepillo electrico de limpieza multiusos para bano, cocina y hogar.",
        "descripcion": "Cepillo electrico de limpieza multiusos con cabezales intercambiables para distintas superficies. Motor potente de alta rotacion que facilita la limpieza de azulejos, juntas, lechadas y superficies difíciles. Resistente al agua. Incluye 3 cabezales. Mango ergonomico antideslizante.",
    },
    {
        "match": ["CEPILLO DE LOZA"],
        "precio": Decimal("22000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_613282-MCO74893547694_022024-O.webp",
        "descripcion_corta": "Cepillo para loza y platos con mango largo y cerdas resistentes.",
        "descripcion": "Cepillo para lavar loza y platos con mango largo ergonomico para mayor comodidad. Cerdas de nylon resistentes y de larga duracion. Dispenser de jabon integrado para facilitar el lavado. Ideal para fregar ollas, sartenes, platos y utensilios de cocina.",
    },
    {
        "match": ["MOP GIRATORIO"],
        "precio": Decimal("72000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_786451-MCO74632901218_022024-O.webp",
        "descripcion_corta": "Mop giratorio con balde escurridor de pedal, limpieza sin esfuerzo.",
        "descripcion": "Mop giratorio de 360 grados con balde escurridor de pedal para limpieza de pisos sin mojarse las manos. Mopa de microfibra lavable y reutilizable que atrapa el polvo y suciedad eficientemente. Mango telescopico ajustable. Ideal para pisos de ceramica, madera y vinyl. Facil de usar y lavar.",
    },
    {
        "match": ["LIMPIADOR DE ESPEJOS"],
        "precio": Decimal("32000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_613282-MCO74893547694_022024-O.webp",
        "descripcion_corta": "Limpiador magnetico de espejos y ventanas de doble cara.",
        "descripcion": "Limpiador magnetico de doble cara para espejos, ventanas y superficies de vidrio. Permite limpiar ambas caras del vidrio simultaneamente sin esfuerzo. Incluye raspador y pano de microfibra. Ideal para ventanas de dificil acceso. No requiere quimicos. Facil de usar.",
    },
    {
        "match": ["MOTOSIERRA"],
        "precio": Decimal("95000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_612978-MCO74893264917_022024-O.webp",
        "descripcion_corta": "Motosierra electrica portatil de mano para poda y corte de ramas.",
        "descripcion": "Motosierra electrica portatil de uso manual para poda de arboles, corte de ramas y madera. Motor electrico de alta potencia sin necesidad de gasolina ni aceite de cadena. Cadena de acero inoxidable con proteccion de seguridad. Ligera y de facil manejo. Ideal para jardineria y mantenimiento del hogar.",
    },
    {
        "match": ["HIDROLAVADORA INALAMBRICA"],
        "precio": Decimal("115000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_893413-MCO74718394023_022024-O.webp",
        "descripcion_corta": "Hidrolavadora inalambrica a bateria para limpieza de exterior.",
        "descripcion": "Hidrolavadora inalambrica a bateria recargable con motor de alta presion para limpieza de autos, motos, patios, fachadas y mas. Sin cable de poder para mayor comodidad y libertad de movimiento. Deposito de agua de gran capacidad. Incluye lanza regulable y accesorios. Ligera y compacta.",
    },
    {
        "match": ["ASPIRADORA GRANDE"],
        "precio": Decimal("120000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_768345-MCO74716804516_022024-O.webp",
        "descripcion_corta": "Aspiradora de alta potencia con filtro HEPA y gran capacidad.",
        "descripcion": "Aspiradora de alta potencia con filtro HEPA para capturar partículas de polvo, acaros y alergenos. Gran deposito de suciedad de alta capacidad. Multiples accesorios para superficies duras, tapetes y rincones. Motor potente y silencioso. Ruedas giratorias para facil movilidad.",
    },
    {
        "match": ["ASPIRADORA CAJA NARANJA"],
        "precio": Decimal("95000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_768345-MCO74716804516_022024-O.webp",
        "descripcion_corta": "Aspiradora compacta naranja sin bolsa con multiples accesorios.",
        "descripcion": "Aspiradora compacta sin bolsa en color naranja con potente succion ciclonica. Filtro lavable y reutilizable. Incluye boquillas para pisos duros, alfombras y esquinas. Deposito de polvo de facil vaciado. Compacta para almacenamiento. Ideal para apartamentos y casas de tamano medio.",
    },
    {
        "match": ["ASPIRADORA CAJA AZUL"],
        "precio": Decimal("95000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_768345-MCO74716804516_022024-O.webp",
        "descripcion_corta": "Aspiradora compacta azul con succion potente y facil uso.",
        "descripcion": "Aspiradora compacta en color azul con motor de succion de alto rendimiento. Filtro lavable de larga duracion. Accesorios para pisos duros y superficies tapizadas. Deposito de polvo translucido de facil vaciado. Diseno ergonomico con cable retractil. Ideal para uso cotidiano.",
    },
    {
        "match": ["ASPIRADORA CAJA VERDE"],
        "precio": Decimal("95000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_768345-MCO74716804516_022024-O.webp",
        "descripcion_corta": "Aspiradora compacta verde con filtro lavable y succion eficiente.",
        "descripcion": "Aspiradora compacta en color verde con sistema de filtracion lavable de alta eficiencia. Succion potente para eliminar polvo, pelo de mascotas y suciedad de pisos y tapetes. Accesorios incluidos. Deposito de facil vaciado. Diseno compacto ideal para espacios pequenos.",
    },
    {
        "match": ["PERCHERO DE ROPA"],
        "precio": Decimal("55000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_671459-MCO74893471829_022024-O.webp",
        "descripcion_corta": "Perchero de pie para ropa con doble barra y estante inferior.",
        "descripcion": "Perchero de ropa de pie con estructura metalica resistente y doble barra colgante de gran capacidad. Incluye estante inferior para calzado o accesorios. Ruedas giratorias para facil movilidad. Facil montaje sin herramientas. Ideal para dormitorios, tiendas de ropa y puntos de venta.",
    },
    {
        "match": ["CORTINAS DE BANO"],
        "precio": Decimal("32000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_613282-MCO74893547694_022024-O.webp",
        "descripcion_corta": "Cortina de bano resistente al agua con 12 ganchos incluidos.",
        "descripcion": "Cortina de bano fabricada en poliester impermeable de alta densidad, resistente al moho y al mildiu. Incluye 12 ganchos de plastico. Facil de lavar a maquina. Disponible en varios disenos. Medidas estandar para duchas y baneras. Refuerza el diseno y privacidad del bano.",
    },
    {
        "match": ["CANASTA DE TELA"],
        "precio": Decimal("28000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_671459-MCO74893471829_022024-O.webp",
        "descripcion_corta": "Canasta organizadora de tela plegable con asas reforzadas.",
        "descripcion": "Canasta organizadora de tela no tejida con estructura firme y asas reforzadas. Plegable para facil almacenamiento cuando no se usa. Ideal para guardar juguetes, ropa, revistas, mantas y accesorios. Disponible en varios tamanos y colores. Lavable a maquina.",
    },

    # ===== VENTILADORES =====
    {
        "match": ["VENTILADOR GATO"],
        "precio": Decimal("65000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_735782-MCO74638917321_022024-O.webp",
        "descripcion_corta": "Ventilador de escritorio diseno gato, silencioso y decorativo.",
        "descripcion": "Ventilador de escritorio con divertido diseno de gato, perfecto para habitaciones infantiles y escritorios. Motor silencioso de bajo consumo energetico. Tres velocidades ajustables. Cabezal giratorio de 360 grados. Facil de limpiar. Enchufe directo a corriente o puerto USB.",
    },
    {
        "match": ["VANTILADOR VERDE", "VENTILADO BLANCO 1"],
        "precio": Decimal("72000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_735782-MCO74638917321_022024-O.webp",
        "descripcion_corta": "Ventilador de pie con oscilacion y tres velocidades.",
        "descripcion": "Ventilador de pie con motor silencioso y eficiente. Tres velocidades ajustables para distintas necesidades de ventilacion. Cabezal oscilante de 90 grados. Altura regulable. Facil de desmontar para limpieza. Bajo consumo energetico. Ideal para sala, dormitorio y oficina.",
    },
    {
        "match": ["VENTILADOR BLANCO 2", "VENTILADOR BLANCO 3"],
        "precio": Decimal("78000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_735782-MCO74638917321_022024-O.webp",
        "descripcion_corta": "Ventilador de pie blanco silencioso con temporizador y control.",
        "descripcion": "Ventilador de pie de alta eficiencia con temporizador programable y control remoto incluido. Cinco velocidades ajustables para mayor comodidad. Oscilacion de 90 grados. Motor DC de bajo consumo. Pantalla LED con indicador de velocidad. Ideal para dormitorios y salas de gran tamano.",
    },
    {
        "match": ["VENTILADOR DOBLE BLANCO"],
        "precio": Decimal("95000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_735782-MCO74638917321_022024-O.webp",
        "descripcion_corta": "Ventilador doble blanco con dos aspas y mayor cobertura de aire.",
        "descripcion": "Ventilador de doble cabezal blanco para una cobertura de ventilacion superior. Motor potente y silencioso. Oscilacion de doble cabezal para distribucion uniforme del aire en espacios amplios. Tres velocidades y temporizador. Alto y delgado para facilitar su ubicacion.",
    },
    {
        "match": ["VENTILADOR DOBLE GRIS"],
        "precio": Decimal("95000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_735782-MCO74638917321_022024-O.webp",
        "descripcion_corta": "Ventilador doble gris de alto rendimiento para espacios amplios.",
        "descripcion": "Ventilador de doble cabezal en color gris con diseno moderno y funcional. Potente motor DC de bajo consumo. Doble flujo de aire para espacios grandes y calurosos. Velocidades multiples con control remoto. Oscilacion independiente por cabezal. Ideal para salas, oficinas y comercios.",
    },

    # ===== EJERCICIO =====
    {
        "match": ["RUEDA"],
        "precio": Decimal("28000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_894213-MCO74719293487_022024-O.webp",
        "descripcion_corta": "Rueda abdominal doble para ejercitar core y fortalecer abdomen.",
        "descripcion": "Rueda abdominal de doble rueda para mayor estabilidad durante los ejercicios. Ideal para fortalecer el core, abdomen, brazos y espalda. Manillar antideslizante de goma. Incluye rodillera de proteccion. Estructura de acero resistente. Compacta y facil de almacenar.",
    },
    {
        "match": ["SET DE BANDAS ELASTICAS"],
        "precio": Decimal("32000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_894213-MCO74719293487_022024-O.webp",
        "descripcion_corta": "Set de bandas elasticas de resistencia para entrenamiento funcional.",
        "descripcion": "Set de bandas elasticas de resistencia progresiva para entrenamiento funcional en casa o gimnasio. Incluye bandas de diferente resistencia (liviana, media y fuerte). Fabricadas en latex natural de alta durabilidad. Ideales para calentar, estirar, rehabilitar y entrenar diferentes grupos musculares.",
    },
    {
        "match": ["RODILLERA VERDE"],
        "precio": Decimal("25000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_913487-MCO74719019827_022024-O.webp",
        "descripcion_corta": "Rodillera compresiva verde para soporte y alivio del dolor de rodilla.",
        "descripcion": "Rodillera elastica de compresion en color verde para soporte de rodilla durante actividad fisica. Fabricada en neopreno de alta calidad con bandas antideslizantes. Alivia el dolor por artritis, tendinitis y lesiones deportivas. Talla ajustable. Lavable a maquina.",
    },
    {
        "match": ["RODILLERA AZUL"],
        "precio": Decimal("25000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_913487-MCO74719019827_022024-O.webp",
        "descripcion_corta": "Rodillera compresiva azul deportiva con soporte patela reforzado.",
        "descripcion": "Rodillera compresiva deportiva azul con soporte de rotula reforzado. Neopreno de alta densidad que mantiene el calor y mejora la circulacion. Ideal para deporte, rehabilitacion y uso cotidiano. Anillos antideslizantes en la parte superior e inferior. Talla ajustable con velcro.",
    },
    {
        "match": ["RODILLERA CALOR"],
        "precio": Decimal("28000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_913487-MCO74719019827_022024-O.webp",
        "descripcion_corta": "Rodillera termica de calor para alivio de dolor articular y muscular.",
        "descripcion": "Rodillera termica de compresion con turmalina que genera calor natural para aliviar el dolor articular y muscular. Mejora la circulacion y reduce la inflamacion. Fabricada en neopreno de alta calidad. Talla unica ajustable. Ideal para artritis, reumatismo y recuperacion deportiva.",
    },
    {
        "match": ["MASAJEADOR 4 EN 1"],
        "precio": Decimal("55000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_788123-MCO74719482918_022024-O.webp",
        "descripcion_corta": "Masajeador electrico 4 en 1 para cuello, espalda, piernas y pies.",
        "descripcion": "Masajeador electrico multifuncion 4 en 1 con cuatro cabezales intercambiables para cuello, espalda, piernas y pies. Seis modos de masaje: amasado, percusion, vibracion y combinados. Intensidad regulable. Funcion de calor. Recargable via USB. Ligero y portatil.",
    },
    {
        "match": ["MASAJEADOR X12"],
        "precio": Decimal("48000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_788123-MCO74719482918_022024-O.webp",
        "descripcion_corta": "Masajeador manual tipo pistola de percusion con 12 cabezales.",
        "descripcion": "Masajeador de percusion profesional con 12 cabezales intercambiables para distintas zonas y tipos de masaje. Motor de alta frecuencia para alivio profundo de tensiones musculares. Tres velocidades de percusion. Bateria recargable. Silencioso y portatil. Ideal para recuperacion deportiva.",
    },
    {
        "match": ["MASAJEADOR AZUL"],
        "precio": Decimal("42000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_788123-MCO74719482918_022024-O.webp",
        "descripcion_corta": "Masajeador azul vibracional para cuello y hombros con calor.",
        "descripcion": "Masajeador en color azul con funcion de calor y vibracion para cuello, hombros y espalda. Tres niveles de intensidad ajustables. Forma ergonomica en U que se adapta al contorno del cuello. Recargable via USB. Silicona suave al tacto. Ideal para aliviar el estres y la tension diaria.",
    },
    {
        "match": ["MASAJEADOR"],
        "precio": Decimal("38000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_788123-MCO74719482918_022024-O.webp",
        "descripcion_corta": "Masajeador electrico portatil para alivio de dolor muscular.",
        "descripcion": "Masajeador electrico portatil con multiples modos de vibracion para alivio de dolor muscular y tension. Diseno ergonomico de facil manejo. Intensidad regulable. Recargable via USB. Compacto y ligero para llevar a cualquier lugar. Ideal para uso en casa, oficina o post entrenamiento.",
    },

    # ===== MOSQUITOS =====
    {
        "match": ["MINI LINTERNA DE MOSQUITOS"],
        "precio": Decimal("22000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_712341-MCO74893048291_022024-O.webp",
        "descripcion_corta": "Mini linterna UV antimosquitos portatil y recargable.",
        "descripcion": "Mini linterna UV 2 en 1: atrae y elimina mosquitos con luz ultravioleta y ademas funciona como linterna. Recargable via USB. Compacta y portatil para llevar en camping, viajes y exteriores. Sin quimicos. Segura para ninos y mascotas. Bateria de larga duracion.",
    },
    {
        "match": ["LAMPARA DE MOSQUITOS", "LAMPARA PARA MOSQUITOS"],
        "precio": Decimal("38000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_712341-MCO74893048291_022024-O.webp",
        "descripcion_corta": "Lampara trampa UV para mosquitos, sin quimicos ni olores.",
        "descripcion": "Lampara atrayente de mosquitos con luz UV de alta eficiencia que atrae y elimina insectos sin quimicos ni olores. Silenciosa y de bajo consumo energetico. Ideal para dormitorios, salas y terrazas. Rejilla de seguridad protectora. Bandeja de captura de facil limpieza. Enchufe directo a corriente.",
    },
    {
        "match": ["RAQUETA DE MOSQUITOS"],
        "precio": Decimal("25000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_615892-MCO74893371648_022024-O.webp",
        "descripcion_corta": "Raqueta electrica antimosquitos recargable via USB.",
        "descripcion": "Raqueta electrica antimosquitos con red de triple capa de alta tension para eliminar mosquitos, moscas y otros insectos voladores. Recargable via USB con bateria de larga duracion. Mango ergonomico antideslizante. Rejilla de seguridad protectora. Sin quimicos. Ideal para interiores y exteriores.",
    },

    # ===== TERMOS =====
    {
        "match": ["TERMOS CHINOS", "TERMOS NARANJA", "TERMOS"],
        "precio": Decimal("35000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_946213-MCO74716591828_022024-O.webp",
        "descripcion_corta": "Termo de acero inoxidable con doble pared, mantiene temperatura 12h.",
        "descripcion": "Termo de acero inoxidable con doble pared al vacio para mantener la temperatura de bebidas calientes hasta 12 horas y frias hasta 24 horas. Tapa hermetica a prueba de derrames. Boca ancha para facil llenado y limpieza. Compacto y ligero. Libre de BPA. Ideal para oficina, viajes y deporte.",
    },
    {
        "match": ["TERMO AZUL"],
        "precio": Decimal("38000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_946213-MCO74716591828_022024-O.webp",
        "descripcion_corta": "Termo azul de acero inoxidable 500ml con tapa antifugas.",
        "descripcion": "Termo de acero inoxidable en color azul con capacidad de 500ml y doble pared al vacio. Mantiene bebidas calientes hasta 12 horas y frias hasta 24 horas. Tapa de rosca con junta hermetica antifugas. Apto para lavavajillas. Ligero y resistente. Sin BPA.",
    },
    {
        "match": ["FUN"],
        "precio": Decimal("42000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_946213-MCO74716591828_022024-O.webp",
        "descripcion_corta": "Termo compacto Fun con diseno moderno y tapa ergonomica.",
        "descripcion": "Termo Fun con diseno moderno y colorido. Doble pared de acero inoxidable para mantener la temperatura de bebidas calientes y frias por horas. Tapa de rosca ergonomica con junta de silicona. Capacidad 400ml. Libre de BPA. Facil de limpiar. Ideal para el dia a dia.",
    },
    {
        "match": ["STANLY"],
        "precio": Decimal("75000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_946213-MCO74716591828_022024-O.webp",
        "descripcion_corta": "Termo tipo Stanley de alta durabilidad para uso outdoor y aventura.",
        "descripcion": "Termo de alta durabilidad estilo Stanley con capacidad de 1 litro. Triple pared de acero inoxidable con aislamiento al vacio para mantener la temperatura hasta 24 horas en bebidas calientes y 48 horas en bebidas frias. Tapa con vaso integrado. Resistente a golpes. Ideal para senderismo, camping y trabajo.",
    },

    # ===== LICUADORA =====
    {
        "match": ["LICUADORA TERMO CON TAPA"],
        "precio": Decimal("65000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_879143-MCO74717393492_022024-O.webp",
        "descripcion_corta": "Licuadora portatil con vaso termico, tapa de seguridad y USB.",
        "descripcion": "Licuadora portatil con vaso termico que conserva la temperatura de tus batidos y jugos. Carga via USB tipo C. Motor de alta potencia con 6 cuchillas de acero inoxidable. Vaso de capacidad 400ml fabricado en plastico libre de BPA. Tapa hermetica con asegurador. Perfecta para gym, oficina y viajes.",
    },
    {
        "match": ["LICUADORA TERMO"],
        "precio": Decimal("58000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_879143-MCO74717393492_022024-O.webp",
        "descripcion_corta": "Licuadora portatil recargable USB con vaso termico 400ml.",
        "descripcion": "Licuadora portatil con vaso termico de 400ml. Recargable via USB con bateria de 2000mAh. Motor de alta potencia con cuchillas de acero inoxidable para frutas duras. Doble pared que conserva la temperatura. Facil de limpiar. Ideal para preparar batidos, jugos y smoothies en cualquier lugar.",
    },
    {
        "match": ["VASO LICUADORA"],
        "precio": Decimal("28000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_879143-MCO74717393492_022024-O.webp",
        "descripcion_corta": "Vaso extra de repuesto para licuadora portatil, 400ml libre BPA.",
        "descripcion": "Vaso de repuesto para licuadora portatil con capacidad de 400ml. Fabricado en plastico libre de BPA de alta resistencia. Compatible con la mayoria de licuadoras portatiles del mercado. Tapa hermetica incluida. Facil de limpiar. Transparente para visualizar el contenido.",
    },

    # ===== PICATODO =====
    {
        "match": ["PICATODO CAJA VERDE"],
        "precio": Decimal("42000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_853261-MCO74719158937_022024-O.webp",
        "descripcion_corta": "Picatodo electrico en caja verde, pica verduras en segundos.",
        "descripcion": "Picatodo electrico con presentacion en caja verde. Motor de alta potencia para picar, triturar y procesar cebollas, ajos, hierbas y vegetales en segundos. Cuchillas de acero inoxidable. Vaso transparente con tapa hermetica. Facil de limpiar. Ideal para agilizar la preparacion de comidas.",
    },
    {
        "match": ["PICATODO BLANCO"],
        "precio": Decimal("38000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_853261-MCO74719158937_022024-O.webp",
        "descripcion_corta": "Picatodo electrico blanco compacto, ideal para cocinas pequenas.",
        "descripcion": "Picatodo electrico blanco de diseno compacto y funcional. Motor silencioso de alta eficiencia. Cuchillas de acero inoxidable para picar cebolla, ajo, pimentones y mas. Cuenco de 500ml con tapa hermetica. Facil desarmado para limpieza. Bajo consumo de energia.",
    },
    {
        "match": ["PICATODO ROSADO"],
        "precio": Decimal("38000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_853261-MCO74719158937_022024-O.webp",
        "descripcion_corta": "Picatodo electrico rosado, divertido y practico para la cocina.",
        "descripcion": "Picatodo electrico rosado con diseno moderno y colorido. Motor de alta velocidad con cuchillas de acero inoxidable afiladas. Ideal para picar vegetales, frutas secas y hierbas aromaticas. Cuenco con tapa hermetica. Facil de limpiar en el lavavajillas. Compacto y eficiente.",
    },
    {
        "match": ["PICATODO DOBLE"],
        "precio": Decimal("52000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_853261-MCO74719158937_022024-O.webp",
        "descripcion_corta": "Picatodo doble con dos vasos independientes para mayor capacidad.",
        "descripcion": "Picatodo doble con dos vasos independientes que permite procesar distintos ingredientes por separado. Motor potente compartido. Cuchillas de acero inoxidable de alta durabilidad. Tapa hermetica en ambos vasos. Perfecto para preparaciones que requieren separar ingredientes. Facil de limpiar.",
    },
    {
        "match": ["MANUAL"],
        "precio": Decimal("28000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_853261-MCO74719158937_022024-O.webp",
        "descripcion_corta": "Picatodo manual sin electricidad, compacto y de alta durabilidad.",
        "descripcion": "Picatodo manual que funciona sin electricidad mediante mecanismo de palanca o tirador. Cuchillas de acero inoxidable de alta durabilidad. Cuenco de vidrio templado resistente. Ideal para cebollas, ajos, nueces y hierbas. Facil de limpiar y almacenar. Silencioso y ecologico.",
    },
    {
        "match": ["BATIDORA Y PICATODO"],
        "precio": Decimal("65000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_853261-MCO74719158937_022024-O.webp",
        "descripcion_corta": "Set batidora y picatodo electrico 2 en 1 para cocina completa.",
        "descripcion": "Set 2 en 1 que combina batidora de mano y picatodo electrico en un mismo motor potente. Incluye varillas batidoras y vaso picatodo con cuchillas de acero. Motor de alta potencia con velocidades variables. Ideal para batir huevos, cremas, salsas y picar ingredientes. Facil de limpiar.",
    },

    # ===== RALLADOR =====
    {
        "match": ["RALLADOR VERDE"],
        "precio": Decimal("18000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_915647-MCO74893618291_022024-O.webp",
        "descripcion_corta": "Rallador de cocina verde multiusos con mango ergonomico.",
        "descripcion": "Rallador de cocina en color verde con multiple superficie de rallado: grueso, fino, en juliana y rallado plano. Acero inoxidable de alta calidad. Mango ergonomico antideslizante. Base antideslizante para mayor seguridad. Facil de limpiar. Ideal para quesos, zanahorias, papa y mas.",
    },
    {
        "match": ["RALLADOR NUEVO"],
        "precio": Decimal("20000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_915647-MCO74893618291_022024-O.webp",
        "descripcion_corta": "Rallador multiuso de acero inoxidable con 4 superficies de corte.",
        "descripcion": "Rallador de cocina multiuso con 4 superficies de rallado intercambiables: extra fino, fino, mediano y grueso. Cuchillas de acero inoxidable de alta durabilidad. Mango de plastico resistente. Deposito recolector incluido. Facil limpieza bajo el grifo o en lavavajillas.",
    },
    {
        "match": ["RALLADOE TRANSPARENTE"],
        "precio": Decimal("18000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_915647-MCO74893618291_022024-O.webp",
        "descripcion_corta": "Rallador transparente con recipiente recolector integrado.",
        "descripcion": "Rallador con cuenco recolector transparente integrado para ver la cantidad rallada mientras trabajas. Superficie de rallado de acero inoxidable. Base con ventosa antideslizante. Cuenco medidor con escala. Facil de desmontar y lavar. Compacto y practico para uso diario.",
    },
    {
        "match": ["RALLADOR PLANO"],
        "precio": Decimal("15000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_915647-MCO74893618291_022024-O.webp",
        "descripcion_corta": "Rallador plano de acero inoxidable con agarre comodo.",
        "descripcion": "Rallador plano de acero inoxidable de alta calidad con superficie de rallado fino ideal para quesos duros, chocolate, limon y nuez moscada. Mango de madera o plastico ergonomico. Resistente y de larga duracion. Facil de limpiar en lavavajillas.",
    },
    {
        "match": ["RALLADOR REDONDO"],
        "precio": Decimal("17000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_915647-MCO74893618291_022024-O.webp",
        "descripcion_corta": "Rallador redondo rotativo para queso y vegetales con manivela.",
        "descripcion": "Rallador redondo rotativo con manivela para rallar queso parmesano, pan, nueces y vegetales con facilidad. Cuchilla intercambiable de acero inoxidable. Cuenco recolector incluido. Facil de usar con una sola mano. Limpieza sencilla. Ideal para postres y gratinados.",
    },
    {
        "match": ["RALLADOR CUADRADO"],
        "precio": Decimal("16000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_915647-MCO74893618291_022024-O.webp",
        "descripcion_corta": "Rallador cuadrado de cuatro caras con multiple granulometria.",
        "descripcion": "Rallador cuadrado de cuatro caras con distintas superficies: rallado grueso, fino, cortado en juliana y laminado. Acero inoxidable de alta resistencia. Base antideslizante. Mango plastico ergonomico. Versatil para queso, verduras, chocolate y mas. Facil de limpiar.",
    },

    # ===== MACHACADOR =====
    {
        "match": ["MACHACADOR NEGRO Y BLANCO"],
        "precio": Decimal("20000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_967213-MCO74893247917_022024-O.webp",
        "descripcion_corta": "Machacador bicolor negro y blanco con base antideslizante.",
        "descripcion": "Machacador manual en colores negro y blanco con cabezal de acero inoxidable y mango ergonomico. Base antideslizante para mayor seguridad. Ideal para machacar especias, semillas, legumbres, ajo y mas. Facil de limpiar. Resistente y de larga duracion. Diseno moderno para la cocina.",
    },
    {
        "match": ["MACHACADOR GRIS"],
        "precio": Decimal("20000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_967213-MCO74893247917_022024-O.webp",
        "descripcion_corta": "Machacador gris resistente para especias y alimentos.",
        "descripcion": "Machacador manual en color gris fabricado en material resistente con cabezal metalico de alta durabilidad. Mango ergonomico de agarre comodo y firme. Ideal para triturar ajos, especias, nueces, pimientas y cereales. Base antideslizante. Facil de lavar.",
    },
    {
        "match": ["MACHACADOR BLANCO"],
        "precio": Decimal("20000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_967213-MCO74893247917_022024-O.webp",
        "descripcion_corta": "Machacador blanco clasico con cabezal inoxidable para cocina.",
        "descripcion": "Machacador manual en color blanco con cabezal de acero inoxidable y mango de plastico resistente. Diseno clasico y funcional para la cocina. Ideal para machacar papas, alubias, especias y frutas. Base plana antideslizante. Apto para lavavajillas. Resistente y duradero.",
    },

    # ===== RECIPIENTE PLASTICO =====
    {
        "match": ["RECIPIENTE PLASTICO REDONDO"],
        "precio": Decimal("15000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_838917-MCO74893524827_022024-O.webp",
        "descripcion_corta": "Recipiente plastico redondo hermetico para alimentos, libre BPA.",
        "descripcion": "Recipiente de plastico redondo con tapa hermetica de cierre seguro. Libre de BPA, apto para alimentos. Transparente para ver el contenido. Apto para microondas y lavavajillas. Facil de apilar para ahorrar espacio. Ideal para guardar sobras, frutas, verduras y alimentos secos.",
    },
    {
        "match": ["RECIPIENTE PLASTICO CUADRADO PEQUENO"],
        "precio": Decimal("13000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_838917-MCO74893524827_022024-O.webp",
        "descripcion_corta": "Recipiente cuadrado pequeno hermetico para alimentos portables.",
        "descripcion": "Recipiente plastico cuadrado pequeno con tapa hermetica de cuatro clips de seguridad. Fabricado en plastico libre de BPA de alta resistencia. Apto para microondas, congelador y lavavajillas. Transparente. Ideal para llevar meriendas, frutas y snacks al trabajo o colegio.",
    },
    {
        "match": ["RECIPIENTE PLASTICO CUADRADO GRANDE"],
        "precio": Decimal("18000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_838917-MCO74893524827_022024-O.webp",
        "descripcion_corta": "Recipiente cuadrado grande hermetico para almacenamiento de alimentos.",
        "descripcion": "Recipiente plastico cuadrado de gran capacidad con tapa hermetica. Libre de BPA, apto para alimentos. Tapa con cierre de cuatro clips para total estanqueidad. Apilable para aprovechar el espacio en nevera y despensa. Apto para microondas y lavavajillas.",
    },

    # ===== COCINA =====
    {
        "match": ["CORTADOR DE PAPA FRANCESA"],
        "precio": Decimal("35000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_623781-MCO74893271928_022024-O.webp",
        "descripcion_corta": "Cortador de papa francesa en tiras uniformes, acero inoxidable.",
        "descripcion": "Cortador de papa francesa que produce tiras perfectas y uniformes en un solo movimiento. Cuchillas de acero inoxidable de alta durabilidad. Base con ventosas antideslizantes para mayor seguridad. Rejilla de corte intercambiable para distintos tamanos de tira. Facil de limpiar en lavavajillas.",
    },
    {
        "match": ["SET DE CUCHARAS"],
        "precio": Decimal("22000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_623781-MCO74893271928_022024-O.webp",
        "descripcion_corta": "Set de cucharas medidoras de acero inoxidable para reposteria.",
        "descripcion": "Set de cucharas medidoras de acero inoxidable de alta calidad para precision en recetas de cocina y reposteria. Incluye 8 tamanos desde 1/8 de cucharadita hasta 1 cuchara grande. Grabado en relieve con las medidas. Anilla de union para mantenerlas organizadas. Aptas para lavavajillas.",
    },
    {
        "match": ["SANDWICHERA"],
        "precio": Decimal("68000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_657891-MCO74893583721_022024-O.webp",
        "descripcion_corta": "Sandwichera electrica antiadherente con calentamiento rapido.",
        "descripcion": "Sandwichera electrica con planchas antiadherentes de ceramica para preparar sandwiches, tostadas y wraps en minutos. Calentamiento rapido en menos de 2 minutos. Luz indicadora de temperatura. Cierre de seguridad. Bordes que sellan los sandwiches. Facil limpieza de las planchas.",
    },
    {
        "match": ["SET TARROS ORGANIZADORES X5"],
        "precio": Decimal("45000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_938127-MCO74893319472_022024-O.webp",
        "descripcion_corta": "Set de 5 tarros hermeticos para organizar despensa y cocina.",
        "descripcion": "Set de 5 tarros hermeticos con tapa transparente para ver el contenido. Fabricados en plastico libre de BPA de alta resistencia. Apilables para aprovechar el espacio. Sellos hermeticos para conservar alimentos frescos por mas tiempo. Ideales para cereales, arroz, azucar, cafe y legumbres.",
    },
    {
        "match": ["SET DE TARROS X7"],
        "precio": Decimal("58000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_938127-MCO74893319472_022024-O.webp",
        "descripcion_corta": "Set de 7 tarros hermeticos de diferentes tamanos para cocina.",
        "descripcion": "Set de 7 tarros hermeticos en diferentes tamanos para una organizacion completa de la despensa. Tapa con sello hermetico de silicona. Plastico libre de BPA, transparente para ver el contenido. Apilables. Incluye tamanos para especias, cereales, harinas y snacks.",
    },
    {
        "match": ["FUENTE DE CHOCOLATE"],
        "precio": Decimal("72000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_675341-MCO74893502847_022024-O.webp",
        "descripcion_corta": "Fuente de chocolate electrica de 3 niveles para fondue y eventos.",
        "descripcion": "Fuente de chocolate electrica de 3 niveles en acero inoxidable. Motor silencioso para flujo continuo de chocolate fundido. Incluye fondue de acero inoxidable. Mantiene el chocolate a temperatura constante. Ideal para fiestas, eventos y celebraciones. Capacidad de 500g de chocolate. Facil de limpiar.",
    },
    {
        "match": ["MAQUINA TRITURADORA DE HIELO"],
        "precio": Decimal("65000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_675341-MCO74893502847_022024-O.webp",
        "descripcion_corta": "Trituradora de hielo electrica para cocteleria y bebidas frias.",
        "descripcion": "Maquina trituradora de hielo electrica de alta potencia para preparar bebidas frias, cocteles y granizados. Cuchillas de acero inoxidable de alta durabilidad. Cubierta protectora de seguridad. Deposito recolector de gran capacidad. Facil de limpiar y almacenar. Silenciosa y eficiente.",
    },
    {
        "match": ["GRAMERA DIGITAL"],
        "precio": Decimal("32000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_647891-MCO74893417293_022024-O.webp",
        "descripcion_corta": "Gramera digital de precision para cocina, hasta 5kg.",
        "descripcion": "Bascula digital de cocina de alta precision con sensores de pesaje de ultima generacion. Capacidad de hasta 5kg con precision de 1 gramo. Pantalla LCD retroiluminada. Funcion tara para restar el peso del recipiente. Unidades de medida multiples. Facil limpieza de plataforma. Pilas incluidas.",
    },
    {
        "match": ["GRAMERA"],
        "precio": Decimal("25000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_647891-MCO74893417293_022024-O.webp",
        "descripcion_corta": "Gramera de cocina compacta para medir ingredientes con precision.",
        "descripcion": "Bascula de cocina compacta con pantalla digital. Precision de pesaje de 1 gramo con capacidad de hasta 3kg. Funcion tara. Unidades convertibles entre gramos, onzas y libras. Diseno plano de facil limpieza. Pilas incluidas. Ideal para reposteria y dietas.",
    },
    {
        "match": ["CEREAL X3"],
        "precio": Decimal("38000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_938127-MCO74893319472_022024-O.webp",
        "descripcion_corta": "Set de 3 dispensadores hermeticos para cereales y snacks.",
        "descripcion": "Set de 3 dispensadores hermeticos para cereales, granolas, snacks y alimentos secos. Tapa de presion con sello hermetico de silicona que conserva los alimentos frescos y crujientes. Cuerpo transparente para ver el contenido. Apilables. Libres de BPA. Facilitan la organizacion de la despensa.",
    },
    {
        "match": ["CEREAL X2"],
        "precio": Decimal("28000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_938127-MCO74893319472_022024-O.webp",
        "descripcion_corta": "Set de 2 dispensadores hermeticos para cereales y granos.",
        "descripcion": "Set de 2 dispensadores hermeticos para cereales, granos y alimentos secos. Cuerpo de plastico transparente libre de BPA. Tapa hermetica con sello de silicona. Apilables para maximizar el espacio en la despensa. Facil de limpiar. Mantienen los alimentos frescos por mas tiempo.",
    },
    {
        "match": ["TARROS X12"],
        "precio": Decimal("55000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_938127-MCO74893319472_022024-O.webp",
        "descripcion_corta": "Set de 12 tarros hermeticos para especias y condimentos.",
        "descripcion": "Set de 12 tarros hermeticos de tamano ideal para especias, condimentos, hierbas y otros ingredientes de cocina. Tapa con sello hermetico. Etiquetas incluidas para identificar el contenido. Apilables y organizables en estante o cajon. Libres de BPA. Facil de limpiar.",
    },
    {
        "match": ["TARROS X18"],
        "precio": Decimal("72000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_938127-MCO74893319472_022024-O.webp",
        "descripcion_corta": "Set de 18 tarros hermeticos para organizacion completa de cocina.",
        "descripcion": "Set de 18 tarros hermeticos en diferentes tamanos para organizar completamente la despensa y los condimentos de la cocina. Incluye etiquetas y rotulador. Tapa con sello hermetico de silicona. Libres de BPA. Apilables. Transparentes para ver el contenido. Facil de limpiar.",
    },
    {
        "match": ["PORTA TRAPOS"],
        "precio": Decimal("18000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_623781-MCO74893271928_022024-O.webp",
        "descripcion_corta": "Soporte organizador de trapos y bolsas para cocina.",
        "descripcion": "Soporte organizador de trapos de cocina y bolsas plasticas para mantener la cocina ordenada. Fabricado en acero inoxidable o plastico resistente. Incluye tornillos y taco para instalacion en pared o puerta. Compacto y de diseno minimalista. Facil de limpiar.",
    },
    {
        "match": ["GRIFO DE AGUA"],
        "precio": Decimal("38000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_623781-MCO74893271928_022024-O.webp",
        "descripcion_corta": "Grifo dosificador electrico para garrafon de agua recargable.",
        "descripcion": "Grifo dosificador electrico para garrafones de 20 litros. Motor silencioso y eficiente con bomba de succion. Recargable via USB. Boquilla flexible de silicon. Adaptable a la mayoria de garrafones estandar. Dispensado preciso sin derrames. Ideal para casa y oficina.",
    },
    {
        "match": ["FILTRO DE AGUA"],
        "precio": Decimal("45000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_623781-MCO74893271928_022024-O.webp",
        "descripcion_corta": "Filtro purificador de agua con carbon activado para grifo.",
        "descripcion": "Filtro purificador de agua de instalacion rapida en el grifo con carbon activado y membrana de filtracion. Elimina cloro, sedimentos, metales pesados y olores del agua del grifo. Vida util de 6 meses o 3000 litros. Facil instalacion sin herramientas. Certificado para uso alimentario.",
    },
    {
        "match": ["ESCURRIDOR CON CAJON"],
        "precio": Decimal("42000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_623781-MCO74893271928_022024-O.webp",
        "descripcion_corta": "Escurridor de platos con cajon recolector de agua integrado.",
        "descripcion": "Escurridor de platos con cajon recolector de agua integrado para mantener la mesada seca y limpia. Fabricado en acero inoxidable y plastico resistente. Gran capacidad para platos, vasos, cubiertos y ollas pequenas. Cajon extraible de facil vaciado. Portacubiertos incluido.",
    },
    {
        "match": ["ESCURRIDOR"],
        "precio": Decimal("35000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_623781-MCO74893271928_022024-O.webp",
        "descripcion_corta": "Escurridor de platos acero inoxidable con portacubiertos.",
        "descripcion": "Escurridor de platos en acero inoxidable resistente a la corrosion con portacubiertos integrado. Diseno compacto de dos niveles para optimizar el espacio. Bandeja de goteo con desague. Facil de limpiar. Capacidad para 8 platos, vasos y cubiertos. Ideal para cocinas de todos los tamanos.",
    },

    # ===== MASCOTAS =====
    {
        "match": ["BEBEDERO DE MASCOTAS AMARILLO"],
        "precio": Decimal("52000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_894231-MCO74719298737_022024-O.webp",
        "descripcion_corta": "Bebedero automatico amarillo para mascotas con filtro y circulacion.",
        "descripcion": "Bebedero automatico para mascotas en color amarillo con sistema de circulacion de agua y filtro de carbon activado para mantener el agua fresca y limpia. Capacidad de 2 litros. Motor silencioso. Indicador de nivel de agua. Facil de limpiar en lavavajillas. Ideal para perros y gatos.",
    },
    {
        "match": ["BEBEDERO DE MASCOTAS VERDE"],
        "precio": Decimal("52000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_894231-MCO74719298737_022024-O.webp",
        "descripcion_corta": "Bebedero automatico verde para mascotas con filtro purificador.",
        "descripcion": "Bebedero automatico para mascotas en color verde con sistema de filtrado continuo para mantener el agua fresca, limpia y oxigenada. Capacidad 2 litros. Motor silencioso de bajo consumo. Fuente de cascada para estimular a las mascotas a beber mas agua. Apto para lavavajillas.",
    },
    {
        "match": ["TAZA LIMPIADORA DE MASCOTAS"],
        "precio": Decimal("28000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_648923-MCO74893467293_022024-O.webp",
        "descripcion_corta": "Taza limpiadora de patas de mascotas con cerdas suaves.",
        "descripcion": "Taza limpiadora de patas de mascotas con cerdas de silicona suaves que limpian eficientemente el barro y la suciedad entre los dedos. Solo agregar agua, introducir la pata y girar. Sin necesidad de bano completo. Apta para perros y gatos de todos los tamanos. Facil de limpiar.",
    },
    {
        "match": ["MALETINES PARA MASCOTAS"],
        "precio": Decimal("65000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_813247-MCO74893492817_022024-O.webp",
        "descripcion_corta": "Maletin transportador ventilado y comodo para mascotas pequenas.",
        "descripcion": "Maletin transportador para mascotas pequenas con ventilacion en todos los lados. Cuerpo rigido de alta resistencia con puerta de malla. Interior acolchado y lavable. Hebillas de seguridad. Talla adecuada para gatos y perros hasta 6kg. Aprobado para transporte en avion como equipaje de mano.",
    },
    {
        "match": ["CEPILLO PARA MASCOTAS"],
        "precio": Decimal("25000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_648923-MCO74893467293_022024-O.webp",
        "descripcion_corta": "Cepillo quitapelo para mascotas con puas de acero inoxidable.",
        "descripcion": "Cepillo para mascotas con puas de acero inoxidable curvadas para remover eficientemente el pelo suelto, nudos y pelo muerto de perros y gatos. Boton de autolimpieza para retirar el pelo del cepillo facilmente. Mango ergonomico antideslizante. Ideal para pelo corto, mediano y largo.",
    },
    {
        "match": ["CEPILLO VAPOR"],
        "precio": Decimal("58000"),
        "imagen_url": "https://http2.mlstatic.com/D_NQ_NP_648923-MCO74893467293_022024-O.webp",
        "descripcion_corta": "Cepillo de vapor para limpiar y desinfectar superficies sin quimicos.",
        "descripcion": "Cepillo de vapor multifuncion para limpieza y desinfeccion profunda de superficies del hogar sin uso de quimicos. Vapor a alta temperatura que elimina el 99.9% de bacterias y germenes. Incluye multiples cabezales para distintas superficies: pisos, juntas, tapiceria y mas. Deposito de agua de 300ml.",
    },
]


def match_producto(nombre: str, patrones: list) -> bool:
    """True si el nombre del producto contiene alguno de los patrones (insensible a mayusculas)."""
    nombre_up = nombre.upper()
    return any(p.upper() in nombre_up for p in patrones)


class Command(BaseCommand):
    help = 'Actualiza precios, imagenes y descripciones de los productos con datos de mercado'

    def add_arguments(self, parser):
        parser.add_argument(
            '--preview',
            action='store_true',
            help='Muestra los cambios sin aplicarlos',
        )

    def handle(self, *args, **options):
        preview = options['preview']
        productos = Producto.objects.all()
        actualizados = 0
        sin_match = []

        for producto in productos:
            matched = False
            for datos in DATOS_PRODUCTOS:
                if match_producto(producto.nombre, datos['match']):
                    if preview:
                        self.stdout.write(
                            f"[PREVIEW] {producto.nombre}\n"
                            f"  precio: {datos['precio']}\n"
                            f"  imagen: {datos['imagen_url'][:60]}...\n"
                        )
                    else:
                        producto.precio = datos['precio']
                        producto.imagen_url = datos['imagen_url']
                        producto.descripcion_corta = datos['descripcion_corta']
                        producto.descripcion = datos['descripcion']
                        producto.save(update_fields=['precio', 'imagen_url', 'descripcion_corta', 'descripcion'])
                    actualizados += 1
                    matched = True
                    break

            if not matched:
                sin_match.append(producto.nombre)

        if not preview:
            self.stdout.write(self.style.SUCCESS(f'\nProductos actualizados: {actualizados}'))
        if sin_match:
            self.stdout.write(self.style.WARNING(f'\nSin coincidencia ({len(sin_match)}):'))
            for n in sin_match:
                self.stdout.write(f'  - {n}')
