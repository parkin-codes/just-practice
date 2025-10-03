def flatten(data):
    output = []
    for item in data:
        if type(item) == list:
            output.extend(flatten(item))
        else:
            output.append(item)
    return output

example = [[1,2,3],[4,[[5,6]]],7,8,[9,10]]
print("원본 :",example)
print("평탄화 :",flatten(example))