---
title: "RACCOON: A Retrieval-Augmented Generation Approach for Location Coordinate Capture from News Articles"
date: 2025-04-28
preprint: false           # <— set to `true` only for preprints
honorswork: true
authors:
    - "Jonathan Lin"
    - "Aditya Joshi"
    - "Hye Youg Paik"
    - "et al."

underlineAuthors:
    - "Jonathan Lin"
    - "Aditya Joshi"
# arxivID: "2405.15310"
links:
    paper: "https://arxiv.org/pdf/2501.11440"
# project:   "https://yourlab.org/project"
venue: "WWW 2025"      # optional—whatever metadata you like
bibtex:  |
    @inproceedings{10.1145/3701716.3715501,
    author = {Lin, Jonathan and Joshi, Aditya and Paik, Hye-young and Doung, Tri Dung and Gurdasani, Deepti},
    title = {RACCOON: A Retrieval-Augmented Generation Approach for Location Coordinate Capture from News Articles},
    year = {2025},
    isbn = {9798400713316},
    publisher = {Association for Computing Machinery},
    address = {New York, NY, USA},
    url = {https://doi.org/10.1145/3701716.3715501},
    doi = {10.1145/3701716.3715501},
    abstract = {Geocoding involves automatic extraction of location coordinates of incidents reported in news articles, and can be used for epidemic intelligence or disaster management. This paper introduces Retrieval-Augmented Coordinate Capture Of Online News articles (RACCOON), an open-source geocoding approach that extracts geolocations from news articles. RACCOON uses a retrieval-augmented generation (RAG) approach where candidate locations and associated information are retrieved in the form of context from a location database, and a prompt containing the retrieved context, location mentions and news articles is fed to an LLM to generate the location coordinates. Our evaluation on three datasets, two underlying LLMs, three baselines and several ablation tests based on the components of RACCOON demonstrate the utility of RACCOON. To the best of our knowledge, RACCOON is the first RAG-based approach for geocoding using pre-trained LLMs.},
    booktitle = {Companion Proceedings of the ACM on Web Conference 2025},
    pages = {1123–1127},
    numpages = {5},
    keywords = {geocoding, large language models, location extraction, news articles, rag, retrieval-augmented generation},
    location = {Sydney NSW, Australia},
    series = {WWW '25}
    }
featured: true
---