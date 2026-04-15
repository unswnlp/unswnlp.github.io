---
title: "Far Out: Evaluating Language Models on Slang in Australian and Indian English"
date: 2026-04-08
preprint: false           # <— set to `true` only for preprints
authors:
    - "Deniz Dilsiz"
    - "Dipankar Srirag"
    - "Aditya Joshi"

underlineAuthors:
    - "Deniz Dilsiz"
    - "Dipankar Srirag"
    - "Aditya Joshi"

links:
    paper: "https://aclanthology.org/2026.vardial-1.2.pdf"
venue: "VarDial @ EACL 2026"      # optional—whatever metadata you like
bibtex:  |
    @inproceedings{dilsiz-etal-2026-far,
    title = "Far Out: Evaluating Language Models on Slang in {A}ustralian and {I}ndian {E}nglish",
    author = "Dilsiz, Deniz Kaya  and
      Srirag, Dipankar  and
      Joshi, Aditya",
    editor = {Scherrer, Yves  and
      Aepli, No{\"e}mi  and
      Blaschke, Verena  and
      Jauhiainen, Tommi  and
      Ljube{\v{s}}i{\'c}, Nikola  and
      Nakov, Preslav  and
      Tiedemann, J{\"o}rg  and
      Zampieri, Marcos},
    booktitle = "Proceedings of the 13th Workshop on {NLP} for Similar Languages, Varieties and Dialects",
    month = mar,
    year = "2026",
    address = "Rabat, Morocco",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2026.vardial-1.2/",
    doi = "10.18653/v1/2026.vardial-1.2",
    pages = "18--31",
    abstract = "Language models exhibit systematic performance gaps when processing text in non-standard language varieties, yet their ability to comprehend variety-specific slang remains underexplored for several languages. We present a comprehensive evaluation of slang awareness in Indian English (en-IN) and Australian English (en-AU) across seven state-of-the-art language models. We construct two complementary datasets: WEB, containing 377 web-sourced usage examples from Urban Dictionary, and GEN, featuring 1,492 synthetically generated usages of these slang terms, across diverse scenarios. We assess language models on three tasks: target word prediction (TWP), guided target word prediction (TWP*) and target word selection (TWS). Our results reveal four key findings: (1) Higher average model performance TWS versus TWP and TWP*, with average accuracy score increasing from 0.03 to 0.49 respectively (2) Stronger average model performance on WEB versus GEN datasets, with average similarity score increasing by 0.03 and 0.05 across TWP and TWP* tasks respectively (3) en-IN tasks outperform en-AU when averaged across all models and datasets, with TWS demonstrating the largest disparity, increasing average accuracy from 0.44 to 0.54. These findings underscore fundamental asymmetries between generative and discriminative competencies for variety-specific language, particularly in the context of slang expressions despite being in a technologically rich language such as English."
    }
---