#!/usr/bin/python
import psycopg2
import pandas


class Tweets(object):
    """Class Tweets."""

    _c = psycopg2.connect("dbname=testes user=postgres")

    def __init__(self, id):
        """Init."""
        self.id = id

    def buscar_tweets(self, id_tweet=None):
        """Busca os tweets."""
        query = open('sql/buscar_tweets.sql', 'r')
        query = query.read()

        _cursor = self._c.cursor()
        _cursor.execute(query, {"id_tweet": id_tweet})

        r = _cursor.fetchall()

        _cursor.close()

        return r

    def buscar_tweets_filtrados(self, tsquery, boolean_ts):
        """Busca os tweets."""
        query = open('sql/buscar_tweets_filtrados.sql', 'r')
        query = query.read()

        _cursor = self._c.cursor()
        _cursor.execute(
            query, {"tsquery": tsquery, "boolean_ts": boolean_ts})

        _names = [n[0] for n in _cursor.description]

        _r = _cursor.fetchall()

        _cursor.close()

        return pandas.DataFrame(_r, columns=_names)

    def inserir_tweets(self, tweet, busca):
        """Busca os tweets."""
        query = open('sql/inserir_tweet.sql', 'r')
        query = query.read()

        _cursor = self._c.cursor()
        _cursor.execute(query, {"tweet": tweet, "busca": busca})

        self._c.commit()

        _cursor.close()

        return

    def remover_tweet(self, id_tweet=None):
        """Busca os tweets."""
        query = open('sql/remover_tweets.sql', 'r')
        query = query.read()

        _cursor = self._c.cursor()
        _cursor.execute(query, {"id_tweet": id_tweet})

        self._c.commit()

        _cursor.close()

        return
