import requests

# It is recommended to use this header along with your request.
headers = {'Accept-Encoding': 'gzip,deflate'}

def wikidata_scraper(url):
    """
    Scrapes a Wikidata JSON page and returns a dictionary with the English
    Identifier, Label, and Description.

    Args:
        url (str): A string with a link to a Wikidata page in JSON format.

    Returns:
        dict: A dictionary with keys "ID", "LABEL", and "DESCRIPTION"
              containing the matching "en" values.
    """
    response = requests.get(url, headers=headers)
    data = response.json()

    # Extract the ID from the URL
    item_id = url.split('/')[-1].split('.')[0] # Assuming URL format like .../entity/Q42.json

    label = "No Label"
    description = "No Description"

    # Navigate the JSON to find the English label and description
    if 'entities' in data and item_id in data['entities']:
        entity = data['entities'][item_id]

        if 'labels' in entity and 'en' in entity['labels']:
            label = entity['labels']['en']['value']

        if 'descriptions' in entity and 'en' in entity['descriptions']:
            description = entity['descriptions']['en']['value']

    return {
        "ID": item_id,
        "LABEL": label,
        "DESCRIPTION": description,
    }