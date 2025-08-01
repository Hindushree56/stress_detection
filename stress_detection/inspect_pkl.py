import pickle

file_path = "WESAD/S10/S10.pkl"  # Adjust the path if needed

with open(file_path, 'rb') as f:
    data = pickle.load(f)

print("\nTop-level keys:", data.keys())

if 'signal' in data:
    print("Available signal keys:", data['signal'].keys())

    if 'chest' in data['signal']:
        print("✅ Chest signals:", data['signal']['chest'].keys())
    else:
        print("❌ No chest signals found.")

    if 'wrist' in data['signal']:
        print("✅ Wrist signals:", data['signal']['wrist'].keys())
    else:
        print("❌ No wrist signals found.")
else:
    print("❌ No 'signal' key found in the .pkl file.")
