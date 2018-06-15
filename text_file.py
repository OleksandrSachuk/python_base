fw = open('sample.txt', 'w')
fw.write('Test message-1\n')
fw.write('Test message-2\n')
fw.close()

fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close
