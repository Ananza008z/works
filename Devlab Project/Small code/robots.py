def move_robot(commands):

    x, y = 0, 0
    direction = (1, 0)  

    for cmd in commands:
        if cmd == 'FW':
            x += direction[0]
            y += direction[1]
        elif cmd == 'BK':
            x -= direction[0]
            y -= direction[1]
        elif cmd == 'R':
            direction = (direction[1], -direction[0])  
            x += direction[0]
            y += direction[1]
        elif cmd == 'L':
            direction = (-direction[1], direction[0])  
            x += direction[0]
            y += direction[1]
        elif cmd == 'END':
            break

    return x, y

commands = []
while True:
    inp = str(input())
    commands.append(inp)
    if inp == 'END':
        break

final_position = move_robot(commands)

print(final_position)
