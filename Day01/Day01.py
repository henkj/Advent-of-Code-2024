from collections import Counter

def part(input):
    ll, rl = [], []

    with open(input) as f:
        for line in f.readlines():
            x, y = [int(s) for s in line.split()]
            ll.append(x)
            rl.append(y)

    ll.sort()
    rl.sort()

    # part 1
    print(sum(abs(ll[i]-rl[i]) for i in range(len(ll))))

    # part 2
    c = Counter(rl)
    print(sum(ll[i]*c[ll[i]] for i in range(len(ll))))
                
part('Day01/input/input.txt')
