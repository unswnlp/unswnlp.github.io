---
title: "BESSTIE" 
date: 2025-05-16
tags: ["sentiment","sarcasm","australian english","indian english","british english","dataset","python", "dialects"]
author: ["Dipankar Srirag", "Aditya Joshi", "Jordan Painter", "Diptesh Kanojia"]
description: "This is a benchmark dataset for sentiment and sarcasm classification for varieties of English."
summary: "This is a benchmark dataset for sentiment and sarcasm classification for varieties of English."
editPost:
    URL: "https://huggingface.com/datasets/unswnlporg/BESSTIE"
    Text: "Dataset"
showToc: false
disableAnchoredHeadings: false

---

## Dataset Details

### Dataset Description

<!-- Provide a longer summary of what this dataset is. -->

- **Curated by:** Dipankar Srirag, Aditya Joshi, Jordan Painter, and Diptesh Kanojia
- **Funded by:** Google Research Scholar grant
- **Shared by:** UNSW-NLP Group
- **Language:** English
- **Varieties:** Australian English, Indian English, British English
<!-- - **License:** [More Information Needed] -->

### Dataset Sources

<!-- Provide the basic links for the dataset. -->

<!-- - **Repository:** [More Information Needed] -->
- **Paper:** [Accepted to Findings of ACL 2025](https://doi.org/10.48550/arXiv.2412.04726)

## Uses

<!-- Address questions around how the dataset is intended to be used. -->

### Direct Use

<!-- This section describes suitable use cases for the dataset. -->

**BESSTIE** is designed for:
- Sentiment classification across three English varieties: Australian (`en-AU`), Indian (`en-IN`), and British (`en-UK`).
- Sarcasm classification, particularly focusing on the challenges posed by dialectal and cultural variation in these language varieties.
- Evaluating LLM performance across inner-circle (`en-AU`, `en-UK`) and outer-circle (`en-IN`) English varieties.
- Cross-variety and cross-domain generalisation studies for fairness and bias in NLP models.


### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the dataset will not work well for. -->
- Not intended for real-time sentiment monitoring in production without adaptation.
- Should not be used for individual profiling or surveillance, especially given the personal nature of some data.
- Not suitable for non-English or non-dialect-specific sentiment/sarcasm studies, as it only targets three English varieties.
- Not ideal for studying neutral sentiment detection, as neutral labels were discarded during annotation.


## Dataset Structure

<!-- This section provides a description of the dataset fields, and additional information about the dataset structure such as criteria used to create the splits, relationships between data points, etc. -->

- **Languages**: English (Australian, Indian, British varieties)
- **Data Sources**: Google Places reviews (formal), Reddit comments (informal)
- **Tasks**: Sentiment classification (binary), Sarcasm classification (binary)
- **Split**s: Train, Validation, Test
- **Label Distribution**: Stratified for class balance

## Dataset Creation

### Curation Rationale

<!-- Motivation for the creation of this dataset. -->

To fill a gap in current NLP benchmarks by providing a labeled dataset targeting sentiment and sarcasm across varieties of English, which are often overlooked or underrepresented in LLM evaluation.

### Source Data

<!-- This section describes the source data (e.g. news text and headlines, social media posts, translated sentences, ...). -->


#### Data Collection and Processing

<!-- This section describes the data collection and processing process such as data selection criteria, filtering and normalization methods, tools and libraries used, etc. -->
- **GOOGLE reviews**: Collected via Google Places API using location-based filtering in specific cities. Reviews with ratings of 2 or 4 stars were selected.
- **REDDIT comments**: Collected using subreddit-based filtering for relevant regional discussions.
- **Languages and variety detection**: FastText was used for English detection; DistilBERT fine-tuned on ICE-Corpora used for variety prediction.
- **Filtering**: Discarded tourist attraction posts, non-English texts, and anonymized data.


#### Who are the source data producers?

<!-- This section describes the people or systems who originally created the data. It should also include self-reported demographic or identity information for the source data creators if this information is available. -->

- Users of Google Maps and Reddit, writing reviews and comments.
- Demographic identities are inferred from context (location/subreddit), not explicitly recorded.
- The data comes from public sources adhering to terms of use.

### Annotations

<!-- If the dataset contains annotations which are not part of the initial data collection, use this section to describe them. -->

#### Annotation process

<!-- This section describes the annotation process such as annotation tools used in the process, the amount of data annotated, annotation guidelines provided to the annotators, interannotator statistics, annotation validation, etc. -->

- Annotators were native speakers for each variety.
- Annotated both sentiment and sarcasm using detailed guidelines.
- Labels: Positive (1), Negative (0), Discard (2 for uninformative).
- Sarcasm labeled as sarcastic (1), non-sarcastic (0), or discarded.
- Annotators paid 22 USD/hour.


#### Who are the annotators?

<!-- This section describes the people or systems who created the annotations. -->

- Three annotators, including two co-authors, who are native speakers of the respective language varieties.

#### Personal and Sensitive Information

<!-- State whether the dataset contains data that might be considered personal, sensitive, or private (e.g., data that reveals addresses, uniquely identifiable names or aliases, racial or ethnic origins, sexual orientations, religious beliefs, political opinions, financial or health data, etc.). If efforts were made to anonymize the data, describe the anonymization process. -->

- User-identifying information (e.g., usernames) was discarded.
- The dataset does not include personal identifiers or health/financial data.
- Sarcasm and sentiment content may contain strong opinions but not sensitive information per se.

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

- **Bias**: Dataset may reflect regional or platform-specific biases (e.g., Reddit skew).
- **Linguistic variation**: `en-IN` contains more dialectal features and code-mixing, leading to lower model performance.
- **Annotation subjectivity**: Sentiment and sarcasm are inherently subjective.
- **Limited representation**: Focus on three national varieties may exclude broader English dialect diversity.

### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->

Users should consider:
- Evaluating model generalizability across varieties and domains.
- Using caution when applying the dataset to high-stakes applications.
- Applying fairness-aware training methods to mitigate observed biases, especially toward outer-circle English like `en-IN`.


## Citation

<!-- If there is a paper or blog post introducing the dataset, the APA and Bibtex information for that should go in this section. -->

**BibTeX:**

```bib
@misc{srirag2025besstie,
      title={BESSTIE: A Benchmark for Sentiment and Sarcasm Classification for Varieties of English}, 
      author={Dipankar Srirag and Aditya Joshi and Jordan Painter and Diptesh Kanojia},
      year={2025},
      eprint={2412.04726},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

**APA:**

Srirag, D., Joshi, A., Painter, J., & Kanojia, D. (2025). BESSTIE: A Benchmark for Sentiment and Sarcasm Classification for Varieties of English. arXiv preprint arXiv:2412.04726.

## Glossary

<!-- If relevant, include terms and calculations in this section that can help readers understand the dataset or dataset card. -->

- **Inner-circle varieties**: English varieties spoken natively (e.g., `en-AU`, `en-UK`).
- **Outer-circle varieties**: English used as a second language (e.g., `en-IN`).
- **P(eng)**: Probability that a sample is in English (from `fastText`).
- **P(variety)**: Probability that a sample matches the intended English variety (from `DistilBERT`-based predictor).

## More Information

For dataset access, code, and models, see the [official repository link] (to be added when published).

## Dataset Card Authors

Dipankar Srirag, Aditya Joshi, Jordan Painter, Diptesh Kanojia

## Dataset Card Contact

- [d.srirag@unsw.edu.au](mailto:d.srirag@unsw.edu.au)
- [aditya.joshi@unsw.edu.au](mailto:aditya.joshi@unsw.edu.au)
- [jp1106@surrey.ac.uk](mailto:jp1106@surrey.ac.uk)
- [d.kanojia@surrey.ac.uk](mailto:d.kanojia@surrey.ac.uk)
