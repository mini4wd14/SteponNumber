def steponNumber(a):
    hasil = []  #list kosong untuk menampung hasil
    for i in range(len(a)): #loop sebanyak "paket" 
        awal = 0    #awal deretnya, yang saya pakai hanya deret ketika x = y, untuk deret sebelahnya tinggal di + 2
        for j in range(1,a[i][1]+1):    #loop sebanyak y dimulai dari 1, karena jika dimulai dari 0, tidak bisa di cek genapnya dan deret menjadi salah
            if j%2 == 0:    #ketika iterasi (n) genap, awal + 3
                awal += 3
            else:   #ketika iterasi (n) ganjil, awal +1
                awal += 1
        if a[i][0] == a[i][1]:  #jika x = y
            hasil.append(awal)  #masukan hasil deret linear
        elif a[i][0] == a[i][1] + 2:    #jika x = 2 + y
            awal += 2   #deret linear x = y ditambahkan 2
            hasil.append(awal)
        else:   #jika inputan selain x = y atau x = y + 2 dinyatakan "No Number"
            hasil.append('No Number')
    return hasil
            
print(steponNumber([[4,2],[6,6],[3,4]]))
print(steponNumber([[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]])) #cek deret linear x = y
print(steponNumber([[2,0],[3,1],[4,2],[5,3],[6,4],[7,5],[8,6]])) #cek deret linear x = y + 2
print(steponNumber([[1,0],[2,1],[3,2],[4,3],[5,4],[6,5],[7,6]])) #cek deret linear x = y + 1 (No Number)

