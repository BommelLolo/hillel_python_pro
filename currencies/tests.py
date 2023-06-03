# from datetime import timedelta
#
# import freezegun
# from django.utils import timezone
#
# from currencies.models import CurrencyHistory
# from currencies.tasks import get_currencies_task, set_currencies_task, \
#     delete_old_currencies
#
#
# def test_currencies(currency_history_factory, mocker):
#     mono_client = mocker.patch(
#         'currencies.clients.monobank.monobank_client.prepare_data'
#     )
#     assert mono_client.call_count == 0
#     mono_client.return_value = [
#         {'code': 'USD', "buy": "40.55000", "sale": "41.55000"},
#         {'code': 'EUR', "buy": "41.00000", "sale": "42.55000"},
#     ]
#     old = timezone.now() - timedelta(days=5)
#     with freezegun.freeze_time(old):
#         currency_history_factory()
#     assert CurrencyHistory.objects.filter(created_at__lte=old).exists()
#     for item in mono_client.return_value:
#         breakpoint()
#         assert CurrencyHistory.objects.filter(
#             code=item['code'],
#             buy=item['buy'],
#             sale=item['sale'],
#         ).exists()
#     delete_old_currencies()
#     assert not CurrencyHistory.objects.filter(created_at__lte=old).exists()
#     assert mono_client.call_count == 1
#     # breakpoint()
#     currency_history_factory()
#     for item in mono_client.return_value:
#         assert not CurrencyHistory.objects.filter(
#                 code=item['code'],
#                 buy=item['buy'],
#                 sale=item['sale'],
#         ).exists()


    # privat_client = mocker.patch('currencies.clients.privatbank.privatbank_client._prepare_data')
    # assert privat_client.call_count == 0
    # privat_client.return_value = [
    #     {'code': 'USD', "buy": "40.55000", "sale": "41.55000"},
    #     {'code': 'EUR', "buy": "41.00000", "sale": "42.55000"},
    # ]
    # old = timezone.now() - timedelta(minutes=10)
    # with freezegun.freeze_time(old):
    #     currency_history_factory()
    # assert CurrencyHistory.objects.filter(created_at__lte=old).exists()
    # get_currencies_task()
    # assert not CurrencyHistory.objects.filter(created_at__lte=old).exists()
    # assert privat_client.call_count == 1
    # for item in privat_client.return_value:
    #     assert CurrencyHistory.objects.filter(
    #         code=item['code'],
    #         buy=item['buy'],
    #         sale=item['sale'],
    #     ).exists()

    # nat_client = mocker.patch(
    #     'currencies.clients.nationbank.nationbank_client.prepare_data'
    # )
    # assert nat_client.call_count == 0
    # privat_client = mocker.patch(
    #     'currencies.clients.privatbank.privatbank_client.prepare_data'
    # )
    # assert privat_client.call_count == 0
    # nat_client.return_value = [
    #     {"r030": 840, "txt": "Долар США", "rate": 36.5686,
    #      "cc": "USD", "exchangedate": "04.05.2023"},
    #     {"r030": 978, "txt": "Євро", "rate": 40.3699,
    #      "cc": "EUR", "exchangedate": "04.05.2023"}
    # ]
    # privat_client.return_value = [
    #     {'code': 'USD', "buy": "40.55000", "sale": "41.55000"},
    #     {'code': 'EUR', "buy": "41.00000", "sale": "42.55000"},
    # ]