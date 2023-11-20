les_dict = {}
with open("subjects.txt", "r", encoding='utf-8') as file:
    for line in file:
        line = line.split(":")
        sub = line[0]
        les = line[1].split()
        total_les = 0
        for lesson in les:
            if '(' in lesson:
                lesson = lesson.split("(")[0]
            total_les += int(lesson)
        les_dict[sub] = total_les

print(les_dict)
