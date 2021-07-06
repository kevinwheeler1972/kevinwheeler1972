def process_scores():
    total=0
    count = 0
    grades=0
    grades_array = []   
    while True: 
        print("Enter grades ")
        grades = int(input()) 
        if grades<0: 
            break
        else:
            grades_array.append(grades)
            count = count +1
    return grades_array, count


def printMax(grades):
    maxValue = grades[0]
    for x in grades:
        if maxValue<x:
            maxValue = x
    print("Maximum value is",maxValue)


def printMin(grades):
    minValue = grades[0]
    for x in grades:
        if minValue>x:
            minValue = x
    print("Minimum value is",minValue)

def sort(grades):
    grades.sort()
    return grades


def get_total(grades):
    total=0
    for grade in grades:
        total += grade
    return total

def get_average(total, count):
    average = total / count
    return average


def display_result(average):
    print("average " + str(average))
    return average


def main():
    grades,count= process_scores()
    total = get_total(grades)
    average = get_average(total, count)
    display_result(average)
    printMax(grades)
    printMin(grades)
    printSort(grades)
main()