from wordcloud import WordCloud
import matplotlib.pyplot as plt

file_path = 'data/movies.txt'


class WordCloudGenerator:
    def __init__(self, file_path: str):
        with open(file_path) as f:
            self.text = f.read()

    def run(self, output_name: str, **kwargs) -> None: #Kwargs are used to set as many input arguments which a class supports and user wants to add them.
        """
        Generate a word cloud image.

        :param output_name: The name of the output file.
        """
        WordCloud(**kwargs).generate(self.text).to_file(output_name)

        # plt.figure(figsize=(7, 5))
        # plt.imshow(wc_gen)
        # plt.axis('off')
        # plt.savefig("wordcloud.png",dpi=500)


if __name__ == '__main__':

    wc_gen = WordCloudGenerator(file_path)
    wc_gen.run(
        output_name='output.png',
        width=600, height=400,
        background_color='white',
    )