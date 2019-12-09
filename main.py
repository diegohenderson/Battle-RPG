from Classes.game import Person, Bcolors
from Classes.magic import Spell
from Classes.Inventory import Item
# Create Black Magic
fire = Spell ("Fire", 10, 100, "black")
thunder = Spell ("Thunder", 10, 100, "black")
blizzard = Spell ("Blizzard", 18, 100, "black")
meteor = Spell ("Meteor", 20, 200, "black")
quake = Spell ("Quake", 14, 120, "black")

# white magic
cure = Spell ("Cure", 12, 120, "white")
cura = Spell ("Cura", 18, 200, "white")

#items
potion = Item ("Potion", "potion","Heals 50 HP",50)
hipotion= Item("Hi.Potion","potion","Heals 100 HP",100)
superpotion = Item("Super Potion","potion","Heals 500 HP", 500)
elixer= Item("Elixer","elixer","Fully restores HP/MP", 999)
hielixer= Item("MegaElixer","elixer ","restores", 9988)

granade= Item("Granade", "attack" ," deals 500 dmg", 500)
player_spells= [fire, thunder, blizzard, meteor, quake, cure, cura]
player_items = [potion,hipotion,superpotion,elixer,hielixer]
#instantiate people
player = Person(460, 65, 60, 34, player_spells, player_items)
enemy = Person(1200, 65, 45, 25, [], [])
running = True
i = 0
print(Bcolors.FAIL + Bcolors.BOLD + "AN ENEMY Attacks" + Bcolors.ENDC)
while running:
    print("----------")
    player.choose_action()
    choice= input("choose action:")
    index = int(choice) -1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("you attacked for ", dmg, "points of damage")
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic!")) -1
        if magic_choice == -1:
            continue
        spell=player.magic[magic_choice]
        magic_dmg= spell.generate_damage()

        current_mp = player.get_mp()
        if spell.cost > current_mp:
            print(Bcolors.FAIL + "\n Not enough MP \n" + Bcolors.ENDC)
            continue
        player.reduce_mp(spell.cost)
        if spell.type == "white":
            player.heal(magic_dmg)
            print(Bcolors.OKGREEN + "\n" + spell.name + "heals for:", str(magic_dmg), "HP." + Bcolors.ENDC)
        elif spell.type == "black":
            enemy.take_damage(magic_dmg)
            print(Bcolors.OKBLUE + "\n" + spell.name + "deals", str(magic_dmg), "points of damage" + Bcolors.ENDC)

    elif index == 2:
        player.choose_item()
        item_choice= int(input("choose item:"))-1
        if item_choice == -1:
            continue
        item = player.items[item_choice]
        if item.type == "potion":
            player.heal(item.prop)
            print(Bcolors.OKGREEN+ "\n"+ item.name + "you have been healed for:", str(item.prop), "hp"+ Bcolors.ENDC)
    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("enemy attacks for", enemy_dmg)
    print("-----------------")
    print("enemy hp:", Bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + Bcolors.ENDC + "\n")
    print("your hp:" + Bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + "/" + Bcolors.ENDC)
    print("your mp:" + Bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + "/" + Bcolors.ENDC + "\n")



    if enemy.get_hp() == 0:
        print(Bcolors.OKGREEN + "you win!" + Bcolors.ENDC)
        running = False
    elif player.get_hp() ==0:
        print(Bcolors.FAIL + "your enemy has defeated you!" + Bcolors.ENDC)
        running = False

