# chat-anaylzer

Analiza la frecuencia de uso de emojis y palabras de un chat exportado de whatsapp.

## Requerimientos e instalación

- Versión de python: *3.9.2*

Las librerías necesarias para el uso de este programa son:

- emoji==2.2.0
- nltk==3.8
- rich==13.0.0
- typer==0.7.0

Se puede clonar este repositorio:

```bash
git clone https://github.com/xeland314/chat-anaylzer.git
```

Luego se instalan las librerías faltantes:

```bash
pip3 install -r requirements.txt
```

## Uso

Una vez se ha clonado el repositorio, se puede usar la línea de comandos de la siguiente manera:

```bash
python3 main.py --file chat.txt
```

o

```bash
python3 main.py -f chat.txt
```

El resultado se imprimirá por consola.

### El chat lo puedes exportar desde tu celular

1. Ir a Ajustes > Chats > Historial de Chats > Exportar Chat.
2. Después, se desplegará una lista de todas las conversaciones, selecciona el que quieras analizar.
3. Al seleccionar el chat que quieras exportar, debes seleccionar la opción de exportar solo texto. Es decir **sin incluir archivos**.
4. Lo copias a tu PC, dentro de la carpeta del repositorio.
5. Finalmente, ya puedes analizar tu chat.

## Resultados

Por consola se imprimirán varias tablas que indican las palabras y emojis más utilizados en el chat por cada persona del chat.
