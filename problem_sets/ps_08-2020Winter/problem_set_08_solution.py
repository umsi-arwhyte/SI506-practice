# START PROBLEM SET 08
print('PROBLEM SET 08 \n')

# BACKGROUND

# In this homework, you'll work and code as a Software Engineer of a game company.
# You are asked to construct objects for the heroes in the game and also simulate the game.

# < heroes > is a list of dictionaries. Each dictionary describes the attributes of a hero at level 0 in the game.

heroes = [
    {
        "name": "Axe",
        "main_attribute": "strength",
        "base_hp": 625,
        "base_mp": 234,
        "base_damage": 52,
        "strength_growth_per_level": 3.6,
        "agility_growth_per_level": 2.2,
        "intelligence_growth_per_level": 1.6
    },
    {
        "name": "Monkey King",
        "main_attribute": "agility",
        "base_hp": 511,
        "base_mp": 260,
        "base_damage": 51,
        "strength_growth_per_level": 2.8,
        "agility_growth_per_level": 3.7,
        "intelligence_growth_per_level": 1.8
    },
    {
        "name": "Invoker",
        "main_attribute": "intelligence",
        "base_hp": 492,
        "base_mp": 195,
        "base_damage": 42,
        "strength_growth_per_level": 2.4,
        "agility_growth_per_level": 1.9,
        "intelligence_growth_per_level": 4.6
    }
]

# There are 39 strength heroes, 37 agility heroes and 43 intelligence heroes in the game.
# we will be looking at one hero from each type in this problem set.

# Some questions to think of before starting (NOT GRADED):
# How would you design the classes to describe those heroes?
# What is a parent class?
# What are child classes?
# What are the differences between child classes?

# First, let's create the parent class for all heroes
class Hero():
    """
    This is a class that contains information on < Hero >.

    Attributes:
        name (str): The name of the hero.
        hp (float): The health points of the hero.
        mp (float): The magic points of the hero.
        level (int): The level of the hero.
        damage (float): The damage of the hero.
        strength_growth (float): The strength gain per level of the hero.
        agility_growth (float): The agility gain per level of the hero.
        intelligence_growth (float): The intelligence gain per level of the hero.
    """

    def __init__(self, name, hp, mp, damage, strength_growth, agility_growth, intelligence_growth):
        """
        The constructor of the < Hero > class. Here you will need to create
        the attributes ("instance variables") that were described in the < Hero >
        docstring. Note that some of the attributes are defined by parameters passed
        to this constructor method, but others are not. In this case, the < level > should be 0.

        Parameters:
            name (str): The name of the hero.
            hp (float): The health points of the hero.
            mp (float): The magic points of the hero.
            damage (float): The damage of the hero.
            strength_growth (float): The strength gain per level of the hero.
            agility_growth (float): The agility gain per level of the hero.
            intelligence_growth (float): The intelligence gain per level of the hero.

        Returns:
            None
        """

        self.name = name
        self.hp = float(hp)
        self.mp = float(mp)
        self.damage = float(damage)
        self.strength_growth = strength_growth
        self.agility_growth = agility_growth
        self.intelligence_growth = intelligence_growth
        self.level = 0


    def __str__(self):
        """
        This is the string method for the < Hero > class, describing the infomation of the hero in the format:
        "< name >, level < level >, hp < hp >, mp < mp >, damage < damage >".

        Parameters:
            None

        Returns:
            str: A string that describes this instance of < Hero >.
        """

        description = f"{self.name}, level {self.level}, hp {self.hp}, mp {self.mp}, damage {self.damage}"
        return description


    def attack(self, other):
        """
        This method allows current hero to attack the other hero.
        Attack means that other hero's < hp > would be reduced by current hero's < damage >.

        Parameters:
            other (obj): other is an instance of < Hero >.

        Returns:
            None
        """

        other.hp -= self.damage


    def is_dead(self):
        """
        This method examines whether the hero is dead or not.
        Dead means < hp > is equal or less than 0.

        Parameters:
            None

        Returns:
            dead (bool): True if the hero is dead. False if the hero is alive.
        """

        return self.hp <= 0


# Second, let's create the child classes for different types of heroes

class StrengthHero(Hero):

    def __init__(self, name, hp, mp, damage, strength_growth, agility_growth, intelligence_growth):
        """
        The constructor of the < StrengthHero > class.
        Use < super() > to initialize the attributes of the parent class.
        Add a new attribute < main_attribute >.
        The < main_attribute > of a strength hero should be "strength".

        Parameters:
            name (str): The name of the hero.
            hp (float): The health points of the hero.
            mp (float): The magic points of the hero.
            damage (float): The damage of the hero.
            strength_growth (float): The strength gain per level of the hero.
            agility_growth (float): The agility gain per level of the hero.
            intelligence_growth (float): The intelligence gain per level of the hero.

        Returns:
            None
        """

        super().__init__(name, hp, mp, damage, strength_growth, agility_growth, intelligence_growth)
        self.main_attribute = "strength"


    def level_up(self):
        """
        This method would level a hero up:
        1. increase < level > by 1
        2. increase < hp > by 20 * < strength_growth >
        3. increase < mp > by 5 * < intelligence_growth >
        4. increase < damage > by 1 * < main_attribute > growth

        Parameters:
            None

        Returns:
            None
        """

        self.level += 1
        self.hp += 20*self.strength_growth
        self.mp += 5*self.intelligence_growth
        self.damage += 1*self.strength_growth


    def ability(self):
        """
        This method would double the hero's < hp > at the cost of 200 < mp >.
        If the hero's < mp > is less than 200, this method should print "< name > doesn't have enough mp"
        If the hero's < mp > is equal or greater than 200, this method would double its < hp >,
        reduce its < mp > by 200 and print "< name > now has < hp > hp"

        Parameters:
            None

        Returns:
            None
        """

        if self.mp < 200:
            print(f"{self.name} doesn't have enough mp")
        else:
            self.hp *= 2
            self.mp -= 200
            print(f"{self.name} now has {self.hp} hp")


class AgilityHero(Hero):

    def __init__(self, name, hp, mp, damage, strength_growth, agility_growth, intelligence_growth):
        """
        The constructor of the < StrengthHero > class.
        Use < super() > to initialize the attributes of the parent class.
        Add a new attribute < main_attribute >.
        The < main_attribute > of an agility hero should be "agility".

        Parameters:
            name (str): The name of the hero.
            hp (float): The health points of the hero.
            mp (float): The magic points of the hero.
            damage (float): The damage of the hero.
            strength_growth (float): The strength gain per level of the hero.
            agility_growth (float): The agility gain per level of the hero.
            intelligence_growth (float): The intelligence gain per level of the hero.

        Returns:
            None
        """

        super().__init__(name, hp, mp, damage, strength_growth, agility_growth, intelligence_growth)
        self.main_attribute = "agility"


    def level_up(self):
        """
        This method would level a hero up:
        1. increase < level > by 1
        2. increase < hp > by 10 * < strength_growth >
        3. increase < mp > by 10 * < intelligence_growth >
        4. increase < damage > by 1 * < main_attribute > growth

        Parameters:
            None

        Returns:
            None
        """

        self.level += 1
        self.hp += 10*self.strength_growth
        self.mp += 10*self.intelligence_growth
        self.damage += 1*self.agility_growth


    def ability(self):
        """
        This method would double hero's < damage > at the cost of 300 < mp >.
        If the hero's < mp > is less than 300, this method should print "< name > doesn't have enough mp"
        If the hero's < mp > is equal or greater than 300, this method would double its < damage >,
        reduce its < mp > by 300 and print "< name > now has < damage > damage"

        Parameters:
            None

        Returns:
            None
        """

        if self.mp < 300:
            print(f"{self.name} doesn't have enough mp")
        else:
            self.damage *= 2
            self.mp -= 300
            print(f"{self.name} now has {self.damage} damage")


class IntelligenceHero(Hero):

    def __init__(self, name, hp, mp, damage, strength_growth, agility_growth, intelligence_growth):
        """
        The constructor of the < StrengthHero > class.
        Use < super() > to initialize the attributes of the parent class.
        Add a new attribute < main_attribute >.
        The < main_attribute > of an intelligence hero should be "intelligence".

        Parameters:
            name (str): The name of the hero.
            hp (float): The health points of the hero.
            mp (float): The magic points of the hero.
            damage (float): The damage of the hero.
            strength_growth (float): The strength gain per level of the hero.
            agility_growth (float): The agility gain per level of the hero.
            intelligence_growth (float): The intelligence gain per level of the hero.

        Returns:
            None
        """

        super().__init__(name, hp, mp, damage, strength_growth, agility_growth, intelligence_growth)
        self.main_attribute = "intelligence"


    def level_up(self):
        """
        This method would level a hero up:
        1. increase < level > by 1
        2. increase < hp > by 5 * < strength_growth >
        3. increase < mp > by 20 * < intelligence_growth >
        4. increase < damage > by 1 * < main_attribute > growth

        Parameters:
            None

        Returns:
            None
        """

        self.level += 1
        self.hp += 5*self.strength_growth
        self.mp += 20*self.intelligence_growth
        self.damage += 1*self.intelligence_growth


    def ability(self):
        """
        This method would transform 50% of < mp > into < hp > and 50% of < mp > into damage.
        After transformation, < mp > should be 0.
        Then print "< name > now has < hp > hp and < damage > damage"

        Parameters:
            None

        Returns:
            None
        """

        self.hp += self.mp * 0.5
        self.damage += self.mp * 0.5
        self.mp = 0
        print(f"{self.name} now has {self.hp} hp and {self.damage} damage")


# Now let's simulate the game!

def main(heroes):
    """
    In this function, you will create instances of heroes. You'll make heroes level up,
    use their abilities, and attack each other.

    Refer to Problem Set 08 README.md for instructions and tips.

    Parameters:
        heroes (list): A list of dictionaries. Each dictionary describes the attributes of a hero.

    Returns:
        winners (list): A list of objects who survive after the fight.
    """

    # 5.1: Create instances of < Hero >

    all_heroes = {}

    for d in heroes:
        main_attribute = d["main_attribute"]
        name = d["name"]
        hp = d["base_hp"]
        mp = d["base_mp"]
        damage = d["base_damage"]
        strength_growth = d["strength_growth_per_level"]
        agility_growth = d["agility_growth_per_level"]
        intelligence_growth = d["intelligence_growth_per_level"]

        if main_attribute == "strength":
            instance = StrengthHero(name, hp, mp, damage, strength_growth, agility_growth, intelligence_growth)
        elif main_attribute == "agility":
            instance = AgilityHero(name, hp, mp, damage, strength_growth, agility_growth, intelligence_growth)
        elif main_attribute == "intelligence":
            instance = IntelligenceHero(name, hp, mp, damage, strength_growth, agility_growth, intelligence_growth)
        all_heroes[name] = instance


    # 5.2: Level up your heroes

    for v in all_heroes.values():
        for _ in range(25):
            # print(v.name, v.damage)
            v.level_up()

    # Uncomment the for loop below when you finish the above steps

    for v in all_heroes.values():
        print(v)


    # 5.3: Simulate a fight!

    for k1, v in all_heroes.items():
        v.ability()
        for k2, other in all_heroes.items():
            if k1 != k2:
                v.attack(other)


    # 5.4: Find the winners!

    winners = []

    for v in all_heroes.values():
        if not v.is_dead():
            winners.append(v)

    return winners


# RECAP

# Now let's do a recap of this Problem Set:
# Why do we need the < Hero > class? These heroes have attributes and methods that do
# not change between the different types of heros, like the < attack() > method. We need
# the child classes < StrengthHero >,  < AgilityHero >, and < IntelligenceHero > because the
# different types of heroes have different ways of leveling up and abilities seen in
# the < level_up() > and < ability() > methods.

# That's the power of inheritance and overriding. We use a parent class to manage the
# common attributes and methods, and then use the child class' attributes and methods
# to specify things that only apply to itself and also to modify parent class methods
# that should act in different ways.

# The simulation has been simplified for you. In a real world game there would be a
# lot more attributes and methods to manage, that's why we need
# Object Oriented Programming, OOP, to better organize our code.


if __name__ == '__main__':
    main(heroes)
