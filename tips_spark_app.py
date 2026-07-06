
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Pyspark Lab exam").enableHiveSupport().getOrCreate()
sc = spark.sparkContext


from pyspark.sql.types import * 
tips_schema = StructType([
    StructField('total_bill', DoubleType(), False),
    StructField('tip', DoubleType(), False),
    StructField('gender', StringType(), False),
    StructField('smoker', StringType(), False),
    StructField('day', StringType(), False),
    StructField('time', StringType(), False),
    StructField('size', IntegerType(), False),
    StructField('price_per_person', DoubleType(), False),
    StructField('Payer_Name', StringType(), False)
])



#a.) Solution
filepath = 'file:///home/talentum/shared/Q1/tips.csv'
tips_df = spark.read.format('csv').load(filepath, schema = tips_schema,header = True)


print("First 10 records of tips dataset") 
print(tips_df.show(10))


#b.) Solution
import pyspark.sql.functions as F
tips_df = tips_df.withColumn('tip_percentage', F.expr("(tip/total_bill)*100"))

print(tips_df.show(10))

tips_df.createOrReplaceTempView("tips")

tips_view = spark.sql("SELECT * FROM tips")
tips_view.show()


avg_total_bill = tips_view.groupBy('day').avg('total_bill')
avg_total_bill.show()



max_tip_by_gender = tips_view.groupBy('gender').max('tip')
max_tip_by_gender.show()


from pyspark.sql.functions import col


# filtering the record using filter() 
#result_df = tips_view.filter("tip > 20")

tip_gt_20 = tips_view.where(col("tip_percentage") > 20)

tip_gt_20.show()
