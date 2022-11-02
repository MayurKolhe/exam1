

g = {70314: {'name': 'Anna Kendrick', 'homework': [77, 83, 100], 'laboratory': [85, 78]}, 90919: {'name': 'Rebel Wilson', 'homework': [51, 60, 96], 'laboratory': [92, 87]}, 72457: {'name': 'Brittany Snow', 'homework': [97, 81, 73], 'laboratory': [67, 100]}, 55331: {'name': 'Hailee Steinfeld', 'homework': [63, 67, 62], 'laboratory': [100, 98]}, 52392: {'name': 'Hana Mae Lee', 'homework': [95, 100, 73], 'laboratory': [97, 74]}, 65087: {'name': 'Skylar Astin', 'homework': [61, 89, 87], 'laboratory': [100, 97]}, 91523: {'name': 'Adam DeVine', 'homework': [99, 94, 89], 'laboratory': [69, 91]}}

print("                                                                              Total")
print("                         |-------HOMEWORK-------|    |---LABORATORY---|    Weighted")
print("Name              ID        H1    H2    H3   Havg       L1    L2   Lavg     Average")
print("================= =====  ===== ===== =====  =====    ===== =====  =====    ========")
for i in g:
    sid = i
    name = g[sid]['name']
    h1 = g[sid]['homework'][0]
    h2 = g[sid]['homework'][1]
    h3 = g[sid]['homework'][2]
    x = 0
    l1 = g[sid]['laboratory'][0]
    l2 = g[sid]['laboratory'][1]
    y = 0
    z = 0
    print(f'{name:18}{sid:5}{h1:7}{h2:6}{h3:6}{x:7.1f}{l1:9}{l2:6}{y:7.1f}{z:12.1f}')
print("                         ===== ===== =====  =====    ===== =====  =====    ========")
a1 = 0
a2 = 0
a3 = 0
b = 0
c1 = 0
c2 = 0
d = 0
e = 0
print(f'{"     Classroom Averages:":18}{a1:6.1f}{a2:6.1f}{a3:6.1f}{b:7.1f}{c1:9.1f}{c2:6.1f}{d:7.1f}{e:12.1f}')
print()
