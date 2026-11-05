N = int(input("entrer un entier N supérieur à zéro:"))
for table in range (1, N+1):
    for multiplicateur in range (1,11):
        print (f"{table} X {multiplicateur} ={table*multiplicateur}")

