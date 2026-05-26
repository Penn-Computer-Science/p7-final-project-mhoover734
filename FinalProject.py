import tkinter as tk

WIDTH = 900
HEIGHT = 600
root = tk.Tk()
root.title("\"Game\"")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

                       # 0 Nothing
colors = ["#000000", # a Hair & pants
          "#4e216b", # b Hoodie & highlights
          "#6f3198", # c Inner sleeve
          "#764099", # d Outer sleeve
          "#8a5cab", # e Hoodie trim
          "#341947", # f Pockets
          "#4d4d4d", # g Outer shoe (closer)
          "#575757", # h Inner shoe (further)
          "#1a1a1a", # i Inner pants (further)
          "#edd4c5", # j Main skin
          "#ba9e8d", # k Shaded skin
          "#cc93cc"] # l Eye color

def draw_pattern(pattern, scale):
    h = len(pattern)*scale
    w = len(pattern[0])*scale
    img = tk.PhotoImage(width=w, height=h)
    for y in range(h):
        for x in range(w):
            if pattern[y//scale][x//scale] != "0":
                img.put(colors[ord(pattern[y//scale][x//scale])-97], (x,y))
    return img

def make_up_0():
    pattern = [
        "000000000",
        "000000000",
        "0aa000000",
        "00aaaa000",
        "0aaaaaaa0",
        "0aaaaaa00",
        "aaaaaaaa0",
        "0aaaaaaa0",
        "0aaeeaa00",
        "0acbbbad0",
        "0acbbbbd0",
        "adbbbbbd0",
        "0dbbbbbd0",
        "00bbbbb00",
        "00ebbee00",
        "000eea000",
        "000aaa000",
        "000a0a000",
        "000a0a000",
        "000a0a000",
        "000g0g000",
        "000000000"]
    return draw_pattern(pattern, 12)
def make_up_1():
    pattern = [
        "000000000",
        "000000000",
        "0aa000000",
        "00aaaa000",
        "0aaaaaa00",
        "0aaaaaaa0",
        "0aaaaaa00",
        "aaaaaaaa0",
        "0aaeeaaa0",
        "0acbbba00",
        "0acbbbad0",
        "adbbbbbd0",
        "adbbbbbd0",
        "00bbbbb00",
        "00ebbbe00",
        "000eee000",
        "000aaa000",
        "000i0a000",
        "000i0a000",
        "000h0a000",
        "00000g000",
        "000000000"]
    return draw_pattern(pattern, 12)
def make_up_2():
    pattern = [
        "000000000",
        "000000000",
        "0aa000000",
        "00aaaa000",
        "00aaaaa00",
        "0aaaaaaa0",
        "0aaaaaa00",
        "aaaaaaaa0",
        "0aaeeaaa0",
        "0acbbba00",
        "0acbbbad0",
        "adbbbbbd0",
        "adbbbbbd0",
        "00bbbbb00",
        "00bbbee00",
        "00eeea000",
        "000aai000",
        "000a0i000",
        "000a0i000",
        "000a0h000",
        "000g00000",
        "000000000"]
    return draw_pattern(pattern, 12)
def make_down_0():
    pattern = [
        "000000000",
        "000000000",
        "0aa000000",
        "00aaaaa00",
        "0aaabbaa0",
        "0ablblba0",
        "aabjjjba0",
        "0aaekeaa0",
        "0acbebc00",
        "0acbbbcd0",
        "adbbbbbd0",
        "0dbbbfcd0",
        "0dcfbfcd0",
        "00cfbbf00",
        "00fbbee00",
        "000eea000",
        "000aaa000",
        "000a0a000",
        "000a0a000",
        "000a0a000",
        "000g0g000",
        "000000000"]
    return draw_pattern(pattern, 12)
def make_down_1():
    pattern = [
        "000000000",
        "000000000",
        "000000000",
        "0aa0aa000",
        "00aaaaa00",
        "0aaabbaa0",
        "0ablblba0",
        "aaajjjaa0",
        "0acekeca0",
        "0acbebcd0",
        "adbbbbbd0",
        "adbbbfcd0",
        "0dcfbfcd0",
        "00cfbbf00",
        "00fbbbe00",
        "00ebee000",
        "000eaa000",
        "000aai000",
        "000a0i000",
        "000a0i000",
        "000a0h000",
        "000g00000"]
    return draw_pattern(pattern, 12)
def make_down_2():
    pattern = [
        "000000000",
        "000000000",
        "000000000",
        "0aa0aa000",
        "00aaaaa00",
        "0aaabbaa0",
        "0ablblba0",
        "aaajjjaa0",
        "0acekeca0",
        "0acbebcd0",
        "adbbbbbd0",
        "adbbbbbd0",
        "0dcfbfcd0",
        "00cfbfcd0",
        "00fbbbf00",
        "00eebbe00",
        "000aee000",
        "000iaa000",
        "000i0a000",
        "000i0a000",
        "000h0a000",
        "00000g000"]
    return draw_pattern(pattern, 12)
def make_right_0():
    pattern = [
        "000000000",
        "000000000",
        "00aa00a00",
        "000aaaa00",
        "00aaabba0",
        "00aabblb0",
        "0aaabjj00",
        "0aaaek000",
        "00adce000",
        "00adcb000",
        "000dcb000",
        "000bdc000",
        "000bdcf00",
        "000bbfb00",
        "000ebe000",
        "0000ea000",
        "0000aa000",
        "0000ai000",
        "0000ai000",
        "0000ai000",
        "0000ggh00",
        "000000000"]
    return draw_pattern(pattern, 12)
def make_right_1():
    pattern = [
        "000000000",
        "000000000",
        "00aa00a00",
        "000aaaa00",
        "00aaabba0",
        "00aabblb0",
        "00aabjj00",
        "0aaabk000",
        "0aaaee000",
        "00adcb000",
        "00adcb000",
        "000dcb000",
        "000bdcf00",
        "000bdfb00",
        "000ebfe00",
        "0000ee000",
        "0000aa000",
        "0000ai000",
        "000aai000",
        "000a0hh00",
        "000gg0000",
        "000000000"]
    return draw_pattern(pattern, 12)
def make_right_2():
    pattern = [
        "000000000",
        "000000000",
        "00aa00a00",
        "000aaaa00",
        "00aaabba0",
        "00aabblb0",
        "00aabjj00",
        "0aaabk000",
        "0aaaee000",
        "00adcb000",
        "00adcb000",
        "000dcb000",
        "000bdcf000",
        "000bdfe00",
        "000bbe000",
        "000eea000",
        "0000aa000",
        "0000ia000",
        "000iia000",
        "000i0gg00",
        "000hh0000",
        "000000000"]
    return draw_pattern(pattern, 12)
def make_left_0():
    pattern = [
        "000000000",
        "000000000",
        "0aa000000",
        "00aaaaa00",
        "0abbaa000",
        "0blbbaa00",
        "00jjbaa00",
        "000kea000",
        "000ecd000",
        "000bcd000",
        "000bcd000",
        "000cdb000",
        "00fcdb000",
        "00bfbb000",
        "000ebe000",
        "000ae0000",
        "000aa0000",
        "000ia0000",
        "000ia0000",
        "000ia0000",
        "00hgg0000",
        "000000000"]
    return draw_pattern(pattern, 12)
def make_left_1():
    pattern = [
        "000000000",
        "000000000",
        "0aa000000",
        "00aaaaa00",
        "0abbaa000",
        "0blbbaa00",
        "00jjbaa00",
        "000keaa00",
        "000eca000",
        "000bcd000",
        "000bcd000",
        "000bcd000",
        "00fcdb000",
        "00efdb000",
        "000ebb000",
        "000aee000",
        "000aa0000",
        "000ai0000",
        "000aii000",
        "00gg0i000",
        "0000hh000",
        "000000000"]
    return draw_pattern(pattern, 12)
def make_left_2():
    pattern = [
        "000000000",
        "000000000",
        "0aa000000",
        "00aaaaa00",
        "0abbaa000",
        "0blbbaa00",
        "00jjbaa00",
        "000keaa00",
        "000eca000",
        "000bcd000",
        "000bcd000",
        "000bcd000",
        "00fcdb000",
        "00bfdb000",
        "00efbe000",
        "000ee0000",
        "000aa0000",
        "000ia0000",
        "000iaa000",
        "00hh0a000",
        "0000gg000",
        "000000000"]
    return draw_pattern(pattern, 12)
def make_attack(rotation):
    pattern = [
        "0b000000000",
        "00bc0000ll0",
        "b000ddee00l",
        "0bc000000l0",
        "b00ccddee00",
        "0cc000000l0",
        "000cddeel00"]
    scale = 12
    h = len(pattern)*scale
    w = len(pattern[0])*scale
    if rotation in ("up", "down"):
        img = tk.PhotoImage(width=len(pattern[0])*scale, height=len(pattern)*scale)
    else:
        img = tk.PhotoImage(width=len(pattern)*scale, height=len(pattern[0])*scale)
    for y in range(len(pattern)*scale):
        for x in range(len(pattern[0])*scale):
            if pattern[y//scale][x//scale] != "0":
                drawing_style = {"down": (x,y),"up": (x,h-y),"left": (h-y,w-x),"right": (y,w-x)}
                img.put(colors[ord(pattern[y//scale][x//scale])-97], drawing_style[rotation])
    return img
def make_room():
    pattern = [
        "111111111111111111111111111111111111111111111111111111111111111111111111111",
        "111111111111111111111111111111111111111111111111111111111111111111111111111",
        "111111111111111111111111111111111111111111111111111111111111111111111111111",
        "114444444444444444444444444444444444444444444444433344444444444444444444411",
        "114444444444444444444444444444444444444444444444433344444444444444444444411",
        "114444444444444444444444444444444444444444444444433344444444444444444444411",
        "114444444444444444444444444444444444444444444444433344444499999999944444411",
        "114444444444444444444444444444444444444444444444433344444990090099944444411",
        "114444444444444444444444444444444444444444444444433344449900900999933444411",
        "114444444444444444444444444444444444444444444444433344499999999990933444411",
        "114444444444444444444444444444444444444444444444433344499000009900933444411",
        "114444444444444444444444444444444444444444444444433322290009000909877782211",
        "114444444444444444444444444444444444444444444444433222290009000990788888211",
        "114444444444444444444444444444444444444444444444433266690999990900780908611",
        "114444444444444444444444444444444444444444444444432666590009000909789998611",
        "114444444444444444444444444444444444444444444444432665588809000999880908611",
        "114444444444444444444444444444444444444444444444426655898800009996588888511",
        "112222222222222222222222222222222222222222222222226555809899999965555555511",
        "112222222222222222222222222222222222222222222222265555888655555555555555511",
        "115555555555555555555555555555555555555555555555555555555555555555555555511",
        "115555555555555555555555555555555555555555555555555555555555555555555555511",
        "115555555555555555555555555555555555555555555555555555555555555555555555511",
        "115555555555555555555555555555555555555555555555555555555555555555555555511",
        "115555555555555555555555555555555555555555555555555555555555555555555555511",
        "115555555555555555555555555555555555555555555555555555555555555555555555511",
        "115555555555555555555555555555555555555555555555555555555555555555555555511",
        "115555555555555555555555555555555555555555555555555555555555555555555555511",
        "115555555555555555555555555555555555555555555555555555555555555555555555511",
        "115555555555555555555555555555555555555555555555555555555555555555555555511",
        "115555555555555555555555555555555555555555555555555555555555555555555555511",
        "115555555555555555555555555555555555555555555555555555555555555555555555511",
        "115555555555555555555555555555555555555555555555555555555555555555555555511",
        "115555555555555555555555555555555555555555555555555555555555555555555555511",
        "115555555555555555555555555555555555555555555555555555555555555555555555511",
        "115555555555555555555555555555555555555555555555555555555555555555555555511",
        "115555555555555555555555555555555555555555555555555555555555555555555555511",
        "115555555555555555555555555555555555555555555555555555555555555555555555511",
        "115555555555555555555555555555555555555555555555555555555555555555555555511",
        "115555555555555555555555555555555555555555555555555555555555555555555555511",
        "115555555555555555555555555555555555555555555555555555555555555555555555511",
        "116666666666666666666666666666666666666666666666666666666666666666666666611",
        "116666666666666666666666666666666666666666666666666666666666666666666666611",
        "116666666666666666666666666666666666666666666666666666666666666666666666611",
        "116666666666666666666666666666666666666666666666666666666666666666666666611",
        "116666666666666666666666666666666666666666666666666666666666666666666666611",
        "116666666666666666666666666666666666666666666666666666666666666666666666611",
        "116666666666666666666666666666666666666666666666666666666666666666666666611",
        "116666666666666666666666666666666666666666666666666666666666666666666666611",
        "111111111111111111111111111111111111111111111111111111111111111111111111111",
        "111111111111111111111111111111111111111111111111111111111111111111111111111"
    ]
    room_colors = [
        "#7F655B", # lightest brown
        "#000000", # outer trim
        "#252525", # wall trim
        "#313131", # that one wall
        "#414141", # main back walls
        "#A4A4A4", # main floor
        "#959595", # shaded floor
        "#4E3D37", # darkest brown
        "#59453E", # darkish brown
        "#665048"] # lightish brown

    room_scale=12
    h = len(pattern)*room_scale
    w = len(pattern[0])*room_scale
    img = tk.PhotoImage(width=w, height=h)
    for y in range(h):
        for x in range(w):
            img.put(room_colors[int(pattern[y//room_scale][x//room_scale])], (x,y))
    return img

attack_sprite_up=make_attack("up")
attack_sprite_down=make_attack("down")
attack_sprite_left=make_attack("left")
attack_sprite_right=make_attack("right")

room_img=make_room()

current_player_sprite = ("down", 2)
player_sprite_list = {"up": (make_up_0(), make_up_1(), make_up_0(), make_up_2()),
                      "down": (make_down_0(), make_down_1(), make_down_0(), make_down_2()),
                      "right": (make_right_0(), make_right_1(), make_right_0(), make_right_2()),
                      "left": (make_left_0(), make_left_1(), make_left_0(), make_left_2())}

movement = {'up': 0,'down': 0,'right': 0,'left': 0}


def change_movement(event, direction, state):
    global movement
    movement[direction] = state


def sprite_animation(direction):
    global current_player_sprite
    if current_player_sprite[0] != direction:
        current_player_sprite = (direction, 0)
        canvas.itemconfig(player, image=player_sprite_list[direction][0])
    else:
        current_player_sprite = (direction, (current_player_sprite[1]+1)%4)
        canvas.itemconfig(player, image=player_sprite_list[direction][current_player_sprite[1]])

movement_locked = 0
move_distance = 12
stamina = 100
def update_player():
    global current_player_sprite, movement_locked, stamina
    if stamina <= 100-4:
        stamina += 4
    player_pos = canvas.bbox(player)
    moved = {"horizontally": False, "vertically": False}
    predicted_x = player_pos[0] + (movement['right']-movement['left'])*move_distance
    predicted_y = player_pos[1] + (movement['down'] - movement['up'])*move_distance
    if predicted_x > 12 and predicted_x < 780 and movement_locked == 0:
        canvas.move(player, (movement['right']-movement['left'])*move_distance, 0) #moves the player horizontally
        moved["horizontally"] = True #states the player has possibly moved horizontally
    if predicted_y > 12 and predicted_y < 318 and movement_locked == 0:
        canvas.move(player, 0, (movement['down'] - movement['up'])*move_distance) #moves the player vertically
        moved["vertically"] = True #states the player has possibly moved vertically
    print(f"Vert: {moved["vertically"]}   Hori: {moved["horizontally"]}")
    if ((moved["horizontally"] and movement['right']-movement['left'] != 0) or (moved["vertically"] and movement['down']-movement['up'] != 0)) and move_distance == 24:
        stamina -= 8 #Above is the check to make sure the player is moving and running
        if stamina <= 0: #If stam hits 0 from above drain, lock movement for 10 frames
            movement_locked = 10
    if movement['right']-movement['left'] == 1 and moved["horizontally"] == True: #moving right
        sprite_animation("right")
    elif movement['right']-movement['left'] == -1 and moved["horizontally"] == True: #moving left
        sprite_animation("left")
    elif movement['down']-movement['up'] == 1 and moved["vertically"] == True: #moving down
        sprite_animation("down")
    elif movement['down']-movement['up'] == -1 and moved["vertically"] == True: #moving up
        sprite_animation("up")
    else:
        current_player_sprite = (current_player_sprite[0], 0)
        canvas.itemconfig(player, image=player_sprite_list[current_player_sprite[0]][0])
    if movement_locked != 0:
        movement_locked -= 1
        current_player_sprite = (current_player_sprite[0], 1)
        canvas.itemconfig(player, image=player_sprite_list[current_player_sprite[0]][1])

def reset(event):
    canvas.delete("all")
    start()

def change_run(event, starting):
    global move_distance
    if bool(starting):
        move_distance = 24
    else:
        move_distance = 12

def attack(event):
    global movement_locked, attack
    if movement_locked != 0:
        return
    movement_locked = 4
    player_pos = canvas.bbox(player)
    if current_player_sprite[0] == "up":
        attack = canvas.create_image(player_pos[0]-24, player_pos[1]+59+12, image=attack_sprite_up, anchor = "sw")
        canvas.tag_raise(player)
    elif current_player_sprite[0] == "down":
        attack = canvas.create_image(player_pos[0]-24, player_pos[3]-60, image=attack_sprite_down, anchor = "nw")
    elif current_player_sprite[0] == "left":
        attack = canvas.create_image(player_pos[0]+11, player_pos[1]+59, image=attack_sprite_left, anchor = "ne")
    else:
        attack = canvas.create_image(player_pos[2]-12, player_pos[1]+59, image=attack_sprite_right, anchor = "nw")

root.bind("w", lambda event: change_movement(event, 'up', 1))
root.bind("W", lambda event: change_movement(event, 'up', 1))
root.bind("s", lambda event: change_movement(event, 'down', 1))
root.bind("S", lambda event: change_movement(event, 'down', 1))
root.bind("d", lambda event: change_movement(event, 'right', 1))
root.bind("D", lambda event: change_movement(event, 'right', 1))
root.bind("a", lambda event: change_movement(event, 'left', 1))
root.bind("A", lambda event: change_movement(event, 'left', 1))
root.bind("<KeyRelease-w>", lambda event: change_movement(event, 'up', 0))
root.bind("<KeyRelease-W>", lambda event: change_movement(event, 'up', 0))
root.bind("<KeyRelease-s>", lambda event: change_movement(event, 'down', 0))
root.bind("<KeyRelease-S>", lambda event: change_movement(event, 'down', 0))
root.bind("<KeyRelease-d>", lambda event: change_movement(event, 'right', 0))
root.bind("<KeyRelease-D>", lambda event: change_movement(event, 'right', 0))
root.bind("<KeyRelease-a>", lambda event: change_movement(event, 'left', 0))
root.bind("<KeyRelease-A>", lambda event: change_movement(event, 'left', 0))
root.bind("<Shift_L>", lambda event: change_run(event, 1))
root.bind("<KeyRelease-Shift_L>", lambda event: change_run(event, 0))
root.bind("r", reset)
root.bind("<space>", attack)

delay = 80
timer = 0
def game_loop():
    global timer
    timer += delay
    #move_enemies() #move all enemies
    #check_collisions() #check out new collisions
    update_player()
    root.after(delay, game_loop) #every [delay], run game_loop
    print(stamina)
    if movement_locked == 0:
        canvas.delete(attack)
    canvas.coords(stamina_bar, 84, 10, 84+stamina*2, 26)


def start():
    global player, stamina_bar
    room = canvas.create_image(0, 0, image=room_img, anchor = 'nw')
    player = canvas.create_image(420, 240, image=player_sprite_list["down"][0], anchor = 'nw')
    stamina_label = canvas.create_text(26, 18, text="Stamina:", fill="white", anchor = "w")
    stamina_bar = canvas.create_rectangle(84, 10, 84+stamina*2, 26, fill="blue")
start()
game_loop()
root.mainloop()