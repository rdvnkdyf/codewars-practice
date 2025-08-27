from preloaded import LOVE_LANGUAGES

def love_language(partner, weeks):
    """
    Finds the main love language of a partner by trying each language
    and counting positive responses.

    Args:
        partner: An object with a 'response' method that returns a string ('positive' or 'neutral').
        weeks: The number of weeks to test.

    Returns:
        The main love language as a string.
    """
    
    positive_counts = {lang: 0 for lang in LOVE_LANGUAGES}
    
    total_tries = weeks * 7

    for i in range(total_tries):
        lang_to_try = LOVE_LANGUAGES[i % len(LOVE_LANGUAGES)]
        
        response = partner.response(lang_to_try)
        
        if response == "positive":
            positive_counts[lang_to_try] += 1

    main_language = max(positive_counts, key=positive_counts.get)