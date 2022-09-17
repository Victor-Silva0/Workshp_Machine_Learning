# Databricks notebook source
from sklearn import tree
from sklearn import model_selection
from sklearn import linear_model
from sklearn import ensemble
from sklearn import metrics

import mlflow

# COMMAND ----------

df = spark.table("sandbox_apoiadores.abt_dota_pre_match_new").toPandas()

# COMMAND ----------

model = mlflow.sklearn.load_model("models:/fatec_dota/production")

predict = model.predict(df[df.columns[2:]])
predict
