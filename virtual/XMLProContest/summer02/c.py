s = input()
onkai = "WBWBWWBWBWBW"
onkai_list = [onkai]
for i in range(11):
    onkai = onkai[1:] + onkai[0]
    if onkai[0] == "W":
        onkai_list.append(onkai)

oto = ["Do", "Re", "Mi", "Fa", "So", "La", "Si"]
for i in range(len(onkai_list)):
    if s[:12] == onkai_list[i]:
        print(oto[i])
        break
