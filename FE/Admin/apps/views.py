from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class AppsView(LoginRequiredMixin,TemplateView):
    pass

calendar_view = AppsView.as_view(template_name="apps/apps-calendar.html")

# chat
chat_view = AppsView.as_view(template_name="apps/chat/apps-chat.html")
chat_video_conference_chat_view = AppsView.as_view(template_name="apps/chat/apps-chat-video-conference.html")

# crypto
crypto_marketplace_view = AppsView.as_view(template_name="apps/crypto/apps-crypto-marketplace.html")
crypto_exchange_view = AppsView.as_view(template_name="apps/crypto/apps-crypto-exchange.html")
crypto_ico_view = AppsView.as_view(template_name="apps/crypto/apps-crypto-ico.html")
crypto_transactions_view = AppsView.as_view(template_name="apps/crypto/apps-crypto-transactions.html")
crypto_coin_overview_view = AppsView.as_view(template_name="apps/crypto/apps-crypto-coin-overview.html")

# customers
customers_list_view = AppsView.as_view(template_name="apps/customers/apps-customers-list.html")
customers_overview_view = AppsView.as_view(template_name="apps/customers/apps-customers-overview.html")

file_manager_view = AppsView.as_view(template_name="apps/apps-file-manager.html")

# invoices
invoices_list_view = AppsView.as_view(template_name="apps/invoices/apps-invoices-list.html")
invoices_create_view = AppsView.as_view(template_name="apps/invoices/apps-invoices-create.html")
invoices_overview_view = AppsView.as_view(template_name="apps/invoices/apps-invoices-overview.html")

notes_view = AppsView.as_view(template_name="apps/apps-notes.html")

to_do_view = AppsView.as_view(template_name="apps/apps-to-do.html")
