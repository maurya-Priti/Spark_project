FROM apache/spark
USER talentum
WORKDIR /app
COPY tips_spark_project.py /app
RUN sudo chmod 754 tips_spark_project.py
CMD ["/opt/spark/bin/spark-submit", "tips_spark_project.py"]