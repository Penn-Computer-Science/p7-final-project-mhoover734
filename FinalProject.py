import tkinter as tk

                       # 0 Nothing
colors = ["#000000", # 1 Hair & pants
          "#4e216b", # 2 Hoodie & highlights
          "#6f3198", # 3 Inner sleeve
          "#764099", # 4 Outer sleeve
          "#8a5cab", # 5 Hoodie trim
          "#341947", # 6 Pockets
          "#4d4d4d", # 7 Outer shoe (closer)
          "#575757", # 8 Inner shoe (further)
          "#1a1a1a", # 9 Inner pants (further)
          "#edd4c5", # a Main skin
          "#ba9e8d", # b Shaded skin
          "#cc93cc"] # c Eye color

def make_backwards_0():
    pattern = [
        "000000000",
        "011000000",
        "001111000",
        "011111110",
        "011111100",
        "111111110",
        "011111110",
        "011551100",
        "013222140",
        "013222240",
        "142222240",
        "042222240",
        "002222200",
        "005225500",
        "000551000",
        "000111000",
        "000101000",
        "000101000",
        "000101000",
        "000707000",
        "000000000"]
    scale = 5
    h = len(pattern)*scale
    w = len(pattern[0])*scale
    img = tk.PhotoImage(width=w, height=h)
    for y in range(h):
        for x in range(w):
            if pattern[y//scale][x//scale] != "0":
                if pattern[y//scale][x//scale] == "a":
                    img.put(colors[9], (x,y))
                elif pattern[y//scale][x//scale] == "b":
                    img.put(colors[10], (x,y))
                elif pattern[y//scale][x//scale] == "c":
                    img.put(colors[11], (x,y))
                else:
                    img.put(colors[int(pattern[y//scale][x//scale])-1], (x,y))
    return img

WIDTH = 600
HEIGHT = 400
root = tk.Tk()
root.title("Bad \"Rhythm\" Game")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

player_img=make_backwards_0()
player = canvas.create_image(40,225, image=player_img, anchor = 'nw')

root.mainloop()