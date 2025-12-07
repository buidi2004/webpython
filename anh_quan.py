"""
File chứa ảnh quân cờ bằng Unicode art và ASCII art
"""

# Unicode art các quân cờ
ANH_UNICODE = {
    'King_white': '♔',
    'Queen_white': '♕',
    'Rook_white': '♖',
    'Bishop_white': '♗',
    'Knight_white': '♘',
    'Pawn_white': '♙',
    'King_black': '♚',
    'Queen_black': '♛',
    'Rook_black': '♜',
    'Bishop_black': '♝',
    'Knight_black': '♞',
    'Pawn_black': '♟',
}

# ASCII art các quân cờ (mỗi quân là một grid 5x5)
ANH_ASCII = {
    'King_white': [
        '  K  ',
        ' /|\\ ',
        '/ | \\',
        '  |  ',
        ' / \\ ',
    ],
    'Queen_white': [
        ' ♛ ♛ ',
        '  Q  ',
        ' /|\\ ',
        '/ | \\',
        ' / \\ ',
    ],
    'Rook_white': [
        '|   |',
        '| R |',
        '|   |',
        '|   |',
        '|   |',
    ],
    'Bishop_white': [
        '  B  ',
        ' / \\ ',
        '| o |',
        ' \\ / ',
        '  |  ',
    ],
    'Knight_white': [
        '  /~ ',
        ' / N ',
        '|    ',
        '|    ',
        ' \\  ',
    ],
    'Pawn_white': [
        '  P  ',
        '  |  ',
        ' /|\\ ',
        '  |  ',
        ' / \\ ',
    ],
    'King_black': [
        '  k  ',
        ' /|\\ ',
        '/ | \\',
        '  |  ',
        ' / \\ ',
    ],
    'Queen_black': [
        ' ♚ ♚ ',
        '  q  ',
        ' /|\\ ',
        '/ | \\',
        ' / \\ ',
    ],
    'Rook_black': [
        '|   |',
        '| r |',
        '|   |',
        '|   |',
        '|   |',
    ],
    'Bishop_black': [
        '  b  ',
        ' / \\ ',
        '| o |',
        ' \\ / ',
        '  |  ',
    ],
    'Knight_black': [
        '  /~ ',
        ' / n ',
        '|    ',
        '|    ',
        ' \\  ',
    ],
    'Pawn_black': [
        '  p  ',
        '  |  ',
        ' /|\\ ',
        '  |  ',
        ' / \\ ',
    ],
}


def lay_anh_unicode(ten_quan: str, mau: str) -> str:
    """Lấy ký hiệu Unicode của quân cờ.
    
    Args:
        ten_quan: 'King', 'Queen', 'Rook', 'Bishop', 'Knight', 'Pawn'
        mau: 'white' hoặc 'black'
    
    Returns:
        Ký hiệu Unicode (string)
    """
    key = f'{ten_quan}_{mau}'
    return ANH_UNICODE.get(key, '?')


def lay_anh_ascii(ten_quan: str, mau: str) -> list:
    """Lấy biểu diễn ASCII art của quân cờ.
    
    Args:
        ten_quan: 'King', 'Queen', 'Rook', 'Bishop', 'Knight', 'Pawn'
        mau: 'white' hoặc 'black'
    
    Returns:
        Danh sách 5 dòng chuỗi (ASCII art)
    """
    key = f'{ten_quan}_{mau}'
    return ANH_ASCII.get(key, ['  ?  ', '  ?  ', '  ?  ', '  ?  ', '  ?  '])


def in_ascii_art_bang(ten_quan: str, mau: str):
    """In ASCII art quân cờ ra console."""
    anh = lay_anh_ascii(ten_quan, mau)
    print(f"\n{ten_quan} ({mau}):")
    for dong in anh:
        print(dong)


def in_tat_ca_ascii():
    """In tất cả ASCII art các quân cờ."""
    types = ['King', 'Queen', 'Rook', 'Bishop', 'Knight', 'Pawn']
    colors = ['white', 'black']
    
    print("=" * 60)
    print("TẤT CẢ QUÂN CỜ - ASCII ART")
    print("=" * 60)
    
    for color in colors:
        print(f"\n--- {color.upper()} ---")
        for qtype in types:
            in_ascii_art_bang(qtype, color)


if __name__ == '__main__':
    # Ví dụ sử dụng
    print("Unicode ký hiệu:")
    for key, val in ANH_UNICODE.items():
        print(f"  {key}: {val}")
    
    print("\n" + "=" * 60)
    in_tat_ca_ascii()
