""" with open('text.txt', 'r') as f:

    size_to_read = 10
    f_contents = f.read(size_to_read)
    
    while len(f_contents) > 0:
        print(f_contents, end='*')
        f_contents = f.read(size_to_read)
 """

with open('text.txt', 'r') as rf:
    with open('textcopy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)