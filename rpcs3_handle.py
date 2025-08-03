import pymem

class rpcs3_mem():
    def __init__(self) -> None:
        self.process = pymem.Pymem("rpcs3.exe")
    
    def read_recipe(self):
        recipe = self.process.read_bytes(0x3018DE800, 6500)
        return recipe

    def write_recipe(self, recipe_bytes:bytes):
        self.process.write_bytes(0x3018DE800, recipe_bytes, 6500)
        self.process.write_bytes(0x3018E0800, b"\x00\x00\x1F\x40", 4)

if __name__ == "__main__":
    rpcs3 = rpcs3_mem()

    recipe_bytes = rpcs3.read_recipe()
    rpcs3.write_recipe(recipe_bytes)
