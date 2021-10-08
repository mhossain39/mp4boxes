import struct

def find_boxes(f, start_offset=0, end_offset=float("inf")):
    s = struct.Struct("> I 4s") 
    boxes = {}
    sboxes = {}
    offset = start_offset
    f.seek(offset, 0)
    while offset < end_offset:
        data = f.read(8)               # read box header
        if data == b"": break          # EOF
        length, text = s.unpack(data)
        f.seek(length - 8, 1)          # skip to next box
        if text ==b'moof' or text==b'traf':
          sboxes = 	find_boxes(f, offset + 8, offset + length)	
        boxes[text] = (offset, offset + length,sboxes)
        offset += length
    return boxes

	
	
with open("text0.mp4", "rb") as f:
	boxes = find_boxes(f)
	print(boxes)
