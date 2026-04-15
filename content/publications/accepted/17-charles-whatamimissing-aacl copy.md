---
title: 'What am I missing here?: Evaluating Large Language Models for Masked Sentence Prediction'
date: 2025-12-28
preprint: false           # <— set to `true` only for preprints
authors:
    - "Charles Wyatt"
    - "Aditya Joshi"
    - "Flora Salim"

underlineAuthors:
    - "Charles Wyatt"
    - "Aditya Joshi"
links:
    paper: https://aclanthology.org/2025.ijcnlp-short.24.pdf
# project:   "https://yourlab.org/project"
venue: "AACL 2025"      # optional—whatever metadata you like
bibtex:  |
    @inproceedings{wyatt-etal-2025-missing,
    title = "What am {I} missing here?: Evaluating Large Language Models for Masked Sentence Prediction",
    author = "Wyatt, Charlie  and
      Joshi, Aditya  and
      Salim, Flora D.",
    editor = "Inui, Kentaro  and
      Sakti, Sakriani  and
      Wang, Haofen  and
      Wong, Derek F.  and
      Bhattacharyya, Pushpak  and
      Banerjee, Biplab  and
      Ekbal, Asif  and
      Chakraborty, Tanmoy  and
      Singh, Dhirendra Pratap",
    booktitle = "Proceedings of the 14th International Joint Conference on Natural Language Processing and the 4th Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics",
    month = dec,
    year = "2025",
    address = "Mumbai, India",
    publisher = "The Asian Federation of Natural Language Processing and The Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.ijcnlp-short.24/",
    doi = "10.18653/v1/2025.ijcnlp-short.24",
    pages = "273--283",
    ISBN = "979-8-89176-299-2",
    abstract = "Transformer-based models primarily rely on Next Token Prediction (NTP), which predicts the next token in a sequence based on the preceding context. However, NTP{'}s focus on single-token prediction often limits a model{'}s ability to plan ahead or maintain long-range coherence, raising questions about how well LLMs can predict longer contexts, such as full sentences within structured documents. While NTP encourages local fluency, it provides no explicit incentive to ensure global coherence across sentence boundaries{---}an essential skill for reconstructive or discursive tasks. To investigate this, we evaluate three commercial LLMs (GPT-4o, Claude 3.5 Sonnet, and Gemini 2.0 Flash) on Masked Sentence Prediction (MSP) {---} the task of infilling a randomly removed sentence {---} from three domains: ROCStories (narrative), Recipe1M (procedural), and Wikipedia (expository). We assess both fidelity (similarity to the original sentence) and cohesiveness (fit within the surrounding context). Our key finding reveals that commercial LLMs, despite their superlative performance in other tasks, are poor at predicting masked sentences in low-structured domains, highlighting a gap in current model capabilities."
    }
featured: true
---