# DouBan_BookStars

# 导出剔除重复项的sql


SELECT distinct title,stars,conments_Num FROM DouBan_BookStars.java_book into outfile "/home/lk/DouBan_BookStars/java_book.xls" ;


SELECT distinct title,stars,conments_Num FROM DouBan_BookStars.shell_book into outfile "/home/g/DouBan_BookStars/shell_book.xls" ;
