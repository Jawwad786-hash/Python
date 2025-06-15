print("Mohd.Jawwad Ali Farooqui, USN:1AY24AI070, SEC:O")
class Kangaroo:
    def __init__(self):
        # Each kangaroo gets its own pouch list
        self.pouch_contents = []
    def put_in_pouch(self, item):
        self.pouch_contents.append(item)
    def __str__(self):
        contents = []
        for item in self.pouch_contents:
            if isinstance(item, Kangaroo):
                # Indent nested kangaroos
                contents.append("  " + str(item).replace("\n", "\n  "))
            else:
                contents.append(str(item))
        return "Kangaroo with pouch contents:\n" + "\n".join(contents)
# ----------- Test Code -----------
if __name__ == "__main__":
    kanga = Kangaroo()
    roo = Kangaroo()
    kanga.put_in_pouch("bottle")
    kanga.put_in_pouch("snack")
    kanga.put_in_pouch(roo)
    print("Kanga:")
    print(kanga)
    print("\nRoo:")
    print(roo)
