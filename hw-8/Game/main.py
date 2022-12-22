#ne zasicha exception-ite ot faila exceptions

#from exceptions import *
# from exceptions import InvalidParameters
# from exceptions import CharacterExists
# from exceptions import InvalidCharacter
# from exceptions import CharacterNotFound
# from exceptions import InvalidSex

# exceptions.character_exist()
# exceptions.character_n_f()
# exceptions.inv_character()
# exceptions.invalid_commands()
# exceptions.invalid_param()
# exceptions.invalid_sex()


characters_names = []
characters = []
characters_class = ["Warrior", "Mage", "Priest", "Rogue"]
class Menu:
    def print_commands(self):
        print("1. Create a new character.")
        print("2. Create a weapon for existing character.")
        print("3. Create an additional weapon for existing character.")
        print("4. Print all existing characters.")
        print("5. Delete an existing character.")
        print("6. Close game.")

    def command_create_character(self, name, sex, ch_class, weapon=None, additional_weapon=None):
        return name, sex, ch_class

    def command_create_weapon(self, name, weapon):
        durability = 100
        return weapon, "with", durability, "durability"
        #return weapon

    def command_additional_weapon(self, name, add_weapon):
        return add_weapon

    def command_print_characters(self):
        pass

    def command_delete_characters(self):
        pass

    def run(self):
        # infinite menu loop
        while True:
            Menu.print_commands(self)   
        
            # ask the user to choose a command

            choice = input("Choose an item from the menu: ")

            # catch errors
            try:

                # process the user's choice
                if choice == "1":
                    # ask the user to input the necessary command parameters
                    name = input("Enter the character name (alpha-numeric): ")
                    if name in characters_names:
                        raise CharacterExists("Character exists!")

                    sex = input("Enter the character sex(Male or Female): ")
                    if sex != "Male" and sex != "Female":
                        raise InvalidSex("Error: Invalid sex")

                    ch_class = input("Enter the character class(Warrior, Mage, Priest, Rogue): ")
                    if name.isdigit() or sex.isdigit() or ch_class.isdigit():
                    #tozi if vinagi vliza v error, koito ot druga strana ne iska da se importne
                        raise InvalidParameters("Not supporting numbers!")

                    if ch_class not in characters_class:
                        raise InvalidCharacter("Invalid character!")

                    characters_names.append(name)
                    char = self.command_create_character(name, sex, ch_class)
                    characters.append(char)
                    print(char)
                    continue

                if choice == "2":
                    name = input("Enter the character name (alpha-numeric): ")
                    if name in characters_names:
                        weapon = input("Enter a weapon: ")
                        weap = self.command_create_weapon(name, weapon)
                        print(f"{name} using {weap}")
                        continue
                    else:
                        raise CharacterNotFound("Character not found!")

                if choice == "3":
                    name = input("Enter the character name (alpha-numeric): ")
                    if name in characters_names:
                        additional_weapon = input("Enter an additional weapon: ")
                        add_weapon = self.command_additional_weapon(name, additional_weapon)
                        print(f"To character named {name} added additional weapon {add_weapon}")
                        continue
                    else:
                        raise CharacterNotFound("Character not found!")

                if choice == "4":
                    print(f"The characters:{characters}.")
                    continue

                if choice == "5":
                    characters.clear()
                    print(f"{characters} All characters deleted!")
                    continue

                if choice == "6":
                    print('Goodbye!')
                    break
                else:
                    raise InvalidCommand("Invalid choice!")

            except Exception as ex:
                print(f"Error: {str(ex)}")
            print()

if __name__ == '__main__':
    menu = Menu()
    menu.run()
    print()