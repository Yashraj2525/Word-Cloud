# Word-Cloud Generator

This script generates a word cloud image from text input. It allows creating a custom shaped word cloud by using a mask image.
Usage

The main steps are:

    Provide text input in a text file (sampletext.txt)
    Specify a mask image (cloud.png) to define word cloud shape
    Run the script:
    python WordCloud.py

  The output word cloud image (custom_wordcloud.png) will be displayed and can also be saved to file.

  A Jupyter Notebook (WordCloud.ipynb) is provided to demonstrate the code in action.

Customization


    The mask image should be a PNG with high contrast between the shape and background.
    Convert mask to grayscale before passing to WordCloud.
    Tune the WordCloud parameters like contour, colors, font sizes to get desired effect.
    Use enough words (max_words) to fill the shape.
    Display the generated array directly using matplotlib to avoid saving to disk.
    To save it as .png uncomment the code which i have mentioned already in the code.

Credits

Word cloud generation uses the excellent word_cloud library (https://github.com/amueller/word_cloud).

The sample code provided generates a basic word cloud. Please refer to word_cloud documentation for advanced usage and customization.
License

MIT License - feel free to reuse and modify the code as needed.
