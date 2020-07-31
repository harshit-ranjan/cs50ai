from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Add to baseknowledge that a person can either be a knight or a knave
baseknowledge = And(
    Or(AKnight, AKnave), Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave), Not(And(BKnight, BKnave)),
    Or(CKnight, CKnave), Not(And(CKnight, CKnave))
)

# Puzzle 0
# A says "I am both a knight and a knave."
Asays = And(AKnight, AKnave)
knowledge0 = And(
    baseknowledge,
    Biconditional(Asays, AKnight),
    Biconditional(Not(Asays), AKnave)
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
Asays = And(AKnave, BKnave)
knowledge1 = And(
    baseknowledge,
    Biconditional(Asays, AKnight),
    Biconditional(Not(Asays), AKnave)
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
Asays = Or(And(AKnight, BKnight), And(AKnave, BKnave))
Bsays = Or(And(AKnight, BKnave), And(AKnave, BKnight))
knowledge2 = And(
    baseknowledge,

    Biconditional(Asays, AKnight),
    Biconditional(Bsays, BKnight),

    Biconditional(Not(Asays), AKnave),
    Biconditional(Not(Bsays), BKnave)
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
Asays = And(Or(AKnight, AKnave), Not(And(AKnight, AKnave)))
Bsays = And(AKnave, CKnave)
Csays = And(AKnight)

knowledge3 = And(
    baseknowledge,
    Biconditional(Asays, AKnight),
    Biconditional(Bsays, BKnight),
    Biconditional(Csays, CKnight),

    Biconditional(Not(Asays), AKnave),
    Biconditional(Not(Bsays), BKnave),
    Biconditional(Not(Csays), CKnave)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
