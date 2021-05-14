import xlwt


def write_data_to_wb(table_headers, files):
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('sheet')
    ws.col(4).width = 8888
    # 建立样式
    font_style = xlwt.XFStyle()
    # 设置字体的样式
    font_style.font.bold = True
    # 设置为水平居中
    # horz(水平居中)、vert(垂直居中)、rote(旋转方向45°)、shri(自动缩进)
    font_style.alignment.horz = 2
    for header_index, header in enumerate(table_headers):
        ws.write(0, header_index, header, font_style)

    row_num = 0
    for file in files:
        row_num += 1
        for file_index, detail in enumerate(file):
            try:
                ws.write(row_num, file_index, detail, font_style,)
            except:
                ws.write(row_num, file_index, 'xxl', font_style)

    return wb
