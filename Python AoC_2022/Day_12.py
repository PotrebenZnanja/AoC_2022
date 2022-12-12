from collections import defaultdict

inp=[]
while(True):
    g = input()
    if g=="":
        break
    inp.append(g)

grid = [list(it) for it in inp]
sx, sy = 0, 0
ex, ey = 0, 0

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for y, row in enumerate(grid): #preveri 2D in iterira cez vrstice, y je od 0 do height
    for x, char in enumerate(row): # preveri 1D in iteriraj po stolpcih, x je od 0 do width
        if char == 'S':
            sx, sy = x, y
        if char == 'E':
            ex, ey = x, y

grid[sy][sx] = 'a'
grid[ey][ex] = 'z'


def find_shortest_path(sx, sy, reverse=False): #BFS
    paths = defaultdict(lambda:len(grid)*len(grid[0])) # ce ni default vrednosti nastavljeno, naj bo to n*m mape
    paths[(sy, sx)] = 0 #startno nastavi na 0
    should_search = [(sx, sy, 0)] #root node, nastavi steps na 0
    while len(should_search) > 0:
        x, y, steps = should_search[0] #preveri Queue
        should_search = should_search[1:] #dequeue
        from_height = ord(grid[y][x]) #daj v cifro

        for (dx, dy) in directions: # preveri levo,desno,gor,dol
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= len(grid[0]) or ny < 0 or ny >= len(grid): #ce gre out of bounds iskat po mapi
                continue

            to_height = ord(grid[ny][nx])

            #preveri ce grem lahko gor
            if not reverse and not from_height - to_height >= -1:
                continue
            #preveri ce gremlahko dol
            if reverse and not from_height - to_height <= 1:
                continue

            if paths[(ny, nx)] > steps + 1:
                paths[(ny, nx)] = steps + 1
                should_search.append((nx, ny, steps + 1)) #dodaj novi node ce lahko obiscem

    return paths

part1 = find_shortest_path(sx, sy)[ey, ex]
print(part1)

print(find_shortest_path(sx, sy))

part2 = min([dist for ((y, x), dist) in find_shortest_path(ex, ey, True).items() if grid[y][x] == 'a'])
print(part2)
