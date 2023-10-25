import pcbnew
import csv
import math


board = pcbnew.GetBoard()

with open('hip_constellation_line_star.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        # 行から必要なデータを抽出
        ra = (float(row[1]) * 15) + (float(row[2]) * (15 / 60)) + (float(row[3]) * (15 / 3600))
        dec = float(row[4]) + (float(row[5]) * (1 / 60)) + (float(row[6]) * (1 / 3600))
        magnutude = float(row[7])
        number = row[0]

        # 平面座標に変換
        x = -ra * 1_000_000
        y = -dec * 1_000_000

        # 等級を適当な曲線でサイズに変換
        size = (2 * math.e ** (-0.2 * magnutude)) * 1_000_000

        via = pcbnew.PCB_VIA(board)
        via.SetX(int(x))
        via.SetY(int(y))
        via.SetWidth(int(size))
        via.SetDrill(int(size * (1 / 1.5)))
        board.Add(via)

        text = pcbnew.PCB_TEXT(board)
        text.SetX(int(x + (size / 2 + 1)))
        text.SetY(int(y))
        text.SetHorizJustify(pcbnew.GR_TEXT_H_ALIGN_LEFT)
        text.SetLayer(pcbnew.F_Fab)
        text.SetText(number)
        board.Add(text)


        pcbnew.Refresh()
