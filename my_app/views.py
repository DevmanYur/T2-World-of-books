from django.shortcuts import render


def index_page_1(request):

    # Словарь для передачи данных в шаблон
    index_page_1_head_zagolovok_page_1 = 'index_page_1_head_zagolovok_page_1'
    index_page_1_body_telo_page_1 = 'index_page_1_body_telo_page_1'
    context = {'index_page_1_head_zagolovok_page_1': index_page_1_head_zagolovok_page_1,
               'index_page_1_body_telo_page_1': index_page_1_body_telo_page_1}

    # передача словаря context с данными в шаблон
    return render(request, 'my_app/index_page_1.html', context)

def page_2(request):

    # Словарь для передачи данных в шаблон
    page_2_head_zagolovok_page_1 = 'page_2_head_zagolovok_page_1'
    page_2_body_telo_page_1 = 'page_2_body_telo_page_1'
    context = {'page_2_head_zagolovok_page_1': page_2_head_zagolovok_page_1,
               'page_2_body_telo_page_1': page_2_body_telo_page_1}

    # передача словаря context с данными в шаблон
    return render(request, 'my_app/page_2.html', context)

def page_3(request):

    # Словарь для передачи данных в шаблон
    page_3_head_zagolovok_page_1 = 'page_3_head_zagolovok_page_1'
    page_3_body_telo_page_1 = 'page_3_body_telo_page_1'
    context = {'page_3_head_zagolovok_page_1': page_3_head_zagolovok_page_1,
               'page_3_body_telo_page_1': page_3_body_telo_page_1}

    # передача словаря context с данными в шаблон
    return render(request, 'my_app/page_3.html', context)