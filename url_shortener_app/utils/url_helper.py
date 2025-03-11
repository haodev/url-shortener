def extract_short_code(url_or_code):
    """Extract short code from either a full URL or just the 6 digit code"""
    if url_or_code.startswith(('http://', 'https://')):
        # If it's a full URL, get everything after the domain
        without_protocol = url_or_code.split('://', 1)[1]
        # Get everything after the first slash (the path)
        path = without_protocol.split('/', 1)[1] if '/' in without_protocol else ''
        # Remove leading/trailing slashes and return
        return path.strip('/')

    # TODO: check if input is not a full URL
    

