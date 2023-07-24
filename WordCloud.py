import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image

# Read text
text = open('sampletext.txt').read()

# Read mask image
mask = np.array(Image.open('cloud.png').convert('L'))

# Create word cloud
wordcloud = WordCloud(mask=mask, contour_width=3, contour_color='black', stopwords=set(STOPWORDS),
                      background_color='white', max_words=200, min_font_size=10)

# Generate word cloud
wordcloud.generate(text)

# Get array representation To view the input after running the code instead of saving it to file
wc_array = wordcloud.to_array()

# To Save word cloud into png format uncomment the below line and comment the above line. So, it will save to the file named "custom_wordcloud.png"
# wordcloud.to_file('custom_wordcloud.png')

# Show word cloud
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
