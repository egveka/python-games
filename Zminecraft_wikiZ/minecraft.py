from tkinter import *

root = Tk()
root.title("Minecraft Recipe Checker")
root.geometry("600x400")

# --- Scrollable frame setup ---
canvas = Canvas(root, bg="#2b2b2b")
canvas.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

canvas.configure(yscrollcommand=scrollbar.set)

content = Frame(canvas, bg="#2b2b2b")
canvas.create_window((0, 0), window=content, anchor="nw")

content.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

# --- Block data (alphabetical) ---
blocks = {
    "Activator Rail": {
        "craftable": True,
        "recipe_img": "Zminecraft_wikiZ/images/activator_rail_craft.png",
        "uses": "speed up and power minecarts",
        "found_in": "mineshafts (mostly in the badlands biome)",
        "status": {"crafted": False, "placed": False, "used": False}
    },
    "Amethyst Cluster": {
        "craftable": False,
        "recipe_img": "Zminecraft_wikiZ/images/.png",
        "uses": "decoration/lighting",
        "found_in": "amethyst geodes",
        "status": {"placed": False, "used": False}
    },
    "Activator Rail": {
        "craftable": True,
        "recipe_img": "Zminecraft_wikiZ/images/activator_rail_craft.png",
        "uses": "speed up and power minecarts",
        "found_in": "mineshafts (mostly in the badlands biome)",
        "status": {"crafted": False, "placed": False, "used": False}
    }
}