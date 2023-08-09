from PIL import Image

word_matrix = Image.open("word_matrix.png")
matrix_size = word_matrix.size

mask = Image.open("mask.png").convert("RGB")
mask_size = mask.size

print(matrix_size, mask_size)


mask = mask.resize((1015, 559))
mask.putalpha(128)


word_matrix.paste(im=mask, box=(0, 0), mask=mask)

word_matrix.show()
