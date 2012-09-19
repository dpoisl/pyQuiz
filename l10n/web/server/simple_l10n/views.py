import decimal
from django.shortcuts import render_to_response


def number(request, number="0"):
    return render_to_response("l10n/generic.tpl.html", 
                              {"value": decimal.Decimal(number)}, 
                              mimetype="text/plain")

