import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image

# Read text
text = open('sampletext1.txt').read()

# Read mask image
mask = np.array(Image.open('cloud.png').convert('L'))

# Create word cloud
wordcloud = WordCloud(mask=mask, contour_width=3, contour_color='black', stopwords=set(STOPWORDS),
                      background_color='white', max_words=200, min_font_size=10)

# Generate word cloud
wordcloud.generate(text)

# Get array representation
wc_array = wordcloud.to_array()

# Save word cloud instead of showing the output it save to the file name "custom_wordcloud.png"
# wordcloud.to_file('custom_wordcloud.png')

# Show word cloud
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
