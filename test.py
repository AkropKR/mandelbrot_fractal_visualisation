from PIL import Image

sample = Image.open('kirill.jpg')

print(size(sample))

type(sample)

sample.show()

resized_image = sample.resize((2200,2200))
resized_image.save('resized.jpg')