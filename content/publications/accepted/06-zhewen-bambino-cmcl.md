---
title: "BAMBINO-LM: (Bilingual-)Human-Inspired Continual Pre-training of BabyLM"
date: 2024-08-01
preprint: false           # <— set to `true` only for preprints
authors:
    - "Zhewen Shen"
    - "Aditya Joshi"
    - "Ruey-Cheng Chen"

torwork: true

underlineAuthors:
    - "Zhewen Shen"
    - "Aditya Joshi"
# arxivID: "2405.15310"
links:
    paper: "https://aclanthology.org/2024.cmcl-1.1.pdf"
# project:   "https://yourlab.org/project"
venue: "CMCL @ ACL 2024"      # optional—whatever metadata you like
bibtex:  |
    @inproceedings{shen-etal-2024-bambino,
    title = "{BAMBINO}-{LM}: (Bilingual-)Human-Inspired Continual Pre-training of {B}aby{LM}",
    author = "Shen, Zhewen  and
      Joshi, Aditya  and
      Chen, Ruey-Cheng",
    editor = "Kuribayashi, Tatsuki  and
      Rambelli, Giulia  and
      Takmaz, Ece  and
      Wicke, Philipp  and
      Oseki, Yohei",
    booktitle = "Proceedings of the Workshop on Cognitive Modeling and Computational Linguistics",
    month = aug,
    year = "2024",
    address = "Bangkok, Thailand",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.cmcl-1.1/",
    doi = "10.18653/v1/2024.cmcl-1.1",
    pages = "1--7",
    abstract = "Children from bilingual backgrounds benefit from interactions with parents and teachers to re-acquire their heritage language. In this paper, we investigate how this insight from behavioral study can be incorporated into the learning of small-scale language models. We introduce BAMBINO-LM, a continual pre-training strategy for BabyLM that uses a novel combination of alternation and PPO-based perplexity reward induced from a parent Italian model. Upon evaluation on zero-shot classification tasks for English and Italian, BAMBINO-LM improves the Italian language capability of a BabyLM baseline. Our ablation analysis demonstrates that employing both the alternation strategy and PPO-based modeling is key to this effectiveness gain. We also show that, as a side effect, the proposed method leads to a similar degradation in L1 effectiveness as human children would have had in an equivalent learning scenario. Through its modeling and findings, BAMBINO-LM makes a focused contribution to the pre-training of small-scale language models by first developing a human-inspired strategy for pre-training and then showing that it results in behaviours similar to that of humans."
    }
---