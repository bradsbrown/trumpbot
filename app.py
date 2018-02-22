import twitter_scraper
import markovify


def trump_tweets(pages=25):
    return '\n'.join([t for t in twitter_scraper.get_tweets('realdonaldtrump', pages=pages)])


def insanity(tweets):
    return markovify.Text(tweets).make_short_sentence(280)


if __name__ == '__main__':
    print(insanity(trump_tweets()))
