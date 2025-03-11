def extract_short_code(url):
    """Extract short code from either a full URL"""
    if url.startswith(('http://', 'https://')):
        # If it's a full URL, get everything after the domain
        without_protocol = url.split('://', 1)[1]
        # Get everything after the first slash (the path)
        path = without_protocol.split('/', 1)[1] if '/' in without_protocol else ''
        # Remove leading/trailing slashes and return
        return path.strip('/')

    # TODO: check if input is not a full URL
    # TODO: just passing in the 6 digit code
    

