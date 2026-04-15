---
title: "Comparison of Multilingual and Bilingual Models for Satirical News Detection of Arabic and English"
date: 2024-12-01
preprint: false           # <— set to `true` only for preprints
authors:
    - "Omar Abdulla"
    - "Aditya Joshi"
    - "Rahat Masood"
    - "Salil Kanhere"

underlineAuthors:
    - "Aditya Joshi"
# arxivID: "2405.15310"
links:
    paper: "https://aclanthology.org/2024.alta-1.14.pdf"
# project:   "https://yourlab.org/project"
venue: "ALTA 2024"      # optional—whatever metadata you like
bibtex:  |
    @inproceedings{abdalla-etal-2024-comparison,
    title = "Comparison of Multilingual and Bilingual Models for Satirical News Detection of {A}rabic and {E}nglish",
    author = "Abdalla, Omar W.  and
      Joshi, Aditya  and
      Masood, Rahat  and
      Kanhere, Salil S.",
    editor = "Baldwin, Tim  and
      Rodr{\'i}guez M{\'e}ndez, Sergio Jos{\'e}  and
      Kuo, Nicholas",
    booktitle = "Proceedings of the 22nd Annual Workshop of the Australasian Language Technology Association",
    month = dec,
    year = "2024",
    address = "Canberra, Australia",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.alta-1.14/",
    pages = "173--178",
    abstract = "Satirical news is real news combined with a humorous comment or exaggerated content, and it often mimics the format and style of real news. However, satirical news is often misunderstood as misinformation, especially by individuals from different cultural and social backgrounds. This research addresses the challenge of distinguishing satire from truthful news by leveraging multilingual satire detection methods in English and Arabic. We explore both zero-shot and chain-of-thought (CoT) prompting using two language models, Jais-chat(13B) and LLaMA-2-chat(7B). Our results show that CoT prompting offers a significant advantage for the Jais-chat model over the LLaMA-2-chat model. Specifically, Jais-chat achieved the best performance, with an F1-score of 80{\%} in English when using CoT prompting. These results high- light the importance of structured reasoning in CoT, which enhances contextual understanding and is vital for complex tasks like satire detection."
    }
---