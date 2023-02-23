#!/bin/bash

pydoc-markdown -I . -m chat_analyzer --render-toc > docs/chat_analyzer.md
pydoc-markdown -I . -m analyzer --render-toc > docs/analyzer.md
pydoc-markdown -I . -m models --render-toc > docs/models.md
pydoc-markdown -I . -m results --render-toc > docs/results.md
pydoc-markdown -I . -m stopwords --render-toc > docs/stopwords.md