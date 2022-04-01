
word_file = "data/words.txt"

def read_words():
  words = []
  f = open(word_file, "r")
  for line in f:
    words.append(line.strip())
  f.close()
  return words

def main():
  words = read_words()
  while True:
    w = input("Enter a word> ")
    w = w.strip()
    if w == "":
      break
    if w in words:
      print("%s is a word" % w)
    else:
      print("Spelling error: %s is not a word!" % w)

main()



a = "A,B,C,D,E"

a.replace("BC", "32")

a = a.strip().split(",")

a = "*".join(a)

print(a)

dict1 = {"0" : 1234 , 0 : "a string" , 2 : 0, 1234 : "0"}