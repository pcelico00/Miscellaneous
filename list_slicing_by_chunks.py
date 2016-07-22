def slice_list_into_list_of_sublist(data, start=0, chunk_size=1,skip=1):
    data = data[start:]

    chunks = []
    while len(data)> chunk_size:
        chunks += [data[:chunk_size]]
        data = data[chunk_size + skip:]
    if len(data) == chunk_size:
        chunks += [data]

    return chunks

if __name__ == "__main__":
    a = bytearray(b'\x1e\x04?\x80\x00\x00\x1f\x04\x00\x00\x00\x00')
    assert(slice_list_into_list_of_sublist(a,2,4,2) == [bytearray(b'?\x80\x00\x00'), bytearray(b'\x00\x00\x00\x00')])
    assert(slice_list_into_list_of_sublist(a,0,2,2) == [bytearray(b'\x1e\x04'), bytearray(b'\x00\x00'), bytearray(b'\x00\x00')])
    b = range(0,10,1)
    assert(slice_list_into_list_of_sublist(b,0,2,2) == [[0,1],[4,5],[8,9]])