# Proyecto Cripto
Este proyecto consiste en una serie de tres trabajos incrementales y relacionados con la Criptografía realizados dentro de la formación post-universitaria.

## Requerimientos del proyecto
El proyecto está realizado en Python v3 (no está adaptado para funcionar con Python v2). Emplea los módulos tkinter para implementar interfaces gráficas Tcl/Tk y datetime para realizar cálculos de tiempos.

## Versiones del proyecto
1. Aplicación cifrado simétrico DES-simplificado. (v1.0.0)
2. Aplicación cifrado de bloques CBC. (v2.0.0)
3. Aplicación función hash. (v3.0.0)

## Contenido de versiones
### v1.0.0:
Se trata de una aplicación que implementa un algoritmo de tipo DES simplificado y un algoritmo de fuerza bruta que prueba la debilidad de DES.

Características algoritmo DES-simplificado:

- Número de iteraciones = 8
- Tamaño en bits del bloque = 12
- Tamaño en bits de la clave = 9

### v2.0.0:
En la siguiente versión se ha modificado la implementación del algoritmo de cifrado  un modo de operación de cifrado por bloques: modo CBC. De nuevo, implementamos un procedimiento de fuerza bruta que prueba la fortaleza del cifrado.


*Nota*: En esta versión, se ha mejorado la interfaz de usuario con un diseño más actual.

### v3.0.0:
Para finalizar el proyecto, se ha realizado la implementación de una función hash y unos indicadores para conocer las variaciones que se producen al modificar el valor al que se aplica dicha función.

*Nota*: En esta versión, se ha añadido un tema oscuro que ahora puede ser modificado desde Tema > Cambiar Tema (alternará entre oscuro y claro).


<!--
#Cabeceras
---

## Cabecera H2
### Cabecera H3
#### Cabecera H4
##### Cabecera H5
###### Cabecera H6

#Underlines
---
Underline 1
---
Underline 2
===

#Formatos
---
formato *italica* primera forma
formato _italica_ segunda forma
formato **negrita** primera forma
formato __negrita__ segunda forma
formato ~~tachado~~  primera forma
formato primera forma

## Listas
---

1. a
2. b
3. c

- a
- b
- c

#Links
---

[This is a link](https://www.google.es)


# Imagenes
---
--![Logo github](https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png)

# Code Snippets
```C++
int a = 4;
int b = 5;

cout << "A + B = " << a+b;
```

```Javascript
function $initHighlight(block, cls) {
  try {
    if (cls.search(/\bno\-highlight\b/) != -1)
      return process(block, true, 0x0F) +
             ` class="${cls}"`;
  } catch (e) {
    /* handle exception */
  }
  for (var i = 0 / 2; i < classes.length; i++) {
    if (checkCondition(classes[i]) === undefined)
      console.log('undefined');
  }

  return (
    <div>
      <web-component>{block}</web-component>
    </div>
  )
}
export  $initHighlight;
```

# Tablas
---

| Nombre | Apellido | Documento | Edad |
|-|-|-|-|
|10|2|4|5|
|x|y|z|d|

# Citas

>Para crecer hay que *desaprender*; quitarse esas cosas que son inútiles
peligrosas o inconsistentes con nuestro objetivo final de realización. 
> 
> ***-Walter Riso***

# Líneas divisorias

Esto es un texto que será dividido por ---

---

Esto es otro texto dividido ***

***

Esto es otro texto dividido por ___

___

# Saltos de línea

Esto es nuestro primer párrafo.
Esto es nuestro segundo párrafo.

Esto es nuestro tercer párrafo.
-->


