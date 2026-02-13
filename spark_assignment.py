from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_extract, length, avg, count

spark = SparkSession.builder.appName("Assignment1").getOrCreate()

books_df = spark.read.text("200.txt").withColumnRenamed("value", "text")
books_df = books_df.withColumn("file_name", books_df.text)

books_df = books_df.withColumn(
    "title",
    regexp_extract("text", r"Title:\s*(.*)", 1)
).withColumn(
    "release_date",
    regexp_extract("text", r"Release Date:\s*(.*)", 1)
).withColumn(
    "language",
    regexp_extract("text", r"Language:\s*(.*)", 1)
).withColumn(
    "encoding",
    regexp_extract("text", r"Character set encoding:\s*(.*)", 1)
)

books_df.filter(
    (books_df.title != "") |
    (books_df.release_date != "") |
    (books_df.language != "") |
    (books_df.encoding != "")
).show(10, False)

#Q11

from pyspark.ml.feature import Tokenizer, StopWordsRemover, HashingTF, IDF

tokenizer = Tokenizer(inputCol="text", outputCol="words")
wordsData = tokenizer.transform(books_df)

remover = StopWordsRemover(inputCol="words", outputCol="filtered")
filteredData = remover.transform(wordsData)

hashingTF = HashingTF(
    inputCol="filtered",
    outputCol="rawFeatures",
    numFeatures=1000
)

featurizedData = hashingTF.transform(filteredData)

idf = IDF(inputCol="rawFeatures", outputCol="features")
idfModel = idf.fit(featurizedData)

tfidfData = idfModel.transform(featurizedData)

print("===== TF-IDF FEATURES =====")
tfidfData.select("features").show(5, False)

#Q12

from pyspark.sql.functions import col, lit

books_df = books_df.withColumn("author", lit("Project_Gutenberg_Author"))

a = books_df.alias("a")
b = books_df.alias("b")

edges = a.join(b)

print("===== AUTHOR INFLUENCE SAMPLE =====")

edges.select(
    col("a.author").alias("author1"),
    col("b.author").alias("author2")
).show(10, False)


