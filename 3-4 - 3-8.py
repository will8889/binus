#3-4.
print("3-4")
guest_list = ["kuntil_anak", "pocong", "genderuwo"]
print(guest_list)

for i in range(3):
    print(guest_list[i] + " have been invited")
#3-5.
print("3-5")
print("kuntil_anak can't come")

del guest_list[0]
guest_list.insert(0, "tuyul")
print(guest_list)

for i in range(3):
    print(guest_list[i] + " have been invited")


#3-6.
print("3-6")
print("We have found a bigger dinner table")

guest_list.insert(0, "suster_ngesot")
guest_list.insert(1, "nenek_gayung")
guest_list.append("valak")

for i in range(6):
    print(guest_list[i] + " have been invited")

#3-7.
print("3-7")
print("only two who survived will come to the dinner")

print(guest_list.pop() + " are dead")
print(guest_list.pop() + " are dead")
print(guest_list.pop() + " are dead")
print(guest_list.pop() + " are dead")

print(guest_list[0] + " invited to the dinner")
print(guest_list[1] + " invited to the dinner")

del guest_list


#3-8.
print("3-8")
tempat = ["Surga", "Eropa", "Madagaskar", "Konoha", "Detroit"]
print(tempat)
print(sorted(tempat))
print(sorted(tempat,reverse=True))
tempat.reverse()
print(tempat)
tempat.reverse()
print(tempat)
print(sorted(tempat))
print(sorted(tempat,reverse=True))