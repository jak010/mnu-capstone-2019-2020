lines_seen = set() # holds lines already seen
outfile = open("2020-04-21_1432r.txt", "w")
for line in open("2020-04-21_1432.txt", "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
