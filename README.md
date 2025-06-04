# 🧮 MMTU: A Massive Multimodal Tabular Understanding Benchmark 

## 📚 Citation

Our paper has been accepted to **ICML 2025**. If you find our work useful, please cite:

```bibtex
@inproceedings{jiang2025compositional,
  title={Compositional Condition Question Answering in Tabular Understanding},
  author={Jun-Peng Jiang and
          Tao Zhou and
          De-Chuan Zhan and
          Han-Jia Ye},
  booktitle={Forty-second International Conference on Machine Learning},
  year={2025}
}
```


## 📖 MMTU
There are several existing tabular understanding benchmarks (e.g., WikiTableQuestions, TabFact, FinaQA, and ComTQA) for MLLMs, but they have some limitations: 
1. **Narrow Domain.** FinaQA focuses primarily on simplecalculations within the financial domain, TabFact assesses the truthfulness of content, and WTQ addresses basic questions answering. 
2. **Uncertainty of Table Images.** Except ComTQA, other benchmarks do not provide table images. Since the method for converting data into table format can vary, this leads to potential biases in the evaluation results. 
3. **Lack of Systematic Evaluation.** All existing benchmarks group similar QA tasks together without systematically evaluating specific capabilities, such as understanding  individual cells, interpreting specific rows or columns, handling compositional conditions, and assessing reasoning and calculation abilities.

To address these challenges, we introduce **MMTU** in this repository,, which is the abbreviation of Massive Multimodal Tabular Understanding Benchmark. We classify the questions into 4 categories: 
- **Understanding individual elements (IE):** This refers to the task of understanding and extracting specific cell values within a table, such as identifying the value at a particular row and column intersection. For example, ”What is Student A’s math score?”
- **Interpreting rows and columns (RC):** This involves comprehending specific samples or attributes within a table, i.e., comprehending tasks involving a specific column or row. For instance, ”Which course does Student A have the highest score in?” or ”Which student has the best math score?
- **Comprehending compositional conditions (CC):** This pertains to understanding table content that satisfies compositional conditions. Examples include, ”What is the math score of the student with the highest total score?” or ”Among the top three students in total score, how many have an ‘A’ in physical education?”
- **Performing calculations or reasoning (CR):** This refers to performing basic calculations or logical reasoning on specific cell values within a table. For example, ”How much higher is the total score of the top student compared to the lowest-scoring student?”

We collect Tables from WTQ, TabFact and NAT-QA creating four QA task types across over ten domains and yielding 8921 QA pairs. To ensure quality, GPT-4 generated questions, LLMs and human experts validated answers, retaining consistent pairs and resolving discrepancies, as shown in the following figure.The JSON files of questions can be found in the [data](https://github.com/LAMDA-Tabular/MMTU/tree/main/data) folder, and the images of tables can be found in the [huggingface](https://huggingface.co/datasets/LAMDA-Tabular/MMTU/tree/main).
<p align="center">
<img src="./resources/filter.png"  width="70%">
</p>

### 📜 MMTU-tiny
We also provide a tiny version of MMTU for a quicker and more convenient analysis. We select 60 QA pairs for each category from raw WTQ datasets. We use this tiny dataset for analysis in section 3.2 in our paper. The JSON files of questions can be found in the [huggingface](https://huggingface.co/datasets/LAMDA-Tabular/MMTU-tiny/tree/main). The raw format (csv, html) of images can be found in the [github](https://github.com/ppasupat/WikiTableQuestions). You can use the code provided in the [StructuredTables2Images](https://github.com/LAMDA-Tabular/MMTU/tree/main/StructuredTables2Images) to convert the raw format to the image format.


## 📏 StructuredTables2Images
During the extensive table collection process, which involved gathering tables from diverse and complex sources such as **HTML** web pages, **CSV** datasets, **Markdown** documents, and **LaTeX** academic papers, we observed an extremely wide variety of table formats. **HTML** tables might have dynamic features and different styling, while **CSV** files rely on simple delimiters without formatting. **Markdown** tables usually have a straightforward structure but may vary in how they handle complex alignments. **LaTeX** tables, on the other hand, can include advanced mathematical notations and complex table hierarchies. To standardize these highly heterogeneous table formats into a consistent and uniform image format, we provide an elaborate unified pipeline. This pipeline is carefully designed to convert tables from these various formats into **PNG** images, which are well - suited for downstream processing tasks. The downstream processing includes tasks such as automated table understanding algorithms that require consistent visual input, as well as evaluation where the visual representation of the table is crucial for accurate assessment. The implementation can be found in the [StructuredTables2Images](https://github.com/LAMDA-Tabular/MMTU/tree/main/StructuredTables2Images) module, which contains the detailed code to carry out this complex conversion process efficiently and accurately.
## 🔧 Continual Fixing

- Some Results and Visualizations are under preparation. 
- We will upload our training and test code soon.

## 🤗 Contact

If there are any questions, please feel free to propose new features by opening an issue or contact the author: **Jun-Peng Jiang** ([jiangjp@lamda.nju.edu.cn](mailto:jiangjp@lamda.nju.edu.cn)) and **Tao Zhou** ([zhout@lamda.nju.edu.cn](mailto:zhout@lamda.nju.edu.cn)). Enjoy the benchmark.
