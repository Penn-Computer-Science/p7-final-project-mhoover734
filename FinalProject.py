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
        "0ablblbaa",
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
        "0ablblbaa",
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
        "000bdcf00",
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
        "00fcdb000",
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
def make_attack():
    pattern = [
        "0b000000000",
        "00bc0000ll0",
        "b000ddee00l",
        "0bc000000l0",
        "b00ccddee00",
        "0cc000000l0",
        "000cddeel00"]
    return draw_pattern(pattern, 12)

player_up_0=make_up_0()
player_up_1=make_up_1()
player_up_2=make_up_2()
player_down_0=make_down_0()
player_down_1=make_down_1()
player_down_2=make_down_2()
player_right_0=make_right_0()
player_right_1=make_right_1()
player_right_2=make_right_2()
player_left_0=make_left_0()
player_left_1=make_left_1()
player_left_2=make_left_2()

current_player_sprite = ("down", 0)
player_sprite_list = {"up": (player_up_0, player_up_1, player_up_2),
                      "down": (player_down_0, player_down_1, player_down_2),
                      "right": (player_right_0, player_right_1, player_right_2),
                      "left": (player_left_0, player_left_1, player_left_2)}

attack_sprite=make_attack()

#player = canvas.create_image(WIDTH//2,HEIGHT//2, image=player_down_0, anchor = 's')
#attack = canvas.create_image(WIDTH//2,HEIGHT//2, image=attack_sprite, anchor = 'center')

#canvas.itemconfig(player, image=player_down_1)

movement = {'up': 0,'down': 0,'right': 0,'left': 0}
#keys_pressed = {'w': False,'s': False,'d': False,'a': False}

def move_pressed(event, direction):
    global movement
    movement[direction] = 1

def stop_movement(event, direction):
    global movement
    movement[direction] = 0

def sprite_animation(direction):
    if current_player_sprite[0] != direction

move_distance = 12
def update_player():
    canvas.move(player, (movement['right']-movement['left'])*move_distance, (movement['down'] - movement['up'])*move_distance)
    if movement['right']-movement['left'] == 1: #moving right
        sprite_animation("right")
    elif movement['right']-movement['left'] == -1: #moving left
        pass
    elif movement['down'] - movement['up'] == 1: #moving down
        pass
    elif movement['down'] - movement['up'] == -1: #moving up
        pass

    


root.bind("w", lambda event: move_pressed(event, 'up'))
root.bind("s", lambda event: move_pressed(event, 'down'))
root.bind("d", lambda event: move_pressed(event, 'right'))
root.bind("a", lambda event: move_pressed(event, 'left'))
root.bind("<KeyRelease-w>", lambda event: stop_movement(event, 'up'))
root.bind("<KeyRelease-s>", lambda event: stop_movement(event, 'down'))
root.bind("<KeyRelease-d>", lambda event: stop_movement(event, 'right'))
root.bind("<KeyRelease-a>", lambda event: stop_movement(event, 'left'))

delay = 50
timer = 0
def game_loop():
    global timer
    timer += delay
    #move_enemies() #move all enemies
    #check_collisions() #check out new collisions
    update_player()
    #print(keys_pressed)
    root.after(delay, game_loop) #every [delay], run game_loop (24ms default)


def start():
    global player
    player = canvas.create_image(WIDTH//2,HEIGHT//2, image=player_down_0, anchor = 's')
    game_loop()
def reset():
    canvas.delete("all")
    #enemies.clear()
    start()
reset()

root.mainloop()