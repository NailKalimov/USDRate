from django.http import JsonResponse
from django_ratelimit.decorators import ratelimit
from django.shortcuts import render
from .models import Currency, CurrencyRate
from .utils import get_actual_rate_usd


def main_page(request):
    return render(request, 'main.html')


@ratelimit(key='ip', rate='1/10s', block=False)
def get_current_usd(request):
    if getattr(request, 'limited', False):
        return JsonResponse({'Error': 'Request limit exceeded, please try again in 10 seconds.'}, status=429)
    else:
        data = get_actual_rate_usd()
        usd_currency, _ = Currency.objects.get_or_create(code='USD', defaults={'name': 'US Dollar'})
        CurrencyRate.objects.create(
            currency=usd_currency,
            time=data['Date'],
            value=data['Valute']['USD']['Value']
        )
        last_ten_requests = CurrencyRate.objects.filter(currency=usd_currency).order_by('-time')[:10]
        res = {
            'Value': data['Valute']['USD']['Value'],
            'CurrentTime': data['Date'],
            'Last_10_Value': [
                {'Value': i.value, 'Time': i.time} for i in last_ten_requests
            ]
        }
        return JsonResponse(res, status=200)
