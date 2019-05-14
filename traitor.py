gen_1 = ["", "", "", "", "", ""]
gen_2 = ["", "", "", "", "", ""]
gen_3 = ["", "", "", "", "", ""]


def showArrays():
    print("{}\n{}\n{}\n".format(gen_1, gen_2, gen_3))


def updateGeneral_1_Array(pos, general, value):
    gen_1[pos] = general
    gen_1[pos + 1] = value


def updateGeneral_2_Array(pos, general, value):
    gen_2[pos] = general
    gen_2[pos + 1] = value


def updateGeneral_3_Array(pos, general, value):
    gen_3[pos] = general
    gen_3[pos + 1] = value


def checkGeneral_1(k):
    if (gen_1[k] == gen_1[k + 2]) and (gen_1[k] == gen_1[k + 4]):
        # print("General 1 : \t{}\t{}\t{}".format(gen_1[k], gen_1[k+2], gen_1[k+4]))
        return "No Traitor"
    elif (gen_1[k] == gen_1[k + 2]) and (gen_1[k] != gen_1[k + 4]):
        # print("General 3 is the Traitor")
        # print("General 1 : \t{}\t{}\t{}".format(gen_1[k], gen_1[k + 2], gen_1[k + 4]))
        return "General 3"
    elif (gen_1[k] != gen_1[k + 2]) and (gen_1[k] == gen_1[k + 4]):
        # print("General 2 is the Traitor")
        #  print("General 1 : \t{}\t{}\t{}".format(gen_1[k], gen_1[k + 2], gen_1[k + 4]))
        return "General 2"


def checkGeneral_2(k):
    if (gen_2[k] == gen_2[k + 2]) and (gen_2[k] == gen_2[k + 4]):
        # print("General 2 : \t{}\t{}\t{}".format(gen_2[k], gen_2[k + 2], gen_2[k + 4]))
        return "No Traitor"
    elif (gen_2[k] == gen_2[k + 2]) and (gen_2[k] != gen_2[k + 4]):
        # print("General 2 : \t{}\t{}\t{}".format(gen_2[k], gen_2[k + 2], gen_2[k + 4]))
        # print("General 3 is the Traitor")
        return "General 3"
    elif (gen_2[k] != gen_2[k + 2]) and (gen_2[k] == gen_2[k + 4]):
        # print("General 2 : \t{}\t{}\t{}".format(gen_2[k], gen_2[k + 2], gen_2[k + 4]))
        # print("General 1 is the Traitor")
        return "General 1"


def checkGeneral_3(k):
    if (gen_3[k] == gen_3[k + 2]) and (gen_3[k] == gen_3[k + 4]):
        # print("General 3 : \t{}\t{}\t{}".format(gen_3[k], gen_3[k + 2], gen_3[k + 4]))
        return "No Traitor"
    elif (gen_3[k] == gen_3[k + 2]) and (gen_3[k] != gen_3[k + 4]):
        # print("General 3 is the Traitor")
        # print("General 3 : \t{}\t{}\t{}".format(gen_3[k], gen_3[k + 2], gen_3[k + 4]))
        return "General 2"
    elif (gen_3[k] != gen_3[k + 2]) and (gen_3[k] == gen_3[k + 4]):
        # print("General 1 is the Traitor")
        # print("General 3 : \t{}\t{}\t{}".format(gen_3[k], gen_3[k + 2], gen_3[k + 4]))
        return "General 1"


def revealTraitor():
    if (not gen_1[len(gen_1)-1] == "") and (not gen_2[len(gen_2)-1] == "") and (not gen_3[len(gen_3)-1] == ""):
        i = 1
        # print("Commander Order : {}\t{}\t{}\t".format(gen_1[i], gen_2[i], gen_3[i]))
        if (gen_1[i] != gen_2[i]) and (gen_1[i] != gen_3[i]) and (gen_2[i] != gen_3[i]):
            print("The Commander-in-chief is the traitor !")
            return
        elif (gen_1[i] == gen_2[i]) and (gen_1[i] == gen_3[i]) and (gen_2[i] == gen_3[i]):
            g1 = checkGeneral_1(i)
            g2 = checkGeneral_2(i)
            g3 = checkGeneral_3(i)

            # print("G1 : {}\nG2 : {}\nG3 : {}".format(g1, g2, g3))

            if (g1 == g2) and (g1 == g3) and (g2 == g3):
                print("None of the Generals is Traitor")
            elif g1 == g2:
                print("General 3 is the Traitor")
            elif g1 == g3:
                print("General 2 is the Traitor")
            elif g2 == g3:
                print("General 1 is the Traitor")
            else:
                print("This problem can not be resolved, there must be only 1 Traitor if there are 4 Generals")
