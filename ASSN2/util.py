import bitio
import huffman
import pickle


def read_tree(tree_stream):
    d = pickle.load(tree_stream)
    return d
    pass


def write_tree(tree, tree_stream):
    pickle.dump(tree, tree_stream)
    pass


def decode_byte(tree, bitreader):
    check = True
    while check:

        # reads only one bit
        bit = bitreader.readbit()
        # 1 is for right and 0 is for left side of the tree.
        if bit == 1:
            tree = tree.getRight()
        elif bit == 0:
            tree = tree.getLeft()

        # When the desired leaf is reached, stops the loop and returns that
        # leaf value.
        if isinstance(tree, huffman.TreeLeaf):
            check = False
            return tree.getValue()
    pass


def decompress(compressed, uncompressed):

    # creating a tree
    tree = read_tree(compressed)

    br = bitio.BitReader(compressed)
    bw = bitio.BitWriter(uncompressed)

    decoded_byte = decode_byte(tree, br)

    # begins to write the decoded bits until EOF is reached
    while decoded_byte is not None:
        try:
            bw.writebits(decoded_byte, 8)
            decoded_byte = decode_byte(tree, br)
        except EOFError:
            decoded_byte = None
    pass


def compress(tree, uncompressed, compressed):

    write_tree(tree, compressed)

    encoding_table = huffman.make_encoding_table(tree)

    br = bitio.BitReader(uncompressed)
    bw = bitio.BitWriter(compressed)

    check = True
    while check:
        try:
            # reading 8 bits to 1 byte
            byte = br.readbits(8)

            # writing the "code" bitwise
            for bit in encoding_table[byte]:
                bw.writebit(bit)

        # marks compressed files with None to indicate the End of that file/
        # EOF.
        except EOFError:
            check = False

            # This for loops write None manully for the indication of the EOF
            # for the decompressor.
            for bit in encoding_table[None]:
                bw.writebit(bit)

    bw.flush()
    pass