---
title: "Spectraformer: A Unified Random Feature Framework for Transformer"
date: 2024-05-24
preprint: false           # <— set to `true` only for preprints
masterswork: true
authors:
    - "Duke Nguyen"
    - "Du Yin"
    - "Aditya Joshi"
    - "Flora Salim"

underlineAuthors:
    - "Duke Nguyen"
    - "Aditya Joshi"
# arxivID: "2405.15310"
links:
    paper: "https://doi.org/10.1145/3768161"
    code: "https://github.com/cruiseresearchgroup/spectraformer"
# project:   "https://yourlab.org/project"
venue: "ACM Transactions on Intelligent Systems and Technology"      # optional—whatever metadata you like
bibtex:  |
    @article{10.1145/3768161,
    author = {Nguyen, Duke and Yin, Du and Joshi, Aditya and Salim, Flora},
    title = {Spectraformer: A Unified Random Feature Framework for Transformer},
    year = {2026},
    issue_date = {June 2026},
    publisher = {Association for Computing Machinery},
    address = {New York, NY, USA},
    volume = {17},
    number = {3},
    issn = {2157-6904},
    url = {https://doi.org/10.1145/3768161},
    doi = {10.1145/3768161},
    abstract = {Linearization of attention using various kernel approximation and kernel learning techniques has shown promise. Past methods used a subset of combinations of component functions and weight matrices within the random feature paradigm. We identify the need for a systematic comparison of different combinations of weight matrices and component functions for attention learning in Transformer. Hence, we introduce Spectraformer, a unified framework for approximating and learning the kernel function in the attention mechanism of the Transformer. Our empirical results demonstrate, for the first time, that a random feature-based approach can achieve performance comparable to top-performing sparse and low-rank methods on the challenging Long-Range Arena benchmark. Thus, we establish a new state-of-the-art for random feature-based efficient Transformers. The framework also produces many variants that offer different advantages in accuracy, training time, and memory consumption. Our code is available at: .},
    journal = {ACM Trans. Intell. Syst. Technol.},
    month = mar,
    articleno = {50},
    numpages = {29},
    keywords = {transformers, kernel, linearized attention, kernelized attention}
    }
---