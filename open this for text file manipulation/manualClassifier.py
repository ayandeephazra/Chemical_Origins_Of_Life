positives = 0
negatives = 0
i = 1
tn = 0
tp = 0
fn = 0
fp = 0
flag = 0
flag2 = 0
totalRawCount = 0
flag5 = 0
with open("file1.txt", "r", encoding="cp1252") as file:
    for line in file:

        # print(line)
        words = line.split()
        if len(words) > 0:
            # totalRawCount = totalRawCount + 1

            if words[0] == "input:":
                totalRawCount = totalRawCount + 1

                print(totalRawCount, words)
                if flag5 == 0:
                    a = totalRawCount
                flag5 = 1

                if float(words[len(words) - 1]) > 0.5:
                    positives = positives + 1
                    str = " ".join(words[1:len(words) - 2])

                    flag = 0
                    if str.find("bulk moduli") != -1 or str.find("bulk modulus") != -1 or str.find(
                            "K 0") != -1 or str.find("K0") != -1 or str.find("B=") != -1 or str.find("B =") != -1:
                        flag = 1
                        # tp = tp + 1

                    if flag == 1 and (
                            str.find("GPa") != -1 or str.find("range of") != -1 or str.find("ranges of") != -1):
                        tp = tp + 1

                    # printing the positive sentences
                    # print(i, " ".join(words[1:len(words) - 3]))
                    i = i + 1


                else:
                    negatives = negatives + 1
                    str = " ".join(words[1:len(words) - 2])
                    flag2 = 0
                    if str.find("bulk moduli") != -1 or str.find("bulk modulus") != -1 or str.find("K 0") != -1 \
                            or str.find("K0") != -1 or str.find("B=") != -1 or str.find("B =") != -1:
                        flag2 = 1
                        # fn = fn + 1

                    if flag2 == 1 and str.find("GPa") != -1:
                        fn = fn + 1

                string = " ".join(words[1:len(words) - 3])

print(positives)
print(negatives)
fp = positives - tp
tn = negatives - fn
print("tn:", tn)
print("tp:", tp)
print("fp:", fp)
print("fn:", fn)

recall = tp / (tp + fn)
precision = tp / (tp + fp)

print("recall: ", recall)
print("precision: ", precision)
print("F score:", 2*precision*recall/(precision+recall))
print(totalRawCount)
