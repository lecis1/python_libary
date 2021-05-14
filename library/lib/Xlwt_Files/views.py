from django.shortcuts import render, HttpResponse

import xlwt
from datetime import datetime

from utils import file_handler

# Create your views here.


def data_export(request):
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment;filename=history.xls'
    table_headers = ['用户名', '类型', '分类', '描述', '操作时间']
    files = [
        ['jack', '普通', '普通', '没有描述', '%s' % datetime.now()],
        ['lucy', '普通', '普通', '没有描述', '%s' % datetime.now()],
        ['andy', '普通', '普通', '没有描述', '%s' % datetime.now()],
        ]

    wb = file_handler.write_data_to_wb(table_headers, files)

    wb.save(response)

    return response
