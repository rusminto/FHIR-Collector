/opt/hadoop/bin/hadoop com.sun.tools.javac.Main Grouping.java
jar cf wc.jar Grouping*.class

rm -r output
/opt/hadoop/bin/hadoop jar wc.jar Grouping input output
