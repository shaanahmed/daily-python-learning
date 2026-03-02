# %% using module
from ferrari_module import Ferrari

car1 = Ferrari("Roma Spider", 2019,"Blu Pozzi", False)
car2 = Ferrari("AmalFi", 2026,"Bianco Avus", True)

print(car1.model)
print(car2.model)

car1.describe()
car1.drive()

print(80*"_")

car2.repair()
car2.describe()

print(80*"_")

print(Ferrari.total_collection())


# %%
