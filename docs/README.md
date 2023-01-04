# Funcionamiento de chat-analyzer

## Objetos de chat-analyzer

### Chat

La clase Chat es una clase que permite almacenar y manipular mensajes. Esta clase contiene los siguientes métodos:

- _append()_: Agrega un nuevo mensaje a la lista de mensajes.

- _get_last_message()_: Devuelve el último mensaje de la lista de mensajes.

- _update_last()_: Actualiza el último mensaje de la lista de mensajes.

### Message

Esta clase define un objeto de mensaje que contiene información sobre la fecha y hora, el autor y el contenido del mensaje. También proporciona algunas funciones para obtener los emojis y las palabras contenidas en el mensaje, así como para agregar más texto al mensaje.

### LexicalAnalyzer

Esta clase define un analizador léxico para reconocer patrones de mensajes en un chat.

Inicialmente, la clase contiene tres expresiones regulares para extraer información de los mensajes: author_pattern, date_pattern y message_pattern. Estas expresiones regulares se usan para extraer el autor, la fecha y el mensaje del texto.

La clase también contiene cuatro métodos: __init__ (), extract_author (), extract_datetime () y extract_message (). El método __init__ () inicializa un objeto Chat vacío. Los otros tres métodos se usan para extraer información de los mensajes.

El último método es process_file (), que se usa para procesar el archivo de entrada. Se abre el archivo y cada línea se procesa con los otros tres métodos. Si no hay autor o fecha, el texto se agrega al último mensaje existente en el objeto Chat. Finalmente, el objeto Chat se devuelve con get_chat ().

### WhatsappResult

Esta clase representa un objeto que contiene los resultados de un análisis de Whatsapp. El constructor recibe tres parámetros: authors (una cuenta de autores), emojis_by_person (una cuenta de emojis por persona) y words_by_person (una cuenta de palabras por persona).

El método _set_title() crea un panel con el título "Whatsapp Analyzer Results" y contiene información sobre el número de mensajes enviados por cada autor.

El método _set_emojis_panel() crea una tabla para cada autor que muestra los 10 emojis más usados junto con su tipo y frecuencia.

El método _set_words_panel() crea un panel para cada autor que muestra la cantidad de palabras únicas, el total de palabras y la riqueza léxica, además de una tabla con las 25 palabras más usadas junto con su frecuencia.

Finalmente, el método print_results() imprime todos los paneles y tablas creados anteriormente.

### WhatsappAnalyzer

Esta clase define el objeto WhatsappAnalyzer, el cual se encarga de realizar un análisis de un chat de Whatsapp. El constructor recibe un argumento que puede ser una cadena con la ruta del archivo del chat o un objeto Chat.

Luego, se definen los métodos search_authors(), search_emojis() y search_words(), los cuales recorren el chat y cuentan la cantidad de autores, emojis y palabras utilizadas por cada autor.

Finalmente, se define el método print_summary(), el cual llama a los métodos anteriores para obtener los resultados del análisis y luego imprimirlos mediante el objeto WhatsappResult.
