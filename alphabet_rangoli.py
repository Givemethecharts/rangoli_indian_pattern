def print_rangoli(size):
    start_letter = 97
    end_letter = start_letter + size - 1
    start_letter_counter = end_letter - 1
    our_list = []
    our_counter = (size - 1) * 2
    our_splitter = '-'
    second_end = end_letter
    counter = 1
    while counter < size:
        for number in range(our_counter):
            our_list.append(our_splitter)
        for letter in range(end_letter, start_letter_counter, - 1):
            if letter == end_letter:
                our_list.append(chr(letter))
            else:
                our_list.append(our_splitter)
                our_list.append(chr(letter))
        if counter != 1:
            for second_letter in range(second_end, end_letter + 1,):
                our_list.append(our_splitter)
                our_list.append(chr(second_letter))
            second_end -= 1
        for number in range(our_counter):
            our_list.append(our_splitter)
        print("".join(our_list))
        counter += 1
        our_counter -= 2
        our_list = []
        start_letter_counter -= 1

    while size > 0:
        for number in range(our_counter):
            our_list.append(our_splitter)
        for letter in range(end_letter, start_letter - 1, -1):
            if letter != start_letter:
                our_list.append(chr(letter))
                our_list.append(our_splitter)
            else:
                our_list.append(chr(letter))
        for reverse_letter in range(start_letter + 1, end_letter + 1):
            our_list.append(our_splitter)
            our_list.append(chr(reverse_letter))
        for number in range(our_counter):
            our_list.append(our_splitter)
        print("".join(our_list))
        our_list = []
        size -= 1
        start_letter += 1
        our_counter += 2


n = int(input())
print_rangoli(n)