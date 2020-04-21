from pathlib import Path
import fileinput

def text_diff(file_a, file_b, file_c):
    with open(file_a) as fin_a:
        lines_in_a = set(line.strip() for line in fin_a)
    with open(file_b) as fin_b:
        fout_c = open(file_c,"w")
        for line in fin_b:
            if line.strip() not in lines_in_a:
                fout_c.writelines(line.strip()+'\n') 
        fout_c.close() 

#call the function
text_diff("2020-04-21_1418r.txt", "2020-04-21_1432r.txt",  "out.txt")

