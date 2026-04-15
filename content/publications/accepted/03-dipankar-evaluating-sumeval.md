---
title: 'Evaluating Dialect Robustness of Language Models via Conversation Understanding'
date: 2025-01-28
preprint: false           # <— set to `true` only for preprints
masterswork: true
authors:
    - "Dipankar Srirag"
    - "Nihar Ranjan Sahoo"
    - "Aditya Joshi"
# arxivID: "2405.15310"

underlineAuthors:
    - "Dipankar Srirag"
    - "Aditya Joshi"
links:
    paper: https://aclanthology.org/2025.sumeval-2.3.pdf
# project:   "https://yourlab.org/project"
venue: "SUMEval @ COLING 2025"      # optional—whatever metadata you like
bibtex: |
    @inproceedings{srirag-etal-2025-evaluating,
        title = "Evaluating Dialect Robustness of Language Models via Conversation Understanding",
        author = "Srirag, Dipankar  and
        Sahoo, Nihar Ranjan  and
        Joshi, Aditya",
        booktitle = "Proceedings of the Second Workshop on Scaling Up Multilingual {\&} Multi-Cultural Evaluation",
        month = jan,
        year = "2025",
        address = "Abu Dhabi",
        publisher = "Association for Computational Linguistics",
        url = "https://aclanthology.org/2025.sumeval-2.3/",
        pages = "24--38",
        abstract = "With an evergrowing number of LLMs reporting superlative performance for English, their ability to perform equitably for different dialects of English (i.e., dialect robustness) needs to be ascertained. Specifically, we use English language (US English or Indian English) conversations between humans who play the word-guessing game of `taboo{`}. We formulate two evaluative tasks: target word prediction (TWP) (i.e., predict the masked target word in a conversation) and target word selection (TWS) (i.e., select the most likely masked target word in a conversation, from among a set of candidate words). Extending MD3, an existing dialectic dataset of taboo-playing conversations, we introduce M-MD3, a target-word-masked version of MD3 with the en-US and en-IN subsets. We create two subsets: en-MV (where en-US is transformed to include dialectal information) and en-TR (where dialectal information is removed from en-IN). We evaluate three multilingual LLMs{--}one open source (Llama3) and two closed-source (GPT-4/3.5). LLMs perform significantly better for US English than Indian English for both TWP and TWS tasks, for all settings, exhibiting marginalisation against the Indian dialect of English. While GPT-based models perform the best, the comparatively smaller models work more equitably after fine-tuning. Our evaluation methodology exhibits a novel and reproducible way to examine attributes of language models using pre-existing dialogue datasets with language varieties. Dialect being an artifact of one{'}s culture, this paper demonstrates the gap in the performance of multilingual LLMs for communities that do not use a mainstream dialect."
    }
---