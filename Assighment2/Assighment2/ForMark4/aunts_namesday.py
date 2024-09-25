class AuntNamesday:
    def __init__(self):
        self.dislikes = {}
        self.color = {}

    def is_bipartite(self, start):
        stack = [start]
        self.color[start] = 0  

        while stack:
            guest = stack.pop()

            for disliked_guest in self.dislikes.get(guest, []):
                if disliked_guest not in self.color:
                    self.color[disliked_guest] = 1 - self.color[guest]
                    stack.append(disliked_guest)
                elif self.color[disliked_guest] == self.color[guest]:
                    return False
        return True

    def add_dislike(self, guest1, guest2):
        if guest1 not in self.dislikes:
            self.dislikes[guest1] = []
        if guest2 not in self.dislikes:
            self.dislikes[guest2] = []
        self.dislikes[guest1].append(guest2)
        self.dislikes[guest2].append(guest1)

    def assign_tables(self):#like main
        for guest in self.dislikes:
            if guest not in self.color:
                if not self.is_bipartite(guest):
                    return False
        return True

    def print_seating_arrangement(self):
        table1, table2 = [], []
        for guest, col in self.color.items():
            if col == 0:
                table1.append(guest)
            else:
                table2.append(guest)

        print("Table 1:", " ".join(table1))
        print("Table 2:", " ".join(table2))


if __name__ == "__main__":
    party = AuntNamesday()

    # Sample dislikes list
    party.add_dislike("Alice", "Bob")
    party.add_dislike("Alice", "Charlie")
    party.add_dislike("Bob", "David")
    party.add_dislike("Charlie", "David")

    if party.assign_tables():
        print("The seating arrangement is possible:")
        party.print_seating_arrangement()
    else:
        print("It is not possible to arrange the seating as per the given dislikes.")
