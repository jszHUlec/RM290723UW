print("przyklad break/continue. Program nie wyswietla '3' a na 9 konczy petle.")
for x in range(10):
    if x == 3:
        continue
    if x == 9:
        break
    print(x)


print("przyklad petli while nieskonczonej zatrzymywanej instrukcja break")
print("petla wykorzystuje 'continue' do pominiecia kroku gdy 'counter' == 2")
counter = 0
while True:  # Boolean: True albo False 1==1 -> True
    counter += 1
    if counter == 2:
        continue
    if counter == 5:
        break



