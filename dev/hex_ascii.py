# CONSTANTS 
HEX_OFFSET = 7
HEX_UNIT = 16
HEX_TO_ASCII = dict()

def generate_hex_ascii_mapping():
    # following https://www.ascii-code.com/ 
    # unprintable chars that should default to '.'
    # i.e. first 32 chars  
    for i in range(32, 128):
        hexed = hex(i)[2:]
        hexed = '0' + hexed if len(hexed) == 1 else hexed
        key  = bytearray.fromhex(hexed)
        HEX_TO_ASCII[hexed] = key.decode()


def serialize_hex_and_ascii(start, end, section):
    hex_out, ascii_out = [], []
    for j in range(start, end, 2):
        hex_out.append(section[j:j+2])
        ascii_out.append(HEX_TO_ASCII.get(section[j:j+2], '.') )
    assert(len(hex_out) == len(ascii_out))
    return " ".join(hex_out), "".join(ascii_out)


def clean_ascii(ascii_line): 
    return f'|{ascii_line}|'



generate_hex_ascii_mapping()
