select
    t.*
from
    twitter t
where
    t.id_tweet = %(id_tweet)s;