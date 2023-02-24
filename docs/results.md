# Table of Contents

* [results](#results)
  * [ResultBuilder](#results.ResultBuilder)
    * [build\_titles](#results.ResultBuilder.build_titles)
    * [build\_emojis\_panel](#results.ResultBuilder.build_emojis_panel)
    * [build\_words\_panel](#results.ResultBuilder.build_words_panel)
    * [build\_images](#results.ResultBuilder.build_images)
    * [build\_all](#results.ResultBuilder.build_all)
    * [reset](#results.ResultBuilder.reset)
    * [set\_chat](#results.ResultBuilder.set_chat)
    * [set\_parameters](#results.ResultBuilder.set_parameters)
  * [ConsoleBuilder](#results.ConsoleBuilder)
    * [print\_results](#results.ConsoleBuilder.print_results)

<a id="results"></a>

# results

results

Author: Christopher Villamarín (xeland314)

Dependencies: standard python modules (abc),
downloaded packages (emoji, nltk, rich).

<a id="results.ResultBuilder"></a>

## ResultBuilder Objects

```python
class ResultBuilder(metaclass=ABCMeta)
```

The ResultBuilder abstract class specifies methods
for creating the different parts of the Result objects.

<a id="results.ResultBuilder.build_titles"></a>

#### build\_titles

```python
@abstractmethod
def build_titles() -> None
```

This method should be implemented
to build the titles to show 
as a result of the analysis.

<a id="results.ResultBuilder.build_emojis_panel"></a>

#### build\_emojis\_panel

```python
@abstractmethod
def build_emojis_panel() -> None
```

This method should be implemented
to build the emojis panel to show 
as a result of the analysis.

<a id="results.ResultBuilder.build_words_panel"></a>

#### build\_words\_panel

```python
@abstractmethod
def build_words_panel() -> None
```

This method should be implemented
to build the words panel to show 
as a result of the analysis.

<a id="results.ResultBuilder.build_images"></a>

#### build\_images

```python
@abstractmethod
def build_images() -> None
```

This method should be implemented
to build the images as a result of the analysis.

<a id="results.ResultBuilder.build_all"></a>

#### build\_all

```python
@abstractmethod
def build_all() -> None
```

This method should be implemented
to build all the results of the analysis.

<a id="results.ResultBuilder.reset"></a>

#### reset

```python
def reset() -> None
```

This method resets the _chat attribute to None.

<a id="results.ResultBuilder.set_chat"></a>

#### set\_chat

```python
def set_chat(chat: Chat) -> None
```

This method sets the chat to be analyzed.

<a id="results.ResultBuilder.set_parameters"></a>

#### set\_parameters

```python
def set_parameters(parameters: dict) -> None
```

This method sets the _parameters attribute to a dictionary
that contains the parameters of the chat analysis.

<a id="results.ConsoleBuilder"></a>

## ConsoleBuilder Objects

```python
class ConsoleBuilder(ResultBuilder)
```

This class provides a way to print/display
the analysis results to the console.

<a id="results.ConsoleBuilder.print_results"></a>

#### print\_results

```python
def print_results() -> None
```

Prints the analysis results in the console.

