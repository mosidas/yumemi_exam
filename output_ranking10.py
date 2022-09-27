import csv
import sys
import time

time_start = time.time()

# ｃｓｖファイルを読み込む
filePath = sys.argv[1]
csv_file = open(filePath)
f = csv.reader(csv_file)
# ヘッダを捨てる
header = next(f)

# プレイヤーごとのトータルスコアとプレイ回数を求める
scores = dict()
for row in f:
    if row[1] not in scores:
        scores[row[1]] = dict()

    if 'count' not in scores[row[1]]:
        scores[row[1]]['count'] = 0
        scores[row[1]]['total'] = 0

    scores[row[1]]['count'] += 1
    scores[row[1]]['total'] += int(row[2])

# プレイヤーごとの平均スコアを求める
average = dict()
for player in scores.keys():
    average[player] = round(float(scores[player]['total']) / scores[player]['count'])

# スコアの降順にソートする
ranking = sorted(average.items(), key=lambda x:x[1], reverse=True)

# スコアのランキングTOP10を出力する
rank = 0
cnt = 0
pre_score = -1
print('rank,player_id,mean_score')
for data in ranking:
    id, score = data
    cnt += 1
    if pre_score != score and cnt > 10:
        break

    if pre_score != score:
        rank += 1

    print(str(rank) + "," + id + "," + str(score))
    pre_score = score

time_end = time.time()
tim = time_end - time_start
print(tim)
