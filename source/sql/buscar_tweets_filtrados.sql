select
    q.*
from
    (select
        to_tsvector('english', tweet ->> 'text') @@ to_tsquery(%(tsquery)s) as tweet_boolean_ts,
        tweet #>> '{user, name}' as tweet_name,
        tweet #>> '{user, screen_name}' as tweet_user,
        tweet ->> 'text' as tweet_text,
        tweet ->> 'retweet_count' as tweet_retweet_count,
        tweet ->> 'favorite_count' as tweet_favorite_count,
        tweet #>> '{user, followers_count}' as tweet_followers_count,
        tweet ->> 'lang' as tweet_lang
    from
        twitter
    order by
        id_tweet
    ) as q
where
    q.tweet_boolean_ts is %(boolean_ts)s;
