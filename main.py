import sys


def boyer_moore(string, pattern):
    state = 1
    delta = compute_delta(pattern)
    result = []

    for i in range(1, len(string)):
        letteridx = find_letter(string[i])
        state = delta[state+1][letteridx]

        if state == len(pattern):
            result.append(i-(len(pattern)-1))
    return result


def find_letter(letter):
    alphabet = list(map(chr, range(ord('A'), ord('Z') + 1)))
    for i in range(0, len(alphabet)):
        if alphabet[i] == letter:
            return i+1


def print_delta(delta):
    for i in range(0, len(delta)):
        print(delta[i])
        print()


def compute_delta(pattern):
    # -------Constructia matricei delta ------ #
    alphabet = list(map(chr, range(ord('A'), ord('Z') + 1)))

    patt = ['e']
    for i in range(1, len(pattern) + 1):
        patt.append(pattern[0:i])

    delta = [[0 for k in range(len(alphabet) + 1)] for j in range(len(patt) + 1)]
    for i in range(1, len(alphabet)+1):
        delta[0][i] = alphabet[i-1]
        for j in range(1, len(patt) + 1):
            delta[j][0] = patt[j-1]

    # ------- Completarea matricei ------- #

    state = 0
    for char in range(1, len(alphabet)+1):
        if delta[0][char] == patt[1]:
            state += 1
            delta[1][char] = state

    i = 2
    for pat in (range(2, len(pattern)+2)):
        cnt = 0
        for letter in alphabet:
            aux_patt = delta[pat][0] + letter
            aux_len = len(aux_patt)
            pa = pattern
            p = slice(0, aux_len)
            if pa[p] == aux_patt:
                state += 1
                delta[i][cnt + 1] = state
            else:
                minus = 0
                no = 1
                while no == 1:
                    if minus == len(aux_patt):
                        break
                    w = slice(minus, len(aux_patt))
                    for cmp in range(1 ,len(patt)):
                        if aux_patt[w] == patt[cmp]:
                            new_state = len(aux_patt[w])
                            delta[i][cnt + 1] = new_state
                            no = 0
                    minus += 1
            cnt += 1
        i += 1
    return delta


if __name__ == '__main__':
    input = sys.argv[1]
    output = sys.argv[2]
    f = open(input, "r")

    pattern = f.readline()
    string = f.readline()
    indices = boyer_moore(string[:-1], pattern[:-1])

    w = open(output, "w")
    for i in range(len(indices)):
        w.write(str(indices[i]))
        w.write(" ")
    w.write("\n")
    w.close()
