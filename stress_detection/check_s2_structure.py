import pickle

with open("WESAD/S2/S2.pkl", "rb") as f:
    data = pickle.load(f)

print("Top-level keys:", data.keys())
print("\nSignal sources:", data['signal'].keys())

if 'chest' in data['signal']:
    print("\nChest keys:", data['signal']['chest'].keys())
else:
    print("Chest data not found")
