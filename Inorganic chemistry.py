
# Inorganic Chemistry Assistant

elements = {
    "Hydrogen": (1, "H"),
    "Helium": (2, "He"),
    "Lithium": (3, "Li"),
    "Carbon": (6, "C"),
    "Nitrogen": (7, "N"),
    "Oxygen": (8, "O"),
    "Sodium": (11, "Na"),
    "Magnesium": (12, "Mg"),
    "Aluminium": (13, "Al"),
    "Chlorine": (17, "Cl"),
    "Iron": (26, "Fe"),
    "Copper": (29, "Cu"),
    "Silver": (47, "Ag"),
    "Gold": (79, "Au")
}

print("🧪 INORGANIC CHEMISTRY ASSISTANT")
print("--------------------------------")

name = input("Enter an element name: ").strip().capitalize()

if name in elements:
    atomic_number, symbol = elements[name]

    print("\nElement:", name)
    print("Symbol:", symbol)
    print("Atomic Number:", atomic_number)
else:
    print("Element not found. Please try again!")
