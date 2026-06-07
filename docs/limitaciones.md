# limitaciones de escuadra - version inicial (v1)

.a continuacion se detallan las limitaciones conocidas y esperadas de escuadra en su versio inicial o planes futuros.

## 1\. falta de integracion con herramientas de diseño garfico

**descripcion:** en esta version no se incluye soporte para importar ni exportar archivos de herramientas como adobe illustrator, Figma o inkscape. no es posible trabajar directamente con estos fromatos.
**¿solucion temporal?**: si se debe exportar/convertir los archivos a formatos soportados (PNG, JPG, SVG simple) antes de usarlos en escuadra.
**¿`planeado en futuras versines?**:si se tiene previsto integrar soporte para estos fromatos en la version v1.2.

## 2\. no soprta sistemas operativos moviles

**descripcion:** la herramienta solo funciona en sistemas de escritorio: Windows, Linux, macOs. no es posible usarla en android ni iOS.
**¿solucion temporal?**: no, no existe forma de ejecutarlo en dispositivos moviles por ahora.
**¿planeado en futuras versiones?**: no, no esta en plan de corto/medio plazo, se priorizaran otra caracteristicas primero.

## 3\. no gestiona proyectos colaborativos simultaneos

**descripcion:** solo permite trabajar con un usuario a la vez en un mismo proyecto.
no hay edicion en yiempo real ni control de versiones compartido.
**¿solucion temporal?**: si, se pueden compartir archivos manualmente manualmente y fusionar cambios por fuera de la herramienta.
**¿planeado en futuras versiones?**: si, sedesarrollara esta funcionalidad para la version v2.0.

## 4\. sin soprte para bases de datos exteranas

**descripcion:** no se puede conectar ni leer/escribir infrmacion de bases de datos com MySQL, PostgreSQL, MongoDB. solo usa archvos locales.
**¿solucion temporal?**: no, no hay formas de conectarse a fuentes externas actuales.
**¿planeando en futuras versiones?**: si , se agregara conectividad basicas en la v1.5.



## 5\. limitaciones por modulo



5.1 modulo civil



descripcion: el modulo civil implementa un conjunto limitado de funcionalidades para el analisis estructural.



limitaciones conocidas:

\- solo soporta vigas simplemente apoyadas.

\- no soporta vigas continuas.

\- no soporta marcos estructurales complejos.

\- no realiza analisis sismico.

\- no contempla cargas dinamicas avanzadas.

\- los resultados deben considerarse aproximaciones para escenarios basicos.



5.2 modulo electrica



descripcion: el modulo electrica esta orientado a circuitos basicos de corriente continua.



limitaciones conocidas:

\- solo trabaja con corriente continua (DC).

\- no soporta corriente alterna (AC).

\- solo considera resistencias puras.

\- no soporta capacitores ni inductores.

\- no realiza analisis fasorial.

\- no contempla fenomenos avanzados de potencia electrica.



5.3 modulo matematicas



descripcion: el modulo matematicas utiliza la precision numerica estandar del lenguaje.



limitaciones conocidas:

\- no utiliza bibliotecas de alta precision numerica.

\- pueden existir errores de redondeo.

\- pueden existir errores de punto flotante.

\- operaciones repetidas pueden acumular pequeñas diferencias numericas.

\- algunos resultados pueden variar ligeramente dependiendo de la plataforma utilizada.



5.4 modulo geometria



descripcion: el modulo geometria se enfoca en operaciones geometricas basicas.



limitaciones conocidas:

\- solo soporta figuras regulares.

\- no soporta figuras irregulares complejas.

\- no incluye modelado tridimensional avanzado.

\- algunas formulas asumen condiciones ideales.

\- no contempla geometria computacional avanzada.



5.5 modulo sistemas



descripcion: el modulo sistemas implementa soporte limitado para manejo de caracteres.



limitaciones conocidas:

\- solo soporta caracteres ASCII del rango 0 al 127.

\- no soporta completamente Unicode.

\- caracteres especiales pueden producir resultados inesperados.

\- no existe soporte completo para alfabetos internacionales.

\- el procesamiento de texto avanzado no esta implementado.

