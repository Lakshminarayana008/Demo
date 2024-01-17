def count_words(line):
    word_count = {}
    words = line.split()

    for word in words:
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


file=open("input.txt","r")
lines =file.readlines()


output_lines = []
for line in lines:
    output_lines.append(line.strip())
    word_count = count_words(line)
    for word, count in word_count.items():
        output_lines.append(f"{word}: {count}")


for output_line in output_lines:
    print(output_line)


output_file=open("output.txt","w")
output_file.write("\n".join(output_lines))
