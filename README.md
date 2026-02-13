# 📊 CSL7110 - Big Data Assignment 1

## 🧑‍💻 Student Information
- **Course:** CSL7110 - Big Data Systems  
- **Assignment:** Assignment 1  
- **Name:** <Your Name>  
- **Roll Number:** <Your Roll Number>  

---

# 🚀 Project Overview

This assignment demonstrates practical implementation of:

- Hadoop MapReduce (WordCount)
- HDFS file operations
- Performance analysis using input split sizes
- Apache Spark for large-scale data processing
- Metadata extraction using Regex
- TF-IDF feature engineering
- Author influence network construction

The dataset used is `200.txt` from Project Gutenberg.

---

# 🗂️ Repository Structure

```
.
├── WordCount.java
├── spark_assignment.py
├── 200.txt
├── README.md
```

---

# 🐘 Hadoop Section

## ✅ WordCount Implementation

The Hadoop MapReduce program performs word frequency counting using:

- **Mapper Input:** `(LongWritable, Text)`
- **Mapper Output:** `(Text, IntWritable)`
- **Reducer Output:** `(Text, IntWritable)`

### Execution Command

```bash
hadoop jar WordCount.jar WordCount /200.txt /output
```

---

## 📁 HDFS Commands Used

```bash
hdfs dfs -mkdir /input
hdfs dfs -put 200.txt /input
hdfs dfs -ls /
```

---

## 📊 Split Size Performance Analysis

The experiment was conducted using three different split sizes:

| Split Size | Execution Time |
|------------|----------------|
| 32 MB      | 13162 ms       |
| 64 MB      | 12108 ms       |
| 128 MB     | 13095 ms       |

### Observation

- Smaller splits increase task scheduling overhead.
- Larger splits reduce parallelism.
- In a single-node cluster, performance differences are minimal.

---

# ⚡ Apache Spark Section

## 🔎 Q10 – Metadata Extraction

Metadata fields extracted using Regex:

- Title
- Release Date
- Language
- Encoding

Regex example:

```python
regexp_extract("text", r"Title:\s*(.*)", 1)
```

### Challenges

- Inconsistent formatting
- Missing metadata fields
- Variations in text structure

---

## 📈 Q11 – TF-IDF Computation

### Steps:

1. Tokenization
2. Stop-word removal
3. Term Frequency (TF)
4. Inverse Document Frequency (IDF)
5. TF-IDF feature vector generation

### Formula

TF-IDF = TF × IDF

Cosine Similarity:

similarity = (A · B) / (|A||B|)

TF-IDF highlights important words while reducing the weight of common terms.

---

## 🌐 Q12 – Author Influence Network

Authors are treated as nodes in a graph.

Edges are generated using Spark DataFrame joins.

Due to limited metadata in the dataset, a simplified author representation was used to demonstrate graph construction.

Output format:

```
(author1, author2)
```

---

# 🛠️ Technologies Used

- Java
- Hadoop 3.x
- HDFS
- Apache Spark 4.x
- PySpark
- macOS

---

# ▶️ How to Run

## Hadoop

```bash
javac -classpath `hadoop classpath` -d . WordCount.java
jar -cvf WordCount.jar *
hdfs dfs -rm -r /output
hadoop jar WordCount.jar WordCount /200.txt /output
```

## Spark

```bash
spark-submit spark_assignment.py
```

---

# 📌 Key Learnings

- Distributed processing using MapReduce
- HDFS storage management
- Performance tuning using split size
- Large-scale text processing using Spark
- Feature engineering using TF-IDF
- Graph modeling using DataFrame joins

---

# 📎 GitHub Submission Note

All code, execution steps, and analysis are included in this repository.  
The repository is public for evaluation purposes.

---

# ⭐ Final Status

✔ Hadoop Completed  
✔ Spark Completed  
✔ Performance Analysis Completed  
✔ Metadata Extraction Completed  
✔ Network Construction Completed  

---

**Assignment 1 Completed Successfully ✅**
