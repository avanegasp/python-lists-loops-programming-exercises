mix = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

# Your code below
def numMix(mix):
    for item in mix:
        print(type(item))

numMix(mix)