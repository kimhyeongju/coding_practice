f = open("test2.txt", "wt", encoding='utf8')
f.write("""Machine learning (ML) is the study of computer algorithms that 
improve automatically through experience.
It is seen as a subset of artificial intelligence.
Machine learning algorithms build a model based on sample data, known as "training data",
in order to make predictions or decisions without being explicitly programmed to do so.
Machine learning algorithms are used in a wide variety of applications, such as email filtering and computer vision,
where it is difficult or unfeasible to develop conventional algorithms to perform the needed tasks.
""")

f.close()