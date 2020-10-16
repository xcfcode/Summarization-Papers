# Summarization Papers

![](https://img.shields.io/badge/Status-building-brightgreen) ![](https://img.shields.io/badge/PRs-Welcome-red) 

This repo contains a list of summarization papers including various topics. If any error, please open an issue. 

> For more topics, please refer to another repo [xcfcode/What-I-Have-Read](https://github.com/xcfcode/What-I-Have-Read), including Meta Learning, Graph Neural Networks (GNN), Knowledge Distillation, Pre-trained Language Models, Natural Language Generation and several [survey and paper slides](https://github.com/xcfcode/What-I-Have-Read#slides).

## Content
   * [Summarization Papers](#summarization-papers)
      * [Content](#content)
      * [Presentations &amp;&amp; Notes](#presentations--notes)
      * [Survey](#survey)
      * [Dataset](#dataset)
      * [Scientific Document](#scientific-document)
      * [Factuality](#factuality)
      * [Sentiment Related](#sentiment-related)
      * [Pretrain Based](#pretrain-based)
      * [Style](#style)
      * [Dialogue](#dialogue)
      * [Graph-Based](#graph-based)
      * [Multi-Document](#multi-document)
      * [Cross-Lingual](#cross-lingual)
      * [Unsupervised](#unsupervised)
      * [Multi-modal](#multi-modal-1)
      * [Concept-map-based](#concept-map-based)
      * [Timeline](#timeline)
      * [Opinion](#opinion)
      * [Reinforcement Learning](#reinforcement-learning)
      * [Reward Learning](#reward-learning)
      * [Evaluation](#evaluation)
      * [Controlled](#controlled)
      * [Analysis](#analysis)
      * [Theory](#theory)
      * [Extractive](#extractive)
      * [Abstractive](#abstractive)
      * [Extractive-Abstractive](#extractive-abstractive)
      * [Syntactic](#syntactic)
      * [QA Related](#qa-related)
      * [Toolkit](#toolkit)

## Presentations && Notes
> **Presentations** and **Notes** I have made for Summarization in our group.

* Presentations
    * [Multi-modal Summarization](slides/presentation/Multi-modal-Summarization.pdf)
    * [ACL20 Summarization](slides/presentation/acl2020-summarization.pdf)
    * [文本摘要简述 (Chinese)](slides/presentation/文本摘要简述.pdf)
    * [ACL19 Summarization](slides/presentation/ACL19%20Summarization.pdf)
* Notes
    * [Brief intro to summarization (Chinese)](slides/notes/Brief-intro-to-summarization.pdf)
    * [EMNLP19 Summarization (Chinese)](slides/notes/EMNLP19_Summarization.pdf)
* Papers
    * [ACL19-A Simple Theoretical Model of Importance for Summarization](slides/paper-slides/A%20Simple%20Theoretical%20Model%20of%20Importance%20for%20Summarization.pdf)
    * [ACL19-Multimodal Abstractive Summarization for How2 Videos](slides/paper-slides/Multimodal%20Abstractive%20Summarization%20for%20How2%20Videos.pdf)

## Survey
<details><summary>papers</summary><p>

| Paper | Conference |
| :---: | :---: |
|[Deep Learning Based Abstractive Text Summarization: Approaches, Datasets, Evaluation Measures, and Challenges](https://www.semanticscholar.org/paper/Deep-Learning-Based-Abstractive-Text-Summarization%3A-Suleiman-Awajan/b7da726c244287748575ef404009609afde45bea)||
|[A Survey of Knowledge-Enhanced Text Generation](https://arxiv.org/abs/2010.04389)||
|[From Standard Summarization to New Tasks and Beyond: Summarization with Manifold Information](https://arxiv.org/abs/2005.04684)|IJCAI20|
|[Neural Abstractive Text Summarization with Sequence-to-Sequence Models](https://arxiv.org/abs/1812.02303)||
|[A Survey on Neural Network-Based Summarization Methods](https://arxiv.org/abs/1804.04589)||
|[Automated text summarisation and evidence-based medicine: A survey of two domains](https://arxiv.org/abs/1706.08162)||
|[Automatic Keyword Extraction for Text Summarization: A Survey](https://arxiv.org/abs/1704.03242)||
|[Text Summarization Techniques: A Brief Survey](https://arxiv.org/abs/1707.02268)||
|[Recent automatic text summarization techniques: a survey](https://link.springer.com/article/10.1007/s10462-016-9475-9)||
</p></details>

## Dataset
<details><summary>papers</summary><p>

|ID|Name|Description|Paper|Conference|
|:---:|:---:|:---:|:---:|:---:|
| 1 | CNN-DailyMail | News| [Abstractive Text Summarization using Sequence\-to\-sequence RNNs and Beyond ](https://www.aclweb.org/anthology/K16-1028/)|SIGNLL16|
| 2 | New York Times| News | [The New York Times Annotated Corpus](https://catalog.ldc.upenn.edu/LDC2008T19) |
| 3 | DUC| News | [The Effects Of Human Variation In DUC Summarization Evaluation](https://www.aclweb.org/anthology/W04-1003/) |
| 4 | Gigaword | News | [A Neural Attention Model For Abstractive Sentence Summarization](https://arxiv.org/abs/1509.00685) |EMNLP15|
| 5 | Newsroom | News | [Newsroom: A Dataset of 1\.3 Million Summaries with Diverse Extractive Strategies](https://www.aclweb.org/anthology/N18-1065)|NAACL18|
| 6 | Xsum | News | [Don’t Give Me the Details, Just the Summary\! Topic\-Aware Convolutional Neural Networks for Extreme Summarization](https://www.aclweb.org/anthology/D18-1206/)|EMNLP18|
| 7 | Multi\-News| Multi-document News | [Multi\-News: a Large\-Scale Multi\-Document Summarization Dataset and Abstractive Hierarchical Model](https://arxiv.org/abs/1906.01749)|ACL19|
| 8 | SAMSum| Multi-party conversation | [SAMSum Corpus: A Human\-annotated Dialogue Dataset for Abstractive Summarization](https://arxiv.org/abs/1911.12237)|EMNLP19|
| 9 | AMI | Meeting | [The AMI Meeting Corpus: A pre\-announcement\. ](http://groups.inf.ed.ac.uk/ami/download/)|
| 10 | ICSI| Meeting | [The ICSI Meeting Corpus](http://groups.inf.ed.ac.uk/ami/icsi/) |
| 11 | MSMO| Multi-modal | [MSMO: Multimodal Summarization with Multimodal Output](https://www.aclweb.org/anthology/D18-1448/) |EMNLP18|
| 12 | How2 | Multi-modal | [How2: A Large\-scale Dataset for Multimodal Language Understanding](https://arxiv.org/abs/1811.00347)| NIPS18|
| 13 | ScisummNet | Scientific paper | [ScisummNet: A Large Annotated Corpus and Content\-Impact Models for Scientific Paper Summarization with Citation Networks](https://arxiv.org/abs/1909.01716) |AAAI19|
| 14 | PubMed, ArXiv | Scientific paper | [A Discourse\-Aware Attention Model for Abstractive Summarization of Long Documents](https://arxiv.org/abs/1804.05685)| NAACL18 |
| 15 | TALKSUMM | Scientific paper | [TALKSUMM: A Dataset and Scalable Annotation Method for Scientiﬁc Paper Summarization Based on Conference Talks](https://www.aclweb.org/anthology/P19-1204/) | ACL19 |
| 16 | BillSum | Legal | [BillSum: A Corpus for Automatic Summarization of US Legislation](https://www.aclweb.org/anthology/D19-5406/) |EMNLP19|
| 17 | LCSTS| Chinese Weibo| [LCSTS: A Large Scale Chinese Short Text Summarization Dataset ](https://www.aclweb.org/anthology/D15-1229/)|EMNLP15|
| 18 | WikiHow| Online Knowledge Base | [WikiHow: A Large Scale Text Summarization Dataset](https://arxiv.org/abs/1810.09305) |
| 19 | Concept-map-based MDS Corpus| Educational Multi-document| [Bringing Structure into Summaries : Crowdsourcing a Benchmark Corpus of Concept Maps](https://www.aclweb.org/anthology/D17-1320/)|EMNLP17|
| 20 | WikiSum | Wikipedia Multi-document | [Generating Wikipedia By Summarizing Long Sequence](https://arxiv.org/abs/1801.10198) |ICLR18|
| 21 | GameWikiSum | Game Multi-document | [GameWikiSum : a Novel Large Multi\-Document Summarization Dataset](https://arxiv.org/abs/2002.06851) |LREC20|
| 22 | En2Zh CLS, Zh2En CLS| Cross-Lingual | [NCLS: Neural Cross\-Lingual Summarization](https://arxiv.org/abs/1909.00156) |EMNLP19|
| 23 | Timeline Summarization Dataset| Baidu timeline| [Learning towards Abstractive Timeline Summarization ](https://www.ijcai.org/Proceedings/2019/686)|IJCAI19|
| 24 | Reddit TIFU | online discussion | [Abstractive Summarization of Reddit Posts with Multi\-level Memory Networks](https://arxiv.org/abs/1811.00783)| NAACL19 |
| 25 | TripAtt | Review | [Attribute\-aware Sequence Network for Review Summarization](https://www.aclweb.org/anthology/D19-1297/)|EMNLP19|
| 26 | Reader Comments Summarization Corpus | Comments-based Weibo | [Abstractive Text Summarization by Incorporating Reader Comments ](https://arxiv.org/abs/1812.05407)|AAAI19|
| 27 | BIGPATENT | Patent| [BIGPATENT: A Large\-Scale Dataset for Abstractive and Coherent Summarization](https://arxiv.org/abs/1906.03741)|ACL19|
| 28 | Curation Corpus | News | [Curation Corpus for Abstractive Text Summarisation](https://github.com/CurationCorp/curation-corpus) |
| 29 | MATINF |Multi-task|[MATINF: A Jointly Labeled Large-Scale Dataset for Classification, Question Answering and Summarization](https://arxiv.org/abs/2004.12302)|ACL20|
| 30 | MLSUM |Multi-Lingual Summarization Dataset|[MLSUM: The Multilingual Summarization Corpus](https://arxiv.org/abs/2004.14900)|EMNLP20|
| 31 | Dialogue(Debate)|Argumentative Dialogue Summary Corpus |[Using Summarization to Discover Argument Facets in Online Idealogical Dialog](https://www.aclweb.org/anthology/N15-1046/)|NAACL15|
|32|WCEP|News Multi-document|[A Large-Scale Multi-Document Summarization Dataset from the Wikipedia Current Events Portal](https://arxiv.org/abs/2005.10070)|ACL20 Short|
|33|ArgKP|Argument-to-key Point Mapping|[From Arguments to Key Points: Towards Automatic Argument Summarization](https://arxiv.org/abs/2005.01619)|ACL20|
|34|CRD3|Dialogue|[Storytelling with Dialogue: A Critical Role Dungeons and Dragons Dataset](https://www.aclweb.org/anthology/2020.acl-main.459/)|2020||
|35|Gazeta|Russian news|[Dataset for Automatic Summarization of Russian News](https://arxiv.org/abs/2006.11063)||
|36|MIND|English news recommendation, Summarization, Classification, Entity|[MIND: A Large-scale Dataset for News Recommendation](https://www.aclweb.org/anthology/2020.acl-main.331/)|ACL20|
|37|public_meetings|french meeting(test set)|[Align then Summarize: Automatic Alignment Methods for Summarization Corpus Creation](https://www.aclweb.org/anthology/2020.lrec-1.829)|LREC|
|38|Enron|Email|[Building a Dataset for Summarization and Keyword Extraction from Emails](https://www.aclweb.org/anthology/L14-1028/)|2014| 349 emails and threads|
|39|Columbia|Email|[Summarizing Email Threads]([https://www.aclweb.org/anthology/N04-4027.pdf](https://dl.acm.org/doi/10.5555/1613984.1614011))|2004|96 email threads,average of 3.25 email|
|40|BC3|Email|[A publicly available annotated corpus for supervised email summarization](https://www.ufv.ca/media/assets/computer-information-systems/gabriel-murray/publications/aaai08.pdf)||40 email threads (3222 sentences)|
|41|WikiLingua|Cross-Lingual|[WikiLingua- A New Benchmark Dataset for Cross-Lingual Abstractive Summarization](https://arxiv.org/abs/2010.03093)|Findings of EMNLP20|
|42|LcsPIRT|Chinese Dialogue|[Global Encoding for Long Chinese Text Summarization](https://dl.acm.org/doi/10.1145/3407911)|TALLIP|
|43|CLTS|Chinese News|[CLTS: A New Chinese Long Text Summarization Dataset](https://link.springer.com/chapter/10.1007/978-3-030-60450-9_42)|NLPCC20|[Data](https://github.com/lxj5957/CLTS-Dataset)|
|44|[VMSMO](https://github.com/yingtaomj/VMSMO)|Multi-modal|[VMSMO: Learning to Generate Multimodal Summary for Video-based News Articles](https://arxiv.org/abs/2010.05406)|EMNLP20 |
|45|[Multi-XScience](https://github.com/yaolu/Multi-XScience)|Multi-document|[Multi-XScience: A Large-scale Dataset for Extreme Multi-document Summarization of Scientiﬁc Articles](http://www.cs.toronto.edu/~lcharlin/papers/Multi-XScience.pdf)|EMNLP20 short|
|46|[SCITLDR](https://github.com/allenai/scitldr)|Scientific Document|[TLDR: Extreme Summarization of Scientific Documents](https://arxiv.org/abs/2004.15011)|Findings of EMNLP20|
</p></details>

## Scientific Document
<details><summary>papers</summary><p>

| Paper | Conference | Dataset |
| :---: | :---: | :---: |
|[scisumm-corpus](https://github.com/WING-NUS/scisumm-corpus)||[scisumm-corpus](https://github.com/WING-NUS/scisumm-corpus)|
|[Enhancing Extractive Text Summarization with Topic-Aware Graph Neural Networks](https://arxiv.org/abs/2010.06253)|COLING20|
|[Multi-XScience: A Large-scale Dataset for Extreme Multi-document Summarization of Scientiﬁc Articles](http://www.cs.toronto.edu/~lcharlin/papers/Multi-XScience.pdf)|EMNLP20 Short|[Dataset: Multi-XScience](https://github.com/yaolu/Multi-XScience)|
|[TLDR: Extreme Summarization of Scientific Documents](https://arxiv.org/abs/2004.15011)|Findings of EMNLP20|[Dataset: SCITLDR](https://github.com/allenai/scitldr)|
|[Extractive Summarization of Long Documents by Combining Global and Local Context](https://arxiv.org/abs/1909.08089)|EMNLP19|
|[ScisummNet: A Large Annotated Corpus and Content\-Impact Models for Scientific Paper Summarization with Citation Networks](https://arxiv.org/abs/1909.01716) |AAAI19|[Dataset: ScisummNet](https://cs.stanford.edu/~myasu/projects/scisumm_net/)|
|[TalkSumm: A Dataset and Scalable Annotation Method for Scientific Paper Summarization Based on Conference Talks](https://www.aclweb.org/anthology/P19-1204/) |ACL19|[Dataset: TALKSUMM](https://github.com/levguy/talksumm)|
|[A Discourse\-Aware Attention Model for Abstractive Summarization of Long Documents](https://arxiv.org/abs/1804.05685)|NAACL18|[Dataset: PubMed, ArXiv](https://github.com/armancohan/long-summarization)|
</p></details>

## Factuality 
<details><summary>papers</summary><p>

1. **Multi-Fact Correction in Abstractive Text Summarization.** *Yue Dong, Shuohang Wang, Zhe Gan, Yu Cheng, Jackie Chi Kit Cheung, Jingjing Liu* `EMNLP20` [[pdf]](https://arxiv.org/abs/2010.02443) ![](https://img.shields.io/badge/-correct-red)
2. **Factual Error Correction for Abstractive Summarization Models** *Cao Meng, Yue Cheung Dong, Jiapeng Wu, and Jackie Chi Kit* `EMNLP20` [[pdf]]() ![](https://img.shields.io/badge/-correct-red)
3. **Evaluating the Factual Consistency of Abstractive Text Summarization** *Wojciech Kryściński, Bryan McCann, Caiming Xiong, Richard Socher* `EMNLP20` [[pdf]](https://arxiv.org/abs/1910.12840) [[code]](https://github.com/salesforce/factCC)![](https://img.shields.io/badge/-evaluation-brightgreen)
4. **Controlled Hallucinations:Learning to Generate Faithfully from Noisy Data ** *Katja Fillippova* `EMNLP-Findings20` [[pdf]](https://arxiv.org/pdf/2010.05873v1.pdf) ![](https://img.shields.io/badge/-improve-orange)
5. **Reducing Quantity Hallucinations in Abstractive Summarization** *Zheng Zhao, Shay B. Cohen, Bonnie Webber*`EMNLP-Findings20` [[pdf]](https://arxiv.org/abs/2009.13312) ![](https://img.shields.io/badge/-evaluation-brightgreen)
6. **Attractive or Faithful? Popularity-Reinforced Learning for Inspired Headline Generation** *Yun-Zhu Song, Hong-Han Shuai, Sung-Lin Yeh, Yi-Lun Wu, Lun-Wei Ku, Wen-Chih Peng* `AAAI20` [[pdf]](https://arxiv.org/abs/2002.02095) [[code]](https://github.com/yunzhusong/AAAI20-PORLHG) ![](https://img.shields.io/badge/-improve-orange)
7. **On Faithfulness and Factuality in Abstractive Summarization**  *Joshua Maynez, Shashi Narayan, Bernd Bohnet, Ryan McDonald*`ACL20` [[pdf]](https://arxiv.org/abs/2005.00661) [[data]](https://github.com/google-research-datasets/xsum_hallucination_annotations) ![](https://img.shields.io/badge/-analysis-blue)
8. **Improving Truthfulness of Headline Generation**  *Kazuki Matsumaru, Sho Takase, Naoaki Okazaki* `ACL20`[[pdf]](https://arxiv.org/abs/2005.00882) ![](https://img.shields.io/badge/-improve-orange)
9. **Optimizing the Factual Correctness of a Summary: A Study of Summarizing Radiology Reports**  *Yuhao Zhang, Derek Merck, Emily Bao Tsai, Christopher D. Manning, Curtis P. Langlotz* `ACL20`[[pdf]](https://arxiv.org/abs/1911.02541) ![](https://img.shields.io/badge/-improve-orange)
10. **FEQA: A Question Answering Evaluation Framework for Faithfulness Assessment in Abstractive Summarization** *Esin Durmus, He He, Mona Diab* `ACL20` [[pdf]](https://arxiv.org/abs/2005.03754) [[code]](https://github.com/esdurmus/feqa) ![](https://img.shields.io/badge/-evaluation-brightgreen)
11. **Asking and Answering Questions to Evaluate the Factual Consistency of Summaries** *Alex Wang, Kyunghyun Cho, Mike Lewis* `ACL20` [[pdf]](https://arxiv.org/abs/2004.04228) [[code]](https://github.com/W4ngatang/qags)![](https://img.shields.io/badge/-evaluation-brightgreen)
12. **Knowledge Graph-Augmented Abstractive Summarization with Semantic-Driven Cloze Reward** *Luyang Huang, Lingfei Wu, Lu Wang* `ACL20` [[pdf]](https://arxiv.org/abs/2005.01159) ![](https://img.shields.io/badge/-improve-orange)
13. **Boosting Factual Correctness of Abstractive Summarization with Knowledge Graph** *Chenguang Zhu, William Hinthorn, Ruochen Xu, Qingkai Zeng, Michael Zeng, Xuedong Huang, Meng Jiang* `arXiv20` [[pdf]](https://arxiv.org/abs/2003.08612) ![](https://img.shields.io/badge/-improve-orange)
14. **Mind The Facts: Knowledge-Boosted Coherent Abstractive Text Summarization** *Beliz Gunel, Chenguang Zhu, Michael Zeng, Xuedong Huang* `NIPS19` [[pdf]](https://arxiv.org/abs/2006.15435) ![](https://img.shields.io/badge/-improve-orange)
15. **Assessing The Factual Accuracy of Generated Text** *Ben Goodrich, Vinay Rao, Mohammad Saleh, Peter J Liu* `KDD19` [[pdf]](https://arxiv.org/abs/1905.13322) ![](https://img.shields.io/badge/-evaluation-brightgreen)
16. **Ranking Generated Summaries by Correctness: An Interesting but Challenging Application for Natural Language Inference** *Tobias Falke, Leonardo F. R. Ribeiro, Prasetya Ajie Utama, Ido Dagan, Iryna Gurevych* `ACL19` [[pdf]](https://www.aclweb.org/anthology/P19-1213/) [[data]](https://tudatalib.ulb.tu-darmstadt.de/handle/tudatalib/2002) ![](https://img.shields.io/badge/-improve-orange)
17. **Ensure the Correctness of the Summary: Incorporate Entailment Knowledge into Abstractive Sentence Summarization** *Haoran Li, Junnan Zhu, Jiajun Zhang, Chengqing Zong* `COLING` [[pdf]](https://www.aclweb.org/anthology/C18-1121/) [[code]](https://github.com/hrlinlp/entail_sum) ![](https://img.shields.io/badge/-improve-orange)
18. **Faithful to the Original: Fact-Aware Neural Abstractive Summarization** *Ziqiang Cao, Furu Wei, Wenjie Li, Sujian Li* `AAAI18` [[pdf]](https://arxiv.org/abs/1711.04434) ![](https://img.shields.io/badge/-improve-orange)

</p></details>

## Sentiment Related
<details><summary>papers</summary><p>

| Paper | Conference |
| :---: | :---: |
|[A Unified Dual-view Model for Review Summarization and Sentiment Classification with Inconsistency Loss](https://arxiv.org/abs/2006.01592)|SIGIR20|
|[A Hierarchical End-to-End Model for Jointly Improving Text Summarization and Sentiment Classification](https://arxiv.org/abs/1805.01089)|IJCAI18|
|[Two-level Text Summarization from Online News Sources with Sentiment Analysis](https://ieeexplore.ieee.org/document/8076735)|IEEE17|
|[Creating Video Summarization From Emotion Perspective](https://ieeexplore.ieee.org/document/7878001/)|ICSP16|
</p></details>

## Pretrain Based
<details><summary>papers</summary><p>

| Paper | Conference |
| :---: | :---: |
|[Pre-training for Abstractive Document Summarization by Reinstating Source Text](https://arxiv.org/abs/2004.01853v3)|EMNLP20|
|[PALM: Pre-training an Autoencoding&Autoregressive Language Model for Context-conditioned Generation](https://arxiv.org/abs/2004.07159)|EMNLP20|
|[TED: A Pretrained Unsupervised Summarization Model with Theme Modeling and Denoising](https://www.microsoft.com/en-us/research/publication/ted-a-pretrained-unsupervised-summarization-model-with-theme-modeling-and-denoising/)|Findings of EMNLP20|
|[QURIOUS: Question Generation Pretraining for Text Generation](https://arxiv.org/pdf/2004.11026.pdf)|ACL20 Short|
|[PEGASUS: Pre-training with Extracted Gap-sentences for Abstractive Summarization](https://arxiv.org/abs/1912.08777)|ICML20|
|[Abstractive Text Summarization based on Language Model Conditioning and Locality Modeling](https://arxiv.org/abs/2003.13027)|LREC20|
|[Abstractive Summarization with Combination of Pre-trained Sequence-to-Sequence and Saliency Models](https://arxiv.org/abs/2003.13028)|
|[Learning by Semantic Similarity Makes Abstractive Summarization Better](https://arxiv.org/abs/2002.07767)|
|[Make Lead Bias in Your Favor: A Simple and Effective Method for News Summarization](https://arxiv.org/abs/1912.11602)||
| [Text Summarization with Pretrained Encoders](https://arxiv.org/abs/1908.08345)| EMNLP19 |
| [HIBERT: Document Level Pre-training of Hierarchical Bidirectional Transformers for Document Summarization](https://www.aclweb.org/anthology/P19-1499/) | ACL19 |
| [MASS: Masked Sequence to Sequence Pre-training for Language Generation](https://arxiv.org/abs/1905.02450)|ICML19|
| [Pretraining-Based Natural Language Generation for Text Summarization](https://arxiv.org/abs/1902.09243)|
| [Fine-tune BERT for Extractive Summarization](https://arxiv.org/abs/1903.10318)||
| [Unified Language Model Pre-training for Natural Language Understanding and Generation](https://arxiv.org/abs/1905.03197)|NIPS19|
|[Self-Supervised Learning for Contextualized Extractive Summarization](https://www.aclweb.org/anthology/P19-1214/) |ACL19 |
| [Efficient Adaptation of Pretrained Transformers for Abstractive Summarization](https://arxiv.org/abs/1906.00138) ||
</p></details>

## Style
<details><summary>papers</summary><p>

| Paper | Conference | Highlights |
| :---: | :---: | :---: |
|[Hooks in the Headline: Learning to Generate Headlines with Controlled Styles](https://arxiv.org/abs/2004.01980)|ACL20|Summarization + Style transfer|
</p></details>

## Dialogue 
<details><summary>papers</summary><p>

### Medical
| Paper | Conference |
| :---: | :---: |
|[Dr. Summarize: Global Summarization of Medical Dialogue by Exploiting Local Structures](https://arxiv.org/abs/2009.08666)|Findings of EMNLP20|
|[Medical Dialogue Summarization for Automated Reporting in Healthcare](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7225507/)||
|[Alignment Annotation for Clinic Visit Dialogue to Clinical Note Sentence Language Generation](https://www.aclweb.org/anthology/2020.lrec-1.52/)|LREC20||
|[Generating SOAP Notes from Doctor-Patient Conversations](https://arxiv.org/pdf/2005.01795.pdf)||
|[Generating Medical Reports from Patient-Doctor Conversations using Sequence-to-Sequence Models](https://www.aclweb.org/anthology/2020.nlpmc-1.4/)|ACL20 Short||
|[Automatically Generating Psychiatric Case Notes From Digital Transcripts of Doctor-Patient Conversations](https://www.aclweb.org/anthology/W19-1918/)|NAACL19|
| [Topic-aware Pointer-Generator Networks for Summarizing Spoken Conversations](https://arxiv.org/abs/1910.01335) |ASRU19|

### French Meeting
| Paper | Conference |
| :---: | :---: |
|[Align then Summarize: Automatic Alignment Methods for Summarization Corpus Creation](https://www.aclweb.org/anthology/2020.lrec-1.829)|LREC20|
|[Leverage Unlabeled Data for Abstractive Speech Summarization with Self-Supervised Learning and Back-Summarization](https://arxiv.org/abs/2007.15296)|SPECOM20|

### Meeting
| Paper | Conference |
| :---: | :---: |
|[A Study of Text Summarization Techniques for Generating Meeting Minutes](https://link.springer.com/chapter/10.1007/978-3-030-50316-1_33)||
|[Restructuring Conversations using Discourse Relations for Zero-shot Abstractive Dialogue Summarization](https://arxiv.org/abs/1902.01615)||
|[How to Interact and Change? Abstractive Dialogue Summarization with Dialogue Act Weight and Topic Change Info](https://link.springer.com/chapter/10.1007/978-3-030-55393-7_22)|KSEM20|
|[Abstractive Text Summarization of Meetings](https://github.com/Bastian/Abstractive-Summarization-of-Meetings)||
|[A Hierarchical Network for Abstractive Meeting Summarization with Cross-Domain Pretraining](https://www.microsoft.com/en-us/research/uploads/prod/2020/04/MeetingNet_EMNLP_full.pdf)|EMNLP20|
|[Meeting Summarization, A Challenge for Deep Learning](https://link.springer.com/chapter/10.1007/978-3-030-20521-8_53)||
|[End-to-End Abstractive Summarization for Meetings](https://arxiv.org/abs/2004.02016)|2020|
| [Abstractive Meeting Summarization via Hierarchical Adaptive Segmental Network Learning](https://dl.acm.org/doi/10.1145/3308558.3313619) | WWW19 |
| [Abstractive Dialogue Summarization with Sentence-Gated Modeling Optimized by Dialogue Acts](https://arxiv.org/abs/1809.05715) | SLT18 |
| [Unsupervised Abstractive Meeting Summarization with Multi-Sentence Compression and Budgeted Submodular Maximization](https://arxiv.org/abs/1805.05271) | ACL18|
|[Generating Abstractive Summaries from Meeting Transcripts](https://arxiv.org/abs/1609.07033)|||
|[Automatic meeting summarization and topic detection system](https://www.emerald.com/insight/content/doi/10.1108/DTA-09-2017-0062/full/html)||
|[Automatic Community Creation for Abstractive Spoken Conversation Summarization](https://www.aclweb.org/anthology/W17-4506/)|ACL17 workshop||
| [Abstractive Meeting Summarization Using Dependency Graph Fusion](https://arxiv.org/abs/1609.07035) | WWW15 |
|[Domain-Independent Abstract Generation for Focused Meeting Summarization](https://www.aclweb.org/anthology/P13-1137.pdf)|ACL13||
| [Summarizing Decisions in Spoken Meetings](https://arxiv.org/abs/1606.07965) | ACL11 |
|[Automatic analysis of multiparty meetings](https://link.springer.com/article/10.1007/s12046-011-0051-3)|11|
|[A keyphrase based approach to interactive meeting summarization](https://ieeexplore.ieee.org/document/4777863)|08|key phrase guide|
|[What are meeting summaries? An analysis of human extractive summaries in meeting corpus](https://www.aclweb.org/anthology/W08-0112/)|08||
|[Evaluating the effectiveness of features and sampling in extractive meeting summarization](https://ieeexplore.ieee.org/document/4777864)|2008||
|[Automatic Summarization of Conversational Multi-Party Speech](https://www.aaai.org/Papers/AAAI/2006/AAAI06-335.pdf)|AAAI06||
|[Focused Meeting Summarization via Unsupervised Relation Extraction](https://www.aclweb.org/anthology/W12-1642.pdf)||
|[Exploring Speaker Characteristics for Meeting Summarization](https://www.isca-speech.org/archive/archive_papers/interspeech_2010/i10_2518.pdf)|10|
|[A global optimization framework for meeting summarization](https://ieeexplore.ieee.org/document/4960697)|06|
|[Semantic Similarity Applied to Spoken Dialogue Summarization](https://www.semanticscholar.org/paper/Semantic-Similarity-Applied-to-Spoken-Dialogue-Gurevych-Strube/5d7e179f1543108f06f09ba801ae70ba38900c5d)|COLING04|

#### Multi-modal
| Paper | Conference |
| :---: | :---: |
|[A Multimodal Meeting Browser that Implements an Important Utterance Detection Model based on Multimodal Information](https://dl.acm.org/doi/abs/10.1145/3379336.3381491)||
|[Exploring Methods for Predicting Important Utterances Contributing to Meeting Summarization](https://www.mdpi.com/2414-4088/3/3/50)||
| [Keep Meeting Summaries on Topic: Abstractive Multi-Modal Meeting Summarization](https://www.aclweb.org/anthology/P19-1210/)| ACL19 |
|[Fusing Verbal and Nonverbal Information for Extractive Meeting Summarization](https://dl.acm.org/doi/10.1145/3279981.3279987)|GIFT18|
|[Meeting Extracts for Discussion Summarization Based on Multimodal Nonverbal Information](https://dl.acm.org/doi/10.1145/2993148.2993160)|ICMI16|
|[Extractive Summarization of Meeting Recordings](https://pdfs.semanticscholar.org/6159/506bdd368fff24dd12e5c6ed91ba05b44f9e.pdf)||
| [Multimodal Summarization of Meeting Recordings](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.862.6509&rep=rep1&type=pdf)|ICME03|

### Open Domain
| Paper | Conference |
| :---: | :---: |
|[Multi-View Sequence-to-Sequence Models with Conversational Structure for Abstractive Dialogue Summarization](https://arxiv.org/abs/2010.01672)|EMNLP20|
|[SAMSum Corpus: A Human-annotated Dialogue Dataset for Abstractive Summarization](https://arxiv.org/abs/1911.12237)|EMNLP19|
|[Making Sense of Group Chat through Collaborative Tagging and Summarization](https://homes.cs.washington.edu/~axz/papers/cscw_tilda.pdf)|CSCW18|
|[Collabot: Personalized Group Chat Summarization](https://dl.acm.org/doi/10.1145/3159652.3160588)|WSDM18|

### Customer Service
| Paper | Conference |
| :---: | :---: |
| [Automatic Dialogue Summary Generation for Customer Service](https://dl.acm.org/doi/10.1145/3292500.3330683) |KDD19|

### Email
| Paper | Conference |
| :---: | :---: |
|[Building a Dataset for Summarization and Keyword Extraction from Emails](http://www.lrec-conf.org/proceedings/lrec2014/pdf/1037_Paper.pdf)||
|[Summarizing Online Conversations A Machine Learning Approach](http://web2py.iiit.ac.in/research_centres/publications/download/inproceedings.pdf.8b32440f2dc771c4.323031325f414e445f43616d6572612e706466.pdf)|2010|
|[Task-focused Summarization of Email](https://www.aclweb.org/anthology/W04-1008.pdf)|2004|

### News Review
| Paper | Conference |
| :---: | :---: |
|[The SENSEI Annotated Corpus: Human Summaries of Reader Comment Conversations in On-line News](https://www.aclweb.org/anthology/W16-3605/)|SIGDIAL16|

### Others
| Paper | Conference | Highlights |
| :---: | :---: | :---: |
|[文本摘要:浓缩的才是精华](https://dl.ccf.org.cn/institude/institudeDetail?id=5011489004210176&_ack=1)|||
|[Unsupervised Abstractive Dialogue Summarization for Tete-a-Tetes](https://arxiv.org/abs/2009.06851)|||
|[Storytelling with Dialogue: A Critical Role Dungeons and Dragons Dataset](https://www.aclweb.org/anthology/2020.acl-main.459/)|ACL20|
| [Legal Summarization for Multi-role Debate Dialogue via Controversy Focus Mining and Multi-task Learning](https://dl.acm.org/doi/10.1145/3357384.3357940)|CIKM19|
| [Abstractive Dialog Summarization with Semantic Scaffolds](https://openreview.net/forum?id=B1eibJrtwr) ||
|[Creating a reference data set for the summarization of discussion forum threads](https://link.springer.com/article/10.1007/s10579-017-9389-4)||
|[Summarizing Dialogic Arguments from Social Media](https://arxiv.org/abs/1711.00092)|SemDial 2017|
| [Dial2Desc: End-to-end Dialogue Description Generation](https://arxiv.org/pdf/1811.00185.pdf) | |
|[Using Summarization to Discover Argument Facets in Online Idealogical Dialog](https://www.aclweb.org/anthology/N15-1046.pdf)|NAACL15|
|[Conversation summarization using machine learning and scoring method](http://www.pluto.ai.kyutech.ac.jp/~shimada/paper/pacling2013.pdf)||
|[Plans Toward Automated Chat Summarization](https://www.aclweb.org/anthology/W11-0501/)|ACL11|
|[Domain Adaptation to Summarize Human Conversations](https://www.aclweb.org/anthology/W10-2603/)|ACL2010 workshop|
|[Automatic Text Summarization for Dialogue Style](https://www.semanticscholar.org/paper/Automatic-Text-Summarization-for-Dialogue-Style-Liu-Wang/3b7339228ee4d8dcfc3dcea6f23832659bf0a440)||
|[Adapting Lexical Chaining to Summarize Conversational Dialogues](https://www.semanticscholar.org/paper/Adapting-Lexical-Chaining-to-Summarize-Dialogues-Gurevych-Nahnsen/36f1bc82cc1d814cf5ec9bb8eab6856258e88ab3)||
|[Semantic Similarity Applied to Spoken Dialogue Summarization](https://www.aclweb.org/anthology/C04-1110/)|COLING04||
</p></details>

## Graph-Based
<details><summary>papers</summary><p>

| Paper | Conference |
| :---: | :---: |
|[Enhancing Extractive Text Summarization with Topic-Aware Graph Neural Networks](https://arxiv.org/abs/2010.06253)|COLING20|
|[Heterogeneous Graph Neural Networks for Extractive Document Summarization](https://arxiv.org/abs/2004.12393)|ACL20|
|[Structured Neural Summarization](https://arxiv.org/abs/1811.01824)|ICLR19|
| [Hierarchical Transformers for Multi-Document Summarization](https://arxiv.org/abs/1905.13164) | ACL19 |
| [Learning to Create Sentence Semantic Relation Graphs for Multi-Document Summarization](https://arxiv.org/abs/1909.12231) | EMNLP19 |
|[Graph-based Neural Multi-Document Summarization](https://www.aclweb.org/anthology/K17-1045/)|CoNLL17|
|[Abstractive Document Summarization with a Graph-Based Attentional Neural Model](https://www.aclweb.org/anthology/P17-1108/)|ACL17|
</p></details>


## Multi-Document
<details><summary>papers</summary><p>

| Paper | Conference |
| :---: | :---: |
|[Multi-document Summarization with Maximal Marginal Relevance-guided Reinforcement Learning](https://arxiv.org/abs/2010.00117)|EMNLP20|
|[Multi-Granularity Interaction Network for Extractive and Abstractive Multi-Document Summarization](https://www.aclweb.org/anthology/2020.acl-main.556/)|ACL2020|
|[SUPERT: Towards New Frontiers in Unsupervised Evaluation Metrics for Multi-Document Summarization](https://arxiv.org/abs/2005.03724)|ACL20||
|[Leveraging Graph to Improve Abstractive Multi-Document Summarization](https://arxiv.org/abs/2005.10043)|ACL20|
|[Generating Representative Headlines for News Stories](https://arxiv.org/abs/2001.09386)|WWW20|
| [Learning to Create Sentence Semantic Relation Graphs for Multi-Document Summarization](https://arxiv.org/abs/1909.12231) | EMNLP19 |
| [Improving the Similarity Measure of Determinantal Point Processes for Extractive Multi-Document Summarization](https://arxiv.org/abs/1906.00072)|ACL19|
| [Hierarchical Transformers for Multi-Document Summarization](https://arxiv.org/abs/1905.13164) | ACL19 |
| [MeanSum: A Neural Model for Unsupervised Multi-Document Abstractive Summarization](https://arxiv.org/abs/1810.05739)|ICML19|
| [Generating Wikipedia By Summarizing Long Sequence](https://arxiv.org/abs/1801.10198) | ICLR18 |
| [Adapting the Neural Encoder-Decoder Framework from Single to Multi-Document Summarization](https://www.aclweb.org/anthology/D18-1446/)|EMNLP18|
| [Graph-based Neural Multi-Document Summarization](https://www.aclweb.org/anthology/K17-1045/)|CoNLL17|
| [Improving Multi-Document Summarization via Text Classification](https://arxiv.org/abs/1611.09238) | AAAI17|
| [An Unsupervised Multi-Document Summarization Framework Based on Neural Document Model](https://www.aclweb.org/anthology/C16-1143/) | COLING16 |
| [Event-Centric Summary Generation](https://www.microsoft.com/en-us/research/publication/event-centric-summary-generation/)| ACL04 |
</p></details>


## Cross-Lingual
<details><summary>papers</summary><p>

| Paper | Conference |
| :---: | :---: |
|[Multi-Task Learning for Cross-Lingual Abstractive Summarization](https://arxiv.org/abs/2010.07503)||
|[WikiLingua- A New Benchmark Dataset for Cross-Lingual Abstractive Summarization](https://arxiv.org/abs/2010.03093)|Findings of EMNLP20|
|[A Deep Reinforced Model for Zero-Shot Cross-Lingual Summarization with Bilingual Semantic Similarity Rewards](https://www.aclweb.org/anthology/2020.ngt-1.7/)|ACL20 workshop|
|[Jointly Learning to Align and Summarize for Neural Cross-Lingual Summarization](https://www.aclweb.org/anthology/2020.acl-main.554.pdf)|ACL20|
|[Attend, Translate and Summarize:An Efficient Method for Neural Cross-Lingual Summarization](https://www.aclweb.org/anthology/2020.acl-main.121.pdf)|ACL20|
|[MultiSumm: Towards a Unified Model for Multi-Lingual Abstractive Summarization](https://aaai.org/Papers/AAAI/2020GB/AAAI-CaoY.7050.pdf)|AAAI20|
| [Global Voices: Crossing Borders in Automatic News Summarization](https://arxiv.org/abs/1910.00421) | EMNLP19 |
| [NCLS: Neural Cross-Lingual Summarization](https://arxiv.org/abs/1909.00156) | EMNLP19|
| [Zero-Shot Cross-Lingual Abstractive Sentence Summarization through Teaching Generation and Attention](https://www.aclweb.org/anthology/P19-1305/) | ACL19 |
| [A Robust Abstractive System for Cross-Lingual Summarization](https://www.aclweb.org/anthology/N19-1204/)|NAACL19|
|[Cross-Lingual Korean Speech-to-Text Summarization](https://link.springer.com/chapter/10.1007/978-3-030-14799-0_17)|ACIIDS19|
|[Cross-language document summarization via extraction and ranking of multiple summaries](https://link.springer.com/article/10.1007/s10115-018-1152-7)||
| [Zero-Shot Cross-Lingual Neural Headline Generation](https://dl.acm.org/doi/10.1109/TASLP.2018.2842432)|IEEE/ACM TRANSACTIONS 18|
|[Cross-Language Text Summarization using Sentence and Multi-Sentence Compression](https://hal.archives-ouvertes.fr/hal-01779465/document)|NLDB18|
|[Cross-language document summarization based on machine translation quality prediction](https://www.aclweb.org/anthology/P10-1094/)|ACL10|
|[Using bilingual information for cross-language document summarization](https://www.aclweb.org/anthology/P11-1155.pdf)|ACL11|
|[Phrase-based Compressive Cross-Language Summarization](https://www.aclweb.org/anthology/D15-1012.pdf)|ACL15|
|[Abstractive Cross-Language Summarization via Translation Model Enhanced Predicate Argument Structure Fusing](http://www.nlpr.ia.ac.cn/cip/ZhangPublications/zhang-taslp-2016.pdf)|IEEE/ACM Trans16|
|[Multilingual Single-Document Summarization with MUSE](https://www.aclweb.org/anthology/W13-3111/)|MultiLing13|
</p></details>

## Unsupervised
<details><summary>papers</summary><p>

| Paper | Conference |
| :---: | :---: |
|[ Q-learning with Language Model for Edit-based Unsupervised Summarization](https://arxiv.org/abs/2010.04379)|EMNLP20|
| [Abstractive Document Summarization without Parallel Data](https://arxiv.org/abs/1907.12951) | LREC20|
| [Unsupervised Neural Single-Document Summarization of Reviews via Learning Latent Discourse Structure and its Ranking](https://arxiv.org/abs/1906.05691) | ACL19 |
|[Sentence Centrality Revisited for Unsupervised Summarization](https://www.aclweb.org/anthology/P19-1628/)|ACL19|
|[Discrete Optimization for Unsupervised Sentence Summarization with Word-Level Extraction](https://arxiv.org/abs/2005.01791)|ACL20|
| [MeanSum : A Neural Model for Unsupervised Multi-Document Abstractive Summarization](https://arxiv.org/abs/1810.05739)|ICML19|
| [SEQ3: Differentiable Sequence-to-Sequence-to-Sequence Autoencoder for Unsupervised Abstractive Sentence Compression](https://arxiv.org/abs/1904.03651)|NAACL19|
|[Learning to Encode Text as Human-Readable Summaries usingGenerative Adversarial Networks](https://www.aclweb.org/anthology/D18-1451/)|EMNLP18|
|[Unsupervised Abstractive Meeting Summarization with Multi-Sentence Compression and Budgeted Submodular Maximization](https://arxiv.org/abs/1805.05271)|ACL18|
</p></details>

## Multi-modal
<details><summary>papers</summary><p>

| Paper | Conference |
| :---: | :---: |
|[VMSMO: Learning to Generate Multimodal Summary for Video-based News Articles](https://arxiv.org/abs/2010.05406)|EMNLP20|[Data](https://github.com/yingtaomj/VMSMO)|
|[Multi-modal Summarization for Video-containing Documents](https://arxiv.org/abs/2009.08018)||
|[Text-Image-Video Summary Generation Using Joint Integer Linear Programming](https://link.springer.com/chapter/10.1007/978-3-030-45442-5_24)|ECIR20|
|[Aspect-Aware Multimodal Summarization for Chinese E-Commerce Products](https://aaai.org/ojs/index.php/AAAI/article/view/6332/6188)|AAAI20|
|[Convolutional Hierarchical Attention Network for Query-Focused Video Summarization](https://arxiv.org/abs/2002.03740)|AAAI20|
|[Multimodal Summarization with Guidance of Multimodal Reference](https://aaai.org/ojs/index.php/AAAI/article/view/6525/6381)|AAAI20|
|[EmotionCues: Emotion-Oriented Visual Summarization of Classroom Videos](https://ieeexplore.ieee.org/document/8948010)|IEEE20|
|[A Survey on Automatic Summarization Using Multi-Modal Summarization System for Asynchronous Collections](http://www.ijirset.com/upload/2019/february/4_shilpa_IEEE.pdf)||
|[Extractive summarization of documents with images based on multi-modal RNN](https://research.aston.ac.uk/en/publications/extractive-summarization-of-documents-with-images-based-on-multi-)||
|[Keep Meeting Summaries on Topic: Abstractive Multi-Modal Meeting Summarization](https://www.aclweb.org/anthology/P19-1210/)|ACL19|
|[Multimodal Abstractive Summarization for How2 Videos](https://www.aclweb.org/anthology/P19-1659/) | ACL19 |
|[MSMO: Multimodal Summarization with Multimodal Output](https://www.aclweb.org/anthology/D18-1448/)|EMNLP18|
|[Abstractive Text-Image Summarization Using Multi-Modal Attentional Hierarchical RNN](https://www.aclweb.org/anthology/D18-1438/)|EMNLP18|
|[Multi-modal Sentence Summarization with Modality Attention and Image Filtering](https://www.ijcai.org/Proceedings/2018/0577.pdf) | IJCAI18 |
|[How2: A Large-scale Dataset for Multimodal Language Understanding](https://arxiv.org/abs/1811.00347)|NIPS18|
|[Multimodal Abstractive Summarization for Open-Domain Videos](https://nips2018vigil.github.io/static/papers/accepted/8.pdf) | NIPS18|
|[Read, Watch, Listen, and Summarize: Multi-Modal Summarization for Asynchronous Text, Image, Audio and Video](https://ieeexplore.ieee.org/document/8387512)|IEEE18|
|[Fusing Verbal and Nonverbal Information for Extractive Meeting Summarization](https://dl.acm.org/doi/10.1145/3279981.3279987)|GIFT18|
|[Multi-modal Summarization for Asynchronous Collection of Text, Image, Audio and Video](https://www.aclweb.org/anthology/D17-1114/) | EMNLP17 |
|[Meeting Extracts for Discussion Summarization Based on Multimodal Nonverbal Information](https://dl.acm.org/doi/10.1145/2993148.2993160)|ICMI16|
|[Summarizing a multimodal set of documents in a Smart Room](https://www.aclweb.org/anthology/L12-1524/)|LREC12|
|[Multi-modal summarization of key events and top players in sports tournament videos](https://eprints.qut.edu.au/43479/1/WACV_266_%281%29.pdf)|2011 IEEE Workshop on Applications of Computer Vision|
|[Multimodal Summarization of Complex Sentences](https://www.cs.cmu.edu/~jbigham/pubs/pdfs/2011/multimodal_summarization.pdf)||
|[Summarization of Multimodal Information](http://www.lrec-conf.org/proceedings/lrec2004/pdf/502.pdf)|LREC04|
| [Multimodal Summarization of Meeting Recordings](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.862.6509&rep=rep1&type=pdf)|ICME 03|
</p></details>


## Concept-map-based
<details><summary>papers</summary><p>

| Paper | Conference |
| :---: | :---: |
| [Fast Concept Mention Grouping for Concept Map–based Multi-Document Summarization](https://www.aclweb.org/anthology/N19-1074/)|NAACL19|
| [Bringing Structure into Summaries : Crowdsourcing a Benchmark Corpus of Concept Maps](https://www.aclweb.org/anthology/D17-1320/) | EMNLP17 |
</p></details>

## Timeline
<details><summary>papers</summary><p>

| Paper | Conference |
| :---: | :---: |
|[Examining the State-of-the-Art in News Timeline Summarization](https://arxiv.org/abs/2005.10107)|ACL20|
|[Learning towards Abstractive Timeline Summarization](https://www.ijcai.org/Proceedings/2019/0686.pdf)|IJCAI19|
</p></details>

## Opinion
<details><summary>papers</summary><p>

| Paper | Conference |
| :---: | :---: |
|[Few-Shot Learning for Opinion Summarization](https://arxiv.org/abs/2004.14884)|EMNLP20|
|[Unsupervised Opinion Summarization as Copycat-Review Generation](https://arxiv.org/abs/1911.02247)|ACL20|
|[Unsupervised Opinion Summarization with Noising and Denoising](https://arxiv.org/abs/2004.10150)|ACL20|
|[OPINIONDIGEST: A Simple Framework for Opinion Summarization](https://arxiv.org/abs/2005.01901)|ACL20 Short|
|[Weakly-Supervised Opinion Summarization by Leveraging External Information](https://arxiv.org/abs/1911.09844)|AAAI20|
| [MeanSum : A Neural Model for Unsupervised Multi-Document Abstractive Summarization](https://arxiv.org/abs/1810.05739)|ICML19
</p></details>

## Reinforcement Learning
<details><summary>papers</summary><p>

| Paper | Conference |
| :---: | :---: |
| [Answers Unite! Unsupervised Metrics for Reinforced Summarization Models](https://arxiv.org/abs/1909.01610)|EMNLP19|
| [Deep Reinforcement Learning with Distributional Semantic Rewards for Abstractive Summarization](https://arxiv.org/abs/1909.00141)|EMNLP19|
| [Reinforced Extractive Summarization with Question-Focused Rewards](https://www.aclweb.org/anthology/P18-3015/)|ACL18|
| [Fast Abstractive Summarization with Reinforce-Selected Sentence Rewriting](https://arxiv.org/abs/1805.11080)|ACL18|
| [Multi-Reward Reinforced Summarization with Saliency and Entailmen](https://www.aclweb.org/anthology/N18-2102/)t|NAACL18|
| [Deep Communicating Agents for Abstractive Summarization](https://arxiv.org/abs/1803.10357) | NAACL18 |
| [Ranking Sentences for Extractive Summarization with Reinforcement Learning](https://www.aclweb.org/anthology/N18-1158/)|NAACL18|
| [A Deep Reinforced Model For Abstractive Summarization](https://arxiv.org/abs/1705.04304)|ICLR18|
</p></details>

## Reward Learning
<details><summary>papers</summary><p>

| Paper | Conference |
| :---: | :---: |
|[Learning to summarize from human feedback](https://arxiv.org/abs/2009.01325)||
|[Better Rewards Yield Better Summaries: Learning to Summarise Without References](https://arxiv.org/abs/1909.01214)|EMNLP19|
</p></details>

## Evaluation
<details><summary>papers</summary><p>

| Paper | Conference | Highlights |
| :---: | :---: | :---: |
|[Unsupervised Reference-Free Summary Quality Evaluation via Contrastive Learning](https://arxiv.org/abs/2010.01781)|EMNLP20|
|[SacreROUGE: An Open-Source Library for Using and Developing Summarization Evaluation Metrics](https://arxiv.org/abs/2007.05374)||https://github.com/danieldeutsch/sacrerouge|
|[SummEval: Re-evaluating Summarization Evaluation](https://arxiv.org/abs/2007.12626)||https://github.com/Yale-LILY/SummEval|
[HIGHRES: Highlight-based Reference-less Evaluation of Summarization](https://arxiv.org/abs/1906.01361)| ACL19 |

</p></details>


## Controlled
<details><summary>papers</summary><p>

| Paper | Conference |
| :---: | :---: |
|[Summarizing Text on Any Aspects: A Knowledge-Informed Weakly-Supervised Approach](https://arxiv.org/abs/2010.06792)|EMNLP20 Short|
| [Length-controllable Abstractive Summarization by Guiding with Summary Prototype](https://arxiv.org/abs/2001.07331)|
|[Positional Encoding to Control Output Sequence Length](https://www.aclweb.org/anthology/N19-1401/)|NAACL19|
|[Query Focused Abstractive Summarization: Incorporating Query Relevance, Multi-Document Coverage, and Summary Length Constraints into seq2seq Models](https://arxiv.org/abs/1801.07704)|
| [Controllable Abstractive Summarization](https://arxiv.org/abs/1711.05217)|ACL2018 Workshop|
|[Controlling Length in Abstractive Summarization Using a Convolutional Neural Network](https://www.aclweb.org/anthology/D18-1444/)|EMNLP18|
|[Controlling Output Length in Neural Encoder-Decoders](https://www.aclweb.org/anthology/D16-1140/)|EMNLP16|
</p></details>

## Analysis
<details><summary>papers</summary><p>

| Paper | Conference |
| :---: | :---: |
|[Understanding Neural Abstractive Summarization Models via Uncertainty](https://arxiv.org/abs/2010.07882)|EMNLP20 Short|
|[Re-evaluating Evaluation in Text Summarization](https://arxiv.org/abs/2010.07100)|EMNLP20|
|[CDEvalSumm: An Empirical Study of Cross-Dataset Evaluation for Neural Summarization Systems](https://arxiv.org/abs/2010.05139)|EMNLP20||
|[What Have We Achieved on Text Summarization?](https://arxiv.org/abs/2010.04529)|EMNLP20|
|[Conditional Neural Generation using Sub-Aspect Functions for Extractive News Summarization](https://arxiv.org/abs/2004.13983)|Findings of EMNLP2020||
|[Extractive Summarization as Text Matching](https://arxiv.org/abs/2004.08795)|ACL20|
|[Neural Text Summarization: A Critical Evaluation](https://www.aclweb.org/anthology/D19-1051/)|EMNLP19|
|[Earlier Isn’t Always Better:Sub-aspect Analysis on Corpus and System Biases in Summarization](https://arxiv.org/abs/1908.11723)|EMNLP19|
|[A Closer Look at Data Bias in Neural Extractive Summarization Models](https://arxiv.org/abs/1909.13705)|EMNLP 2019 Workshop|
|[Countering the Effects of Lead Bias in News Summarization via Multi-Stage Training and Auxiliary Losses](https://arxiv.org/abs/1909.04028)|EMNLP19 Short|
|[Searching for Effective Neural Extractive Summarization: What Works and What's Next](https://arxiv.org/abs/1907.03491)|ACL19|
|[Content Selection in Deep Learning Models of Summarization](https://www.aclweb.org/anthology/D18-1208/)|EMNLP18|
</p></details>

## Theory
<details><summary>papers</summary><p>

| Paper | Conference |
| :---: | :---: |
|[KLearn: Background Knowledge Inference from Summarization Data](https://arxiv.org/abs/2010.06213)|Findings of EMNLP|
|[A Simple Theoretical Model of Importance for Summarization](https://www.aclweb.org/anthology/P19-1101/)|ACL19|
|[BottleSum: Unsupervised and Self-supervised Sentence Summarization using the Information Bottleneck Principle](https://arxiv.org/abs/1909.07405)|EMNLP19|
</p></details>

## Extractive
<details><summary>papers</summary><p>

| Paper | Conference |
| :---: | :---: |
|[Summarize, Outline, and Elaborate: Long-Text Generation via Hierarchical Supervision from Extractive Summaries](https://arxiv.org/abs/2010.07074)||
|[SupMMD: A Sentence Importance Model for Extractive Summarization using Maximum Mean Discrepancy](https://arxiv.org/abs/2010.02568)||
|[Stepwise Extractive Summarization and Planning with Structured Transformers](https://arxiv.org/abs/2010.02744)|EMNLP20|
|[A Discourse-Aware Neural Extractive Model for Text Summarization](http://www.cs.utexas.edu/~jcxu/material/ACL20/DiscoBERT_ACL2020.pdf)|ACL20|
|[Reading Like HER: Human Reading Inspired Extractive Summarization](https://www.aclweb.org/anthology/D19-1300/)|EMNLP19|
| [Extractive Summarization with SWAP-NET: Sentences and Words from Alternating Pointer Networks](https://www.aclweb.org/anthology/P18-1014/)|ACL18|
| [Neural Document Summarization by Jointly Learning to Score and Select Sentences](https://www.aclweb.org/anthology/P18-1061/)|ACL18|
| [Neural Latent Extractive Document Summarization](https://www.aclweb.org/anthology/D18-1088/)|ACL18|
|[Generative Adversarial Network for Abstractive Text Summarization](https://arxiv.org/abs/1711.09357)|AAAI18|
|[Improving Neural Abstractive Document Summarization with Explicit Information Selection Modeling](https://www.aclweb.org/anthology/D18-1205/)|EMNLP18|
| [Extractive Summarization Using Multi-Task Learning with Document Classification](https://www.aclweb.org/anthology/D17-1223/)|EMNLP17|
| [SummaRuNNer: A Recurrent Neural Network based Sequence Model for Extractive Summarization of Documents](https://arxiv.org/abs/1611.04230)|AAAI17|
| [Text Summarization through Entailment-based Minimum Vertex Cover](https://www.aclweb.org/anthology/S14-1010/)|ENLG13|
</p></details>

## Abstractive
<details><summary>papers</summary><p>

| Paper | Conference |
| :---: | :---: |
|[Multi-hop Inference for Question-driven Summarization](https://arxiv.org/abs/2010.03738)|EMNLP20|
|[Quantitative Argument Summarization and Beyond-Cross-Domain Key Point Analysis](https://arxiv.org/abs/2010.05369)|EMNLP20|
|[Learning to Fuse Sentences with Transformers for Summarization](https://arxiv.org/abs/2010.03726)|EMNLP20 short|
|[AutoSurvey: Automatic Survey Generation based on a Research Draft](https://www.ijcai.org/Proceedings/2020/0761.pdf)|IJCAI20|
|[Neural Abstractive Summarization with Structural Attention](https://arxiv.org/abs/2004.09739)|IJCAI20|
|[A Unified Model for Financial Event Classification, Detection and Summarization](https://www.ijcai.org/Proceedings/2020/644)|IJCAI20|
|[Keywords-Guided Abstractive Sentence Summarization](https://aaai.org/Papers/AAAI/2020GB/AAAI-LiH.1493.pdf)|AAAI20|
|[Discriminative Adversarial Search for Abstractive Summarization](https://arxiv.org/abs/2002.10375)|ICML20|
|[Controlling the Amount of Verbatim Copying in Abstractive Summarization](https://arxiv.org/abs/1911.10390)|AAAI20|
|[GRET：Global Representation Enhanced Transformer](https://arxiv.org/abs/2002.10101)|AAAI20 |
|[Abstractive Summarization of Spoken and Written Instructions with BERT](https://arxiv.org/abs/2008.09676)|KDD Converse 2020|
|[DeepChannel: Salience Estimation by Contrastive Learning for Extractive Document Summarization](https://arxiv.org/abs/1811.02394)|AAAI19|
|[Concept Pointer Network for Abstractive Summarization](https://www.aclweb.org/anthology/D19-1304.pdf)|EMNLP19|
|[Co-opNet: Cooperative Generator–Discriminator Networks for Abstractive Summarization with Narrative Flow](https://arxiv.org/abs/1907.01272)||
|[Contrastive Attention Mechanism for Abstractive Sentence Summarization](https://www.aclweb.org/anthology/D19-1301/)|EMNLP19|
|[An Entity-Driven Framework for Abstractive Summarization](https://arxiv.org/abs/1909.02059)|EMNLP19|
|[Abstract Text Summarization: A Low Resource Challenge](https://www.aclweb.org/anthology/D19-1616/)|EMNLP19|
|[Attention Optimization for Abstractive Document Summarization](https://arxiv.org/abs/1910.11491)|EMNLP19|
|[BiSET: Bi-directional Selective Encoding with Template for Abstractive Summarization](https://www.aclweb.org/anthology/P19-1207/)|ACL19|
|[Scoring Sentence Singletons and Pairs for Abstractive Summarization](https://www.aclweb.org/anthology/P19-1209/)|ACL19|
| [Inducing Document Structure for Aspect-based Summarization](https://www.aclweb.org/anthology/P19-1630/)|ACL19|
|[Generating Summaries with Topic Templates and Structured Convolutional Decoders](https://arxiv.org/abs/1906.04687)|ACL19|
|[Improving Abstractive Text Summarization with History Aggregation](https://arxiv.org/abs/1912.11046)||
|[Summary Refinement through Denoising](https://arxiv.org/abs/1907.10873)|RANLP19|
| [Closed-Book Training to Improve Summarization Encoder Memory](https://arxiv.org/abs/1809.04585)|EMNLP18|
| [Bottom-Up Abstractive Summarization](https://arxiv.org/abs/1808.10792)|EMNLP18|
| [A Unified Model for Extractive and Abstractive Summarization using Inconsistency Loss](https://www.aclweb.org/anthology/P18-1013/)|ACL18|
| [Soft Layer-Specific Multi-Task Summarization with Entailment and Question Generation](https://www.aclweb.org/anthology/P18-1064/)|ACL18|
| [Retrieve, Rerank and Rewrite: Soft Template Based Neural Summarization](https://www.aclweb.org/anthology/P18-1015/)|ACL18|
|[Abstractive Document Summarization via Bidirectional Decoder](https://link.springer.com/chapter/10.1007/978-3-030-05090-0_31)|ADMA18|
| [Guiding Generation for Abstractive Text Summarization based on Key Information Guide Network](https://www.aclweb.org/anthology/N18-2009/)|NAACL18|
| [Entity Commonsense Representation for Neural Abstractive Summarization](https://www.aclweb.org/anthology/N18-1064/) | NAACL18|
| [Get To The Point: Summarization with Pointer-Generator Networks](https://arxiv.org/abs/1704.04368)|ACL17|
|[Selective Encoding for Abstractive Sentence Summarization](https://arxiv.org/abs/1704.07073)|ACL17|
| [Abstractive Document Summarization with a Graph-Based Attentional Neural Model](https://www.aclweb.org/anthology/P17-1108/)|ACL17|
|[Deep Recurrent Generative Decoder for Abstractive Text Summarization](https://www.aclweb.org/anthology/D17-1222/) |EMNL17|
|[A Cascade Approach to Neural Abstractive Summarization with Content Selection and Fusion](https://arxiv.org/abs/2010.03722)|AACL20 short|
|[Improving Neural Abstractive Document Summarization with Structural Regularization](https://www.aclweb.org/anthology/D18-1441/)|EMNLP18|
|[Toward Abstractive Summarization Using Semantic Representations](https://www.aclweb.org/anthology/N15-1114/)|NAACL15|
|[Abstractive Meeting Summarization with Entailment and Fusion](https://www.aclweb.org/anthology/W13-2117/)|ENLG13|
</p></details>

## Extractive-Abstractive
<details><summary>papers</summary><p>

| Paper | Conference |
| :---: | :---: |
|[On Extractive and Abstractive Neural Document Summarization with Transformer Language Models](https://arxiv.org/abs/1909.03186)|EMNLP20|
| [Jointly Extracting and Compressing Documents with Summary State Representations](https://arxiv.org/abs/1904.02020)|NAACL19|
</p></details>

## Syntactic
<details><summary>papers</summary><p>

| Paper | Conference |
| :---: | :---: |
|[Compressive Summarization with Plausibility and Salience Modeling](https://arxiv.org/abs/2010.07886)|EMNLP20|
|[StructSum: Incorporating Latent and Explicit Sentence Dependencies for Single Document Summarization](https://arxiv.org/abs/2003.00576)||
|[Joint Parsing and Generation for Abstractive Summarization](https://arxiv.org/abs/1911.10389)|AAAI20|
|[Neural Extractive Text Summarization with Syntactic Compression](https://arxiv.org/abs/1902.00863)|EMNLP19|
|[Single Document Summarization as Tree Induction](https://www.aclweb.org/anthology/N19-1173/)|NAACL19|
</p></details>

## QA Related
<details><summary>papers</summary><p>

| Paper | Conference |
| :---: | :---: |
|[Towards Question-Answering as an Automatic Metric for Evaluating the Content Quality of a Summary](https://arxiv.org/abs/2010.00490)||
|[Guiding Extractive Summarization with Question-Answering Rewards](https://arxiv.org/abs/1904.02321)|NAACL19|
|[A Semantic QA-Based Approach for Text Summarization Evaluation](https://arxiv.org/abs/1704.06259)|AAAI18|
</p></details>

## Toolkit
<details><summary>papers</summary><p>

* [openNMT](https://github.com/OpenNMT/OpenNMT-py)
* [fairseq](https://github.com/pytorch/fairseq)
* [LeafNATS](https://www.aclweb.org/anthology/N19-4012/)
* [TransformerSum](https://github.com/HHousen/TransformerSum)
</p></details>



