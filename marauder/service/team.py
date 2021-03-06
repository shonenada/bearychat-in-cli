# -*- coding: utf-8 -*-

from marauder.service.request import rqs, api_url, handle_response


def get_team(subdomain):
    url = api_url(subdomain, 'team')
    return handle_response(rqs.get(url))
