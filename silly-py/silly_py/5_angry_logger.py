# https://github.com/GitToby/angry-logger
from collections import Counter

import angry_logger

angry_logger.go_to_town(potty_mouth=False)

import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)-8s %(message)s")
log = logging.getLogger(__name__)


def do_analysis(text):
    paragraphs = [l for l in text if l != '\n']
    num_paras = len(paragraphs)
    if num_paras > 20:
        log.warning(f"Careful, this is a long book with {num_paras} lines!")

    sentences = " ".join(paragraphs).split(".")
    log.info(f'Your book has {len(sentences)} sentences in.')
    char_dist = Counter("".join(paragraphs).lower().replace(" ", ''))
    log.info(f'Here is the most common char: {char_dist.most_common()[0]}.')
    log.info(f'This should take about {len(sentences) // 12} mins to read')
    log.info('Here is the first section:')
    for sentence in sentences[:3]:
        log.info(sentence)


if __name__ == '__main__':
    log.info("hello world")
    log.info("This is a demo in logging")
    log.info("lets read my file shall we?")

    try:
        with open('data/book.txt') as f:
            log.debug('opening file')
            my_text = f.readlines()
        log.debug('starting analysis')
        do_analysis(my_text)
    except FileNotFoundError as e:
        log.error('We couldn\'t find that file!!!')
