class Solution:
    # @param A : list of strings
    # @param B : integer
    # @return a list of strings
    def fullJustify(self, A, B):
        # import pdb
        # pdb.set_trace()
        returnList = []
        temp_list = []
        space_occupied = 0
        no_of_spaces = 0
        
        i = 0
        while (i < len(A)):
            word = A[i]
            space_occupied += len(word)
            if space_occupied + no_of_spaces <= B:
                temp_list.append(word)
                no_of_spaces += 1
                i += 1
                if i == len(A):
                    if len(temp_list) != 1:
                        new_sentence = ' '.join(temp_list[:-1])
                        new_sentence += ' ' + temp_list[-1]
                        new_sentence += ' ' * (B - len(new_sentence))
                    else:
                        new_sentence = temp_list[0]
                        new_sentence += ' ' * (B - len(new_sentence))
                    returnList.append(new_sentence)
            else:
                space_occupied -= len(word)
                if len(temp_list) == 1:
                    new_sentence = temp_list[0]
                    new_sentence += ' ' * (B - len(new_sentence))
                else:
                    remaining_spaces = B - space_occupied
                    space_per_word = remaining_spaces / (len(temp_list) - 1)
                    remaining_spaces = remaining_spaces % (len(temp_list) - 1)
                    new_sentence = ''
                    for temp_word in temp_list[:-1]:
                        if remaining_spaces != 0:
                            new_sentence += temp_word + (' ' * (space_per_word + 1))
                            remaining_spaces -= 1
                        else:
                            new_sentence += temp_word + (' ' * space_per_word)
                    new_sentence += temp_list[-1]
                    new_sentence += ' ' * remaining_spaces
                returnList.append(new_sentence)
                temp_list = []
                space_occupied = 0
                no_of_spaces = 0
        return returnList

# A = [ "tv", "izln", "dkq", "ypbbix", "k", "xoojn", "xju", "xfe", "aysz", "agkfhvtqkt", "rsklvgn", "kedzohp", "lqzz", "hivu", "gtxrjj", "nz", "ysoatq", "n", "ote", "xuctw", "vlvgmfzm", "zlpmp", "oe", "kayhyihc", "yvsllceili", "osqkjjvydc", "p", "zxqrgyvnic", "ebxhww", "pyjdlt", "ruwl", "lnlt", "ddzf", "jicwez", "mcrj", "unbej", "on", "thivo", "sbzxsxvm", "jj", "lacb", "qfsopsmeq", "ial", "tifiuf", "uybh", "pcbufc", "nccdldzs", "pbsofijlmp", "ehdcxkgbi", "wu", "gvnzmw", "czonuzrls", "blg", "y", "qbdgiwboi", "wpeupcwz", "fxnbh", "sybikok", "ukuztzdqk", "oowhjnhol", "s", "kvmtoutvf", "ilh", "q", "tclbqcdbz", "oglfrq", "cwtucyecf", "am", "kflhesgk", "xnxpogj", "nx", "hwfb", "htmf", "xawcimlx", "hhivdgf", "uk", "evtsczh" ]
# B = 483

A = [ "am", "fasgoprn", "lvqsrjylg", "rzuslwan", "xlaui", "tnzegzuzn", "kuiwdc", "fofjkkkm", "ssqjig", "tcmejefj", "uixgzm", "lyuxeaxsg", "iqiyip", "msv", "uurcazjc", "earsrvrq", "qlq", "lxrtzkjpg", "jkxymjus", "mvornwza", "zty", "q", "nsecqphjy" ]
B = 14

sol = Solution()
returnList = sol.fullJustify(A,B)
for word in returnList:
    print word, '#'