from decimal import Decimal
from django.shortcuts import render_to_response


def number(request, number="0"):
    try:
        value = int(number)
    except ValueError:
        value = Decimal(number)
    return render_to_response("l10n/generic.tpl.html", {"value": value}, 
                              mimetype="text/plain")

