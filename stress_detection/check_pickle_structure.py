import pickle

file_path = "WESAD/S10/S10.pkl"  # Change to any existing file path

with open(file_path, 'rb') as f:
    data = pickle.load(f)

print("Top-level keys:", data.keys())

if 'signal' in data:
    print("Signal keys:", data['signal'].keys())

    if 'chest' in data['signal']:
        print("Chest signals:", data['signal']['chest'].keys())
    else:
        print("❌ No chest data found.")
        
    if 'wrist' in data['signal']:
        print("✅ Wrist signals available:", data['signal']['wrist'].keys())
else:
    print("❌ No signal key found.")
