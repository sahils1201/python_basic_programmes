str1=str(input("Enter a string-"))
str2=str(input("Enter a string-"))
uncommon_words=[]

uncommon_words.extend(word for word in str1 if word not in str2)
uncommon_words.extend(word for word in str2 if word not in str1)

print(uncommon_words)