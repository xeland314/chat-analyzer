# chat-anaylzer

Analiza la frecuencia de uso de emojis y palabras de un chat exportado de whatsapp.

## Requerimientos e instalación

- Versión de python: *3.9.2*

Las librerías necesarias para el uso de este programa son:

- emoji==2.2.0
- nltk==3.8
- rich==13.3.1
- typer==0.7.0
- wordcloud==1.8.2.2

Se puede clonar este repositorio:

```bash
git clone https://github.com/xeland314/chat-anaylzer.git && cd chat-analyzer
```

Luego se instalan las librerías faltantes:

```bash
pip3 install -r requirements.txt
```

El primer comando antes de analizar cualquier chat es:

```bash
python3 chat_analyzer.py --install
```

o

```bash
python3 chat_analyzer.py -i
```

Esto descargará:

```python
import nltk
nltk.download("punkt")      # Separa el texto en palabras y signos de puntuación
nltk.download("stopwords")  # Palabras más comunes para filtrar del texto original
nltk.download("wordnet")    # Lemmatizer
nltk.download("vader_lexicon") # SentimentAnalyzer
```

## Uso

Una vez se ha clonado el repositorio, se puede usar la línea de comandos de la siguiente manera:

```bash
python3 chat_analyzer.py chat.txt
```

Se pasa como argumento el nombre del archivo que se desea analizar.
El resultado se imprimirá por consola.

También se puede definir el número de emojis y palabras más comunes para mostrar en el resumen:

```bash
python3 chat_analyzer.py chat.txt -w50 -e20
```

```bash
python3 chat_analyzer.py chat.txt --words 50 --emojis 20
```

Los valores por defecto, son 30 palabras y 15 emojis por mostrar en el resumen.

### El chat lo puedes exportar desde tu celular

1. Ir a Ajustes > Chats > Historial de Chats > Exportar Chat.
2. Después, se desplegará una lista de todas las conversaciones, selecciona el que quieras analizar.
3. Al seleccionar el chat que quieras exportar, debes seleccionar la opción de exportar solo texto. Es decir **sin incluir archivos**.
4. Lo copias a tu PC, dentro de la carpeta del repositorio.
5. Finalmente, ya puedes analizar tu chat.

## Resultados

Por consola se imprimirán los siguientes resultados:

- Tabla de palabras más utilizadas por persona en el chat.
- Tabla de emojis más usados por persona en el chat.

También se generará:

- Una nube de palabras (*wordcloud*) de las palabras más usadas.

## Tiempo de ejecución

**¡Debes esperar de 1 a 3 minutos!**

Luego de algunas pruebas se han obtenido los siguientes resultados:

<div id="results" align="center">
    <img width="484" height="371" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vQYzl7jxgLN9QGN4yvFYRzU5dMv3WMyJGhbeXYiEHwwtxUKDudXUINhxq3fhXmzv1JbmTVGImI07r0e/pubchart?oid=1886909932&amp;format=image"></img>
</div>

Estas pruebas se realizaron con un procesador de dos núcleos.
Puede que con una computadora con mejores prestaciones los tiempos se reduzcan.
