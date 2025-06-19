def checkmate(board_str):
    try:
        board = [list(row) for row in board_str.strip().splitlines()]
        size = len(board)

        # หาตำแหน่งของ King
        king_pos = None
        for i in range(size):
            for j in range(size):
                if board[i][j] == 'K':
                    king_pos = (i, j)
        if not king_pos:
            print("Fail")
            return

        xk, yk = king_pos

        def within(x, y):
            return 0 <= x < size and 0 <= y < size

        # ตรวจจาก Rook และ Queen แนวตรง
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            x, y = xk + dx, yk + dy
            while within(x, y):
                if board[x][y] == '.':
                    x += dx
                    y += dy
                elif board[x][y] in ('R', 'Q'):
                    print("Success")
                    return
                else:
                    break

        # ตรวจจาก Bishop และ Queen แนวทแยง
        for dx, dy in [(-1,-1),(-1,1),(1,-1),(1,1)]:
            x, y = xk + dx, yk + dy
            while within(x, y):
                if board[x][y] == '.':
                    x += dx
                    y += dy
                elif board[x][y] in ('B', 'Q'):
                    print("Success")
                    return
                else:
                    break

        # ตรวจจาก Knight
        for dx, dy in [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]:
            x, y = xk + dx, yk + dy
            if within(x, y) and board[x][y] == 'N':
                print("Success")
                return

        # ตรวจจาก Pawn (สมมุติ Pawn เดินลง)
        for dy in [-1, 1]:
            x, y = xk - 1, yk + dy
            if within(x, y) and board[x][y] == 'P':
                print("Success")
                return

        print("Fail")
    except:
        pass  # ตามข้อกำหนด ให้คืน control แบบเงียบ ๆ
def checkmate(board_str):
    try:
        board = [list(row) for row in board_str.strip().splitlines()]
        size = len(board)

        king_pos = None
        for i in range(size):
            for j in range(size):
                if board[i][j] == 'K':
                    king_pos = (i, j)
        if not king_pos:
            print("Fail")
            return

        xk, yk = king_pos

        def within(x, y):
            return 0 <= x < size and 0 <= y < size

        # Rook & Queen (แนวตรง)
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            x, y = xk + dx, yk + dy
            while within(x, y):
                if board[x][y] == '.':
                    x += dx
                    y += dy
                elif board[x][y] in ('R', 'Q'):
                    print("Success")
                    return
                else:
                    break

        # Bishop & Queen (ทแยง)
        for dx, dy in [(-1,-1),(-1,1),(1,-1),(1,1)]:
            x, y = xk + dx, yk + dy
            while within(x, y):
                if board[x][y] == '.':
                    x += dx
                    y += dy
                elif board[x][y] in ('B', 'Q'):
                    print("Success")
                    return
                else:
                    break

        # Knight
        for dx, dy in [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]:
            x, y = xk + dx, yk + dy
            if within(x, y) and board[x][y] == 'N':
                print("Success")
                return

        # Pawn (สมมุติว่ามาจากด้านบน → เดินลง)
        for dy in [-1, 1]:
            x, y = xk - 1, yk + dy
            if within(x, y) and board[x][y] == 'P':
                print("Success")
                return

        print("Fail")
    except:
        pass  # ตาม requirement: undefined behavior = return control เงียบ ๆ
