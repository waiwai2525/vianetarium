import pcbnew


board = pcbnew.GetBoard()

via = pcbnew.PCB_VIA(board)
via.SetX(0)
via.SetY(0)
via.SetWidth(int(1.5 * 1_000_000))
via.SetDrill(int(1.0 * 1_000_000))

board.Add(via)


pcbnew.Refresh()
print("end")