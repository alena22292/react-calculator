from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

# create black magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 12, 124, "black")
blizzard = Spell("Blizzard", 9, 95, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 15, 165, "black")

# create white magic
pill = Spell("Pill", 12, 134, "white")
cure = Spell("Cure", 18, 220, "white")

# Create some Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
hielixer = Item("Mega Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

# Player attributes
player_magic = [fire, thunder, meteor, cure, pill, blizzard]
player_items = [{"item": potion, "quantity": 5},
                {"item": hipotion, "quantity": 3},
                {"item": superpotion, "quantity": 2},
                {"item": elixer, "quantity": 1},
                {"item": hielixer, "quantity": 1},
                {"item": grenade, "quantity": 1}]

# instantiate magic_spell_name with players
player1 = Person(460, 65, 60, 43, player_magic, player_items)
enemy1 = Person(1200, 65, 45, 25, [quake], [])

run = True
i = 0

fail_color = bcolors.FAIL + bcolors.BOLD + "Your enemy had defeated you!" + bcolors.ENDC
win_color = bcolors.OKGREEN + bcolors.BOLD + "You win!" + bcolors.ENDC

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while run:
    print('============================')
    player1.choose_action()
    choice = input("Choose action: ")
    index = int(choice) - 1

    if index == 0:
        dmg = player1.generate_damage()
        enemy1.take_damage(dmg)
        print("You attacked for", dmg, "points of damage")
    elif index == 1:
        player1.choose_magic()
        magic_choice = int(input("Choose magic: ")) - 1

        if magic_choice == -1:
            continue

        spell = player1.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        current_mp = player1.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + "\nNot Enough MP\n" + bcolors.ENDC)
            continue

        player1.reduce_mp(spell.cost)

        if spell.type == "white":
            player1.heal(magic_dmg)
            print(bcolors.OKGREEN + "\n" + spell.name + " heals for " + str(magic_dmg), "HP" + bcolors.ENDC)
        elif spell.type == "black":
            enemy1.take_damage(magic_dmg)
            print(bcolors.WARNING + "\n" + spell.name + " deals", str(magic_dmg), "point of damage", bcolors.ENDC)
    elif index == 2:
        player1.choose_item()
        item_choice = int(input("Choose item: ")) - 1

        if item_choice == -1:
            continue

        item = player1.items[item_choice]["item"]

        if player1.items[item_choice]["quantity"] == 0:
            print(bcolors.FAIL + '\n' + "None left..." + bcolors.ENDC)
            continue

        player1.items[item_choice]["quantity"] -= 1

        if item.type == "potion":
            player1.heal(item.prop)
            print(bcolors.OKGREEN + '\n' + item.name + " heals for " + str(item.prop), "HP" + bcolors.ENDC)
        elif item.type == "elixer":
            player1.hp = player1.maxhp
            player1.mp = player1.maxmp
            print(bcolors.OKGREEN + '\n' + item.name + " fully restored HP/MP" + bcolors.ENDC)
        elif item.type == "attack":
            player1.take_damage(item.prop)
            print(bcolors.FAIL + '\n' + item.name + " deals " + str(item.prop), "points of damage" + bcolors.ENDC)

    enemy_choice = 1
    enemy_dmg = enemy1.generate_damage()
    player1.take_damage(enemy_dmg)
    print("Enemy attacked for", enemy_dmg)

    print('============================')
    print("Enemy HP:", bcolors.FAIL + str(enemy1.get_hp()) + "/" + str(enemy1.get_max_hp()) + bcolors.ENDC + "\n")

    print("Your HP: ", bcolors.OKGREEN + str(player1.get_hp()) + "/" + str(player1.get_max_hp()) + bcolors.ENDC)
    print("Your MP: ", bcolors.OKBLUE + str(player1.get_mp()) + "/" + str(player1.get_max_mp()) + bcolors.ENDC)

    if enemy1.get_hp() == 0:
        print(win_color)
        run = False
    elif player1.get_hp() == 0:
        print(fail_color)
        run = False



