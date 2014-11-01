import json
import traceback
from functools import wraps

from django.http import JsonResponse, Http404, HttpResponseForbidden

from apps.main.models import *
from libs.bank import BankApi, BankServerError


class Http403 (Exception):
    pass


def api(fx):
    @wraps(fx)
    def wrapper(request, **kwargs):
        body = {}
        if request.body:
            body = json.loads(request.body)
        kwargs.update(body)

        kwargs['client_id'] = request.session.get('client-id', None)

        status = 200

        try:
            response = fx(request, **kwargs)
        except Http403:
            return HttpResponseForbidden()
        except BankServerError as e:
            response = {
                'error': e.__class__.__name__,
                'error_reason': e.reason,
                'error_message': e.response,
            }
            status = 500
        except Exception as e:
            traceback.print_exc()
            response = {
                'error': e.__class__.__name__,
                'error_message': str(e),
            }
            status = 500

        return JsonResponse(response, safe=False, status=status)

    return wrapper


@api
def get_info(request, client_id=None):
    return {
        'client': BankApi().get_client(client_id),
    }


@api
def get_notifications(request, client_id=None):
    return [x.to_json() for x in Notification.objects.filter(client_id=client_id).all()]


@api
def erip_tree(request, client_id=None):
    return BankApi().get_erip_tree()


@api
def get_currency(request, client_id=None):
    return BankApi().get_currency_rates()


@api
def pay(request, client_id=None, accountId=None, 
    recipientBank=None, recipientId=None, recipientName=None, recipientAccountId=None, amount=None):
    client = BankApi().get_client(client_id)
    if not any(account['id'] == accountId for account in client['client']['accounts']):
        raise Exception('Invalid accountId')
    return BankApi().pay(accountId, recipientBank, recipientId, recipientName, recipientAccountId, amount)


@api
def change_password(request, client_id=None, client_id_to_change=None, old_password=None, new_password=None):
    if not BankApi().auth(client_id_to_change, old_password):
        raise Http403()
    return BankApi().change_password(client_id_to_change, new_password)
