import logging      # utilisé pour afficher des messages d'erreur au lieu
# de print


logging.basicConfig(level=logging.ERROR, format='%(levelname)s: %(message)s')
# formatage des messages d'erreur


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        logging.error('Invalid input: template must be a string')
        return
    if not isinstance(attendees, list) or not all(
        isinstance(a, dict) for a in attendees
    ):
        logging.error(
            'Invalid input: attendees must be a list of dictionaries.'
        )
        return

    if template.strip() == "":
        logging.error("Template is empty, no output files generated")
        return

    if not attendees:
        logging.error("No data provided, no output files generated")
        return

    for index, attendee in enumerate(attendees, start=1):
        copy = template                     # copie du modèle à modifier
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(key)
            copy = copy.replace(f'{{{key}}}', str(value) if value else 'N/A')
        try:
            with open(f'output_{index}.txt', 'w') as f:
                f.write(copy)
        except Exception as e:
            logging.error(f'Error writing file output_{index}.txt: {e}')
