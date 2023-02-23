# Table of Contents

* [results](#results)
  * [WhatsappResult](#results.WhatsappResult)
    * [print\_results](#results.WhatsappResult.print_results)

<a id="results"></a>

# results

results

Author: Christopher Villamarín (xeland314)

Dependencies: standard python modules (collections),
downloaded packages (emoji, nltk, rich).

<a id="results.WhatsappResult"></a>

## WhatsappResult Objects

```python
class WhatsappResult(object)
```

Class for storing and printing results of WhatsApp analysis.

**Arguments**:

  - authors (collections.Counter): A Counter object
  containing the message count for each author.
  - emojis_by_person (collections.Counter): A Counter
  object containing the most frequent emojis used by each author.
  - words_by_person (collections.Counter): A Counter
  object containing the most frequent words used by each author.
  - parameters (dict): A dictionary containing the parameters used for analysis.

<a id="results.WhatsappResult.print_results"></a>

#### print\_results

```python
def print_results() -> None
```

Prints the analysis results to the console.
