import tkinter as tk

WIDTH = 500
HEIGHT = 730
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

def draw_pattern(pattern):
    scale = 10
    h = len(pattern)*scale
    w = len(pattern[0])*scale
    img = tk.PhotoImage(width=w, height=h)
    for y in range(h):
        for x in range(w):
            if pattern[y//scale][x//scale] != "0":
                img.put(colors[ord(pattern[y//scale][x//scale])-97], (x,y))
    return img

def make_backwards_0():
    pattern = [
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
    return draw_pattern(pattern)
def make_backwards_1():
    pattern = [
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
    return draw_pattern(pattern)
def make_backwards_2():
    pattern = [
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
    return draw_pattern(pattern)
def make_forwards_0():
    pattern = [
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
    return draw_pattern(pattern)
def make_forwards_1():
    pattern = [
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
    return draw_pattern(pattern)
def make_forwards_2():
    pattern = [
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
    return draw_pattern(pattern)
def make_right_0():
    pattern = [
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
    return draw_pattern(pattern)
def make_right_1():
    pattern = [
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
    return draw_pattern(pattern)
def make_right_2():
    pattern = [
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
    return draw_pattern(pattern)
def make_left_0():
    pattern = [
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
    return draw_pattern(pattern)
def make_left_1():
    pattern = [
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
    return draw_pattern(pattern)
def make_left_2():
    pattern = [
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
    return draw_pattern(pattern)

player_img0=make_backwards_0()
player0 = canvas.create_image(20,10, image=player_img0, anchor = 'nw')
player_img1=make_backwards_1()
player1 = canvas.create_image(20,260, image=player_img1, anchor = 'nw')
player_img2=make_backwards_2()
player2 = canvas.create_image(20,510, image=player_img2, anchor = 'nw')
player_img3=make_forwards_0()
player3 = canvas.create_image(150,10, image=player_img3, anchor = 'nw')
player_img4=make_forwards_1()
player4 = canvas.create_image(150,260, image=player_img4, anchor = 'nw')
player_img5=make_forwards_2()
player5 = canvas.create_image(150,510, image=player_img5, anchor = 'nw')
player_img6=make_right_0()
player6 = canvas.create_image(280,10, image=player_img6, anchor = 'nw')
player_img7=make_right_1()
player7 = canvas.create_image(280,260, image=player_img7, anchor = 'nw')
player_img8=make_right_2()
player8 = canvas.create_image(280,510, image=player_img8, anchor = 'nw')
player_img9=make_left_0()
player9 = canvas.create_image(410,10, image=player_img9, anchor = 'nw')
player_img10=make_left_1()
player10 = canvas.create_image(410,260, image=player_img10, anchor = 'nw')
player_img11=make_left_2()
player11 = canvas.create_image(410,510, image=player_img11, anchor = 'nw')

root.mainloop()