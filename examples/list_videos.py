import os
from collections import defaultdict

BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Tricks')

video_counts = defaultdict(int)
for root, dirs, files in os.walk(BASE_DIR):
    for fname in files:
        if fname.lower().endswith('.mov'):
            label = os.path.basename(root)
            video_counts[label] += 1

for label, count in sorted(video_counts.items()):
    print(f'{label}: {count} videos')
