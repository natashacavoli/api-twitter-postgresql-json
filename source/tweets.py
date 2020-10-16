#!/usr/bin/python
from client import Client
from tweets_model import Tweets as TweetsModel
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as pyplot
import json
import re


class Tweets(object):
    """Class Tweets."""

    _model = TweetsModel(id="model")

    def __init__(self, id):
        """Init."""
        self.id = id

    def inserir_tweets(self, search,
                       lang=None,
                       result_type=None,
                       count=None):
        """Insere tweets."""
        client = Client(id="client")

        if not count:
            count = 5

        tweets = client.get_tweets_json(
            search=search,
            lang=lang,
            result_type=result_type,
            count=count)

        tweets = tweets['statuses']

        for t in tweets:
            t['text'] = t['text'].replace("'", "")

            t = json.dumps(t)

            self._model.inserir_tweets(
                tweet=t, busca=search)

        print "OK"

    def _tratar_tweets(self, tweet_text):
        """Trata os tweets."""
        _r = r"[A-Z]+:\/\/[A-Z]+(\.[A-Z]+)+[^\s]+|@[A-Z]+[^\s]+"

        text = ""

        text = text + tweet_text.lower()
        text = re.sub(_r, "", text, flags=re.IGNORECASE)

        return text

    def gerar_imagem(self, busca, tsquery=''):
        """Gera um wordcloud e uma imagem."""
        _df = self.buscar_tweets(
            busca=busca,
            tsquery=tsquery)

        _tweet_text = _df['tweet_text']

        _r = ""
        for t in _tweet_text:
            _r = _r + self._tratar_tweets(tweet_text=t)

        _stopwords = set(STOPWORDS)
        _stopwords.update(["rt", ",", "."])

        _wordcloud = WordCloud(
            stopwords=_stopwords).generate(text=_r)

        pyplot.imshow(_wordcloud, interpolation="bilinear")
        pyplot.axis("off")
        pyplot.show()

    def buscar_tweets(self, busca, tsquery='', boolean_ts=True):
        """Busca os tweets."""
        if not tsquery:
            boolean_ts = False

        df = self._model.buscar_tweets_filtrados(
            tsquery=tsquery, boolean_ts=boolean_ts)

        return df
