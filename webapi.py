import hug,tsx

@hug.get('/stocks_api')
def stocks_api(quote):
    # Return TSX Quote Info
    a = tsx.get_info(quote)
    if a != "Invalid Quote":
        return(tsx.get_info(quote))
    else:
        return(tsx.get_info(quote+':us'))
