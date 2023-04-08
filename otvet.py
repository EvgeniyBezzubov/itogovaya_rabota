lst_1 = ["hello","2", "world", ":-)"]
lst_2 = ["1234","1567", "-2", "compuhter service"]
lst_3 = ["Russia","Denmark", "Kazan"]
ans = []
for i in lst_1,lst_2,lst_3:
    for y in i:
        if len(y)<=3:
            ans.append(y)
    print(i, ">>>", ans)
    ans = []
