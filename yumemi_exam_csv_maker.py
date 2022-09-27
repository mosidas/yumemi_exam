import csv
import os
import random
import sys

output_path = os.path.join(os.path.dirname(__file__), sys.argv[1])
size = sys.argv[2]

# 書き込み
with open(output_path, 'w', newline="") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow(["create_timestamp", "player_id", "score"])
    for i in range(int(size)):
        create_on = "2022/01/01 11:11:11"
        player_id = "player" + str(random.randrange( 0, 9999 )).zfill(4)
        score = str(random.randrange( 100, 10000 ))
        writer.writerow([create_on, player_id, score])
