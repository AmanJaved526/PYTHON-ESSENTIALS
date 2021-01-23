# REMOVE EMPTY LIST FROM THE LIST
l = []
while True:
    n = input("Enter data in list:")
    l.append(n)
    l.append([])
    key_input = input("press '+' to continue or '=' to stop")
    if(key_input == '+'):
        continue
    elif(key_input == '='):
        break
    else:
        print("invalid key")

print(l)

print("updated list:")
l1 = [i for i in l if i!=[] and i!='']

print(l1)


# REMOVE ALL THE DUPLICATE WORDS FROM THE SENTENCE
str1 = input("Enter a sentence:")
l = str1.split()
k = []

for i in l:
    if(str1.count(i)>1 and (i not in k) or str1.count(i) == 1):
        k.append(i)

print(' '.join(k))


#COUNT THE OCCURENCE OF A CHARACTER IN THE GIVEN STRING
sentence = input("Enter a  sentence:")
count_input = input("Enter the letter to count for the occurence in the sentence:")
print("total count of input letter:",sentence.count(count_input))