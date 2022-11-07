import sys

def process_file(fileName):
    input_file = open(fileName, "r")
    result_list = []
    for idx, line in enumerate(input_file):
        line = line.rstrip('\n')
        if idx == 0:
            content = line + ',합계,평균'
            result_list.append(content)
            continue
        else:
            name, kor, eng, math = line.split(',')
            sum = float(kor) + float(eng) + float(math)
            avg = sum / 3
            content = line + ',' + str(sum) + ',' + str(avg)
            print(content)
            result_list.append(content)
    input_file.close()

    print(result_list)
    output_file = open('output.csv', "wt")

    for line in result_list:
        output_file.write(line + '\n')

    output_file.close()


if __name__ == "__main__":
        # process_file(sys.argv[1])
    process_file('input.csv')