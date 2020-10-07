import unittest, inspect, re, csv
from gradescope_utils.autograder_utils.decorators import weight
from problem_set_07 import SuperHeroine, write_to_file, main

# Setup variables
STU_BLACK_WIDOW = SuperHeroine(
    "Black Widow",
    "Natasha Romanoff",
    "Avengers",
    "Green",
    "Red",
    "Russia"
    )
FXT_BLACK_WIDOW = {
    "name": "Black Widow",
    "full_name": "Natasha Romanoff",
    "team": "Avengers",
    "eye_color": "Green",
    "hair_color": "Red",
    "base": "Russia",
    "powers": [],
    "nemeses": []
    }
FXT_TEST_STRING = """test = SuperHeroine("Black Widow", "Natasha Romanoff", "Avengers", "Green", "Red", "Russia")"""

# Unit tests
class ProblemSet07(unittest.TestCase):

    @weight(24)
    def test_problem_1(self):
        """Problem 1. Test SuperHeroine constructor."""

        stu_variables = vars(STU_BLACK_WIDOW)

        self.assertEqual(
            stu_variables,
            FXT_BLACK_WIDOW,
            """\nERROR: We tried to create an instance of < SuperHeroine > with the following data:

            {FXT_TEST_STRING}

            but something went wrong. Try creating a test case in your code exactly like the
            one we made above and see if all of the instance variables are as they should be.
            Make sure you remember to create empty lists for the < powers > and < nemeses >
            instance variables in your constructor (i.e. __init__()).\n"""
            )


    @weight(24)
    def test_problem_2(self):
        """Problem 2. Test SuperHeroine __str__()."""

        STU_BLACK_WIDOW.powers.append("Super Reflexes")
        stu_string = str(STU_BLACK_WIDOW)

        fxt_string = "Black Widow is a member of the Avengers and possesses the following powers:\n['Super Reflexes']"

        self.assertEqual(
            stu_string,
            fxt_string,
            f"""\nERROR: We created an instance of < SuperHeroine > and then added some powers as below:

            {FXT_TEST_STRING}
            test.powers.append("Super Reflexes")

            and we expected the string representation to be:

            {fxt_string}

            but got this instead:

            {stu_string}\n"""
            )

        STU_BLACK_WIDOW.powers.clear()


    @weight(24)
    def test_problem_3(self):
        """Problem 3. Test SuperHeroine add_power() method."""

        STU_BLACK_WIDOW.add_power("Super Reflexes")
        stu_power = STU_BLACK_WIDOW.powers

        fxt_power = ["Super Reflexes"]

        self.assertEqual(
            stu_power,
            fxt_power,
            f"""\nERROR: We created an instance of < SuperHeroine > and then added a power as below:

            {FXT_TEST_STRING}
            test.add_power("Super Reflexes")

            and we expected test.powers to be:

            {fxt_power}

            but got this instead:

            {stu_power}\n"""
            )

        STU_BLACK_WIDOW.powers.clear()


    @weight(24)
    def test_problem_4(self):
        """Problem 4. Test SuperHeroine add_nemesis() method."""

        STU_BLACK_WIDOW.add_nemesis("Taskmaster")
        stu_nemesis = STU_BLACK_WIDOW.nemeses

        fxt_nemesis = ["Taskmaster"]

        self.assertEqual(
            stu_nemesis,
            fxt_nemesis,
            f"""\nERROR: We created an instance of < SuperHeroine > and then added a nemesis as below:

            {FXT_TEST_STRING}
            test.add_nemesis("Taskmaster")

            and we expected test.nemeses to be:

            {fxt_nemesis}

            but got this instead:

            {stu_nemesis}\n"""
            )

        STU_BLACK_WIDOW.nemeses.clear()


    @weight(24)
    def test_problem_5(self):
        """Problem 5. Test write_to_file()."""

        STU_BLACK_WIDOW.powers.append("Super Reflexes")
        write_to_file('test.txt', STU_BLACK_WIDOW)

        with open('test.txt','r') as f:
            stu_write = f.read()

        fxt_write = "Black Widow is a member of the Avengers and possesses the following powers:\n['Super Reflexes']"

        self.assertEqual(
            stu_write,
            fxt_write,
            f"""\nERROR: We created an instance of < SuperHeroine > and then added a power and wrote it as below:

            {FXT_TEST_STRING}
            test.powers.append("Super Reflexes")
            write_to_file('test.txt',test)

            and we expected contents of test.txt to be:

            {fxt_write}

            but got this instead:

            {stu_write}\n"""
            )

        STU_BLACK_WIDOW.powers.clear()


    @weight(10)
    def test_problem_6_scarlet(self):
        """Problem 6. Test scarlet_witch.txt in main()."""

        main()

        fxt_scarlet = """Scarlet Witch is a member of the X-men; Avengers and possesses the following powers:
['agility', 'dimensional awareness', 'flight', 'longevity', 'energy blasts', 'teleportation', 'telekinesis', 'magic', 'astral projection', 'energy constructs', 'probability manipulation', 'levitation', 'illusions', 'reality warping']"""

        with open("scarlet_witch.txt",'r') as f:
            stu_scarlet = f.read()

        self.assertEqual(
            stu_scarlet,
            fxt_scarlet,
            f"""\nERROR: We expected your 'scarlet_witch.txt' file to consist of:

            {fxt_scarlet}

            but instead we found:

            {stu_scarlet}\n"""
            )


    @weight(10)
    def test_problem_6_jessica(self):
        """Problem 6. Test jessica_jones.txt in main()."""

        main()

        fxt_jessica = """Jessica Jones is a member of the Defenders and possesses the following powers:
['durability', 'flight', 'super strength', 'super speed', 'telepathy resistance']"""

        with open("jessica_jones.txt",'r') as f:
            stu_jessica = f.read()

        self.assertEqual(
            stu_jessica,
            fxt_jessica,
            f"""\nERROR: We expected your 'jessica_jones.txt' file to consist of:

            {fxt_jessica}

            but instead we found:

            {stu_jessica}\n"""
            )


    @weight(10)
    def test_problem_6_storm(self):
        """Problem 6. Test storm.txt in main()."""

        main()

        fxt_storm = """Storm is a member of the X-men and possesses the following powers:
['cold resistance', 'flight', 'intelligence', 'enhanced senses', 'empathy', 'heat resistance', 'telepathy resistance', 'weather control']"""

        with open('storm.txt','r') as f:
            stu_storm = f.read()

        self.assertEqual(
            stu_storm,
            fxt_storm,
            f"""\nERROR: We expected your 'storm.txt' file to consist of:

            {fxt_storm}

            but instead we found:

            {stu_storm}\n"""
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
