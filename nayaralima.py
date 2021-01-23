dados=input()
Lakewood=[]
Bridgewood=[]
Ridgewood=[]
dias=[]
status, data1, data2, data3 = dados.split(" ",3)
dias.extend((data1,data2,data3))
if status == "Regular:" :
    for element in dias:
        if ( "sat" in element or "sun" in element):
            Lakewood.append(90)
            Bridgewood.append(60)
            Ridgewood.append(150)
        else:
            Lakewood.append(110)
            Bridgewood.append(160)
            Ridgewood.append(220)
else:
    for element in dias:
        if ( "sat" in element or "sun" in element):
            Lakewood.append(80)
            Bridgewood.append(50)
            Ridgewood.append(40)
        else:
            Lakewood.append(50)
            Bridgewood.append(110)
            Ridgewood.append(100)

L=sum(Lakewood)
B=sum(Bridgewood)
R=sum(Ridgewood)
if B==L and B<R:
    print("Brigewood")
if B==R and B<L:
    print("Ridgewood")
if L==R and L<B:
    print("Ridgewood")
if L<B and L<R:
    print("Lakewood")
else:
    if B<L and B<R:
        print("Bridgewood")
    else:
        if R<L and R<B:
            print("Ridgewood")
