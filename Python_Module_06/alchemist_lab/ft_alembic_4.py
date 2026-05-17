import alchemy

print("=== Alembic 4 ===")
print("Accessing the alchemy module using 'import alchemy'")
print(f"Testing create_air: {alchemy.create_air()}")
print("Now show that not all functions can be reached and raise an Exeption!")

try:
    # This will trigger our custom __getattr__ error!
    print(f"Testing the hidden create_earth: {alchemy.create_earth()}")
except AttributeError as e:
    print(f"AttributeError: {e}")
