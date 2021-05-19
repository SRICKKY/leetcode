from pprint import pprint

def powerSet(xs):
    result = [[]]

    for x in xs:
        newSubset = [subset + [x] for subset in result]
        print("newSubset => ", newSubset)
        result.extend(newSubset)
        print("result => ", result)

    # return result


# print(powerSet([1, 2, 3]))
pprint(powerSet([1, 2, 3, 4]))
# print(powerSet([1, 2, 6]))
