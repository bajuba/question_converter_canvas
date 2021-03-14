infile = open("input.txt",'r')
outfile = open('output.txt','w')
count = 3
for line in infile:
  out_line = '''0{0}. Question {0}
###
multiblank~1
###\n'''.format(count)
  count = count+1
  in_line = line.split(" ")
  #print(in_line)
  for word in in_line:
    #print(word)
    word = word.strip()
    if word[0] == "[":
      answer = word[1:-1]
      answer = "1~"+answer+"~"+answer+"s"
      out_line += "[1] "
    else:
      out_line += word+" "
  out_line = out_line[:-1]+"\n###\n"+answer+"\n###\n###\n"
  print(out_line)
  outfile.write(out_line)
outfile.close()