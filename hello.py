def application(env, start_response):
    q_string = env.get('QUERY_STRING')
    pairs_list = q_string.split("&")
    body = "\n".join(pairs_list).encode('utf-8')
    # for pair in pairs_list:
    #     body += pair + "\n"

    response_string = [('Content-type', 'text/plain')]

    start_response('200 OK', response_string)
    return [body]
