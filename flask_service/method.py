from __future__ import division
from flaskdb import *


def calc_funcline(coord1, coord2):
    if coord2[0] != coord1[0]:
        m = (coord2[1] - coord1[1]) / float(coord2[0] - coord1[0])
        n = coord1[1] - m * coord1[0]
    else:
        print 'error'
    return m, n


def values_line(m, n, img_with):
    values = []
    for x in xrange(img_with):
        values.append(m * x + n)
    # print values
    return values


def pintar(img, num_left, num_right):
    m, n = calc_funcline(
        (num_left[0], num_left[1]), (num_right[0], num_right[1]))
    values = values_line(m, n, len(img[0, :]))
    y_len = len(img[:, 0])
    for x, y in enumerate(values):
        # print x, y
        if y <= y_len or y*(-1) <= y_len:
            img[int(y), x] = (255, 0, 0)
    # img[num_right + 1, y] = (255,0,0)
    # img[num_right - 1, y] = (255,0,0)
    return values


# def values_depth(line, limit, image, rango_min=[0, 0], h_min=-1):
#     depth = []
#     limit_tmp = limit
#     for x, y in enumerate(line):
#         flat = False
#         if x >= rango_min[0] and x <= rango_min[1]:
#             h = h_min
#         else:
#             h = -1
#         while not flat and h < limit_tmp and h >= -1:
#             if x >= rango_min[0] and x <= rango_min[1]:
#                 h -= 1
#             else:
#                 h += 1
#             # val = image[y + h, x]
#             # print y, h
#             val = image[int(y) + h, x]
#             if val == 255:
#                 around = redor(x, y + h, 2, 2, image)
#                 if around:
#                     flat = True
#         if flat:
#             depth.append(h + y)
#         else:
#             depth.append('nan')
#     # print depth
#     return depth


# def values_high(line, limit, image, rango_min=[0, 0], h_min=-1):
#     high = []
#     for x, y in enumerate(line):
#         flat = False
#         if x >= rango_min[0] and x <= rango_min[1]:
#             h = h_min
#         else:
#             h = -1
#         while not flat and h < limit:
#             h += 1
#             val = image[int(y) - h, x]
#             # print val
#             if val == 255:
#                 around = redor(x, y - h, 3, 3, image)
#                 if around:
#                     flat = True
#         if flat:
#             high.append(y - h)
#         else:
#             high.append('nan')
#     # print high
#     return high

# versao ate 9/1/2018 iniciava no estremos da imagem
# def values_depth(line, limit, image, rango_min=[0, 0], h_min=-1):
#     depth = []
#     limit_tmp = limit
#     for x, y in enumerate(line):
#         flat = False
#         if x >= rango_min[0] and x <= rango_min[1]:
#             h = h_min
#             limit_tmp = len(image[:, 0])
#         else:
#             h = -1
#             limit_tmp = limit
#         while not flat and h < limit_tmp and h >= -1:
#             if x >= rango_min[0] and x <= rango_min[1]:
#                 h -= 1
#             else:
#                 h += 1
#             # val = image[y + h, x]
#             if y + h < len(image[:, 0]):
#                 val = image[int(y) + h, x]
#                 # print int(y), h, val
#                 if val == 0:
#                     around = redor(x, y + h, 3, 3, image)
#                     if around:
#                         flat = True
#         if flat:
#             depth.append(h + y)
#         else:
#             depth.append('nan')
#     # print depth
#     return depth

def values_depth(line, limit, image, rangox, rango_min=[0, 0], h_min=-1, matrix_redor = [3,3]):
    depth = []
    limit = len(image[:, 0])
    for x in xrange(rangox[0], rangox[1]):
        flat = False
        y = int(line[x])
        if x >= rango_min[0] and x <= rango_min[1]:
            y += h_min        
        while not flat and y < limit:
            val = image[y, x]
            if val == 0:
                around = redor(x, y, matrix_redor[0], matrix_redor[1], image)
                if around:
                    flat = True
            y+=1
        if flat:
            depth.append(y - line[x])
        else:
            depth.append('nan')
    # print depth
    return depth    

# versao antes de 8/1/2018 iniciava na linea e sobe 
# def values_high(line, limit, image, rango_min=[0, 0], h_min=-1):
#     high = []
#     for x, y in enumerate(line):
#         flat = False
#         if x >= rango_min[0] and x <= rango_min[1]:
#             h = h_min
#         else:
#             h = -1
#         while not flat and h < limit:
#             h += 1
#             val = image[int(y) - h, x]
#             # print val
#             if val == 255:
#                 around = redor(x, y - h, 3, 3, image)
#                 if around:
#                     flat = True
#         if flat:
#             high.append(y - h)
#         else:
#             high.append('nan')
#     # print high
#     return high

def values_high(line, init_y, image, rangox, matrix_redor = [3,3]):
    high = []
    for x in xrange(rangox[0], rangox[1]):
        y = init_y
        flat = False
        # print y, line[x]
        while  not flat and y < line[x]:   
            val = image[y, x]
            if val == 0:
                around = redor(x, y, matrix_redor[0], matrix_redor[1], image)
                if around:
                    flat = True
            y+=1
        if flat:
            high.append(line[x] - y)
        else:
            high.append('nan')
    # print high
    return high    


def redor(realX, realY, dimX, dimY, image):
    cont0 = 0
    restaX = realX - dimX
    sumaX = realX + dimX
    if restaX < 0:
        restaX = 0
    if sumaX > len(image[0, :]):
        sumaX = len(image[0, :])

    restaY = realY - dimY
    sumaY = realY + dimY
    # print sumaY
    if restaY < 0:
        restaY = 0
    if sumaY > len(image[:, 0]):
        sumaY = len(image[:, 0])

    for x in xrange(restaX, sumaX):
        for y in xrange(int(restaY), int(sumaY)):
            # print 'y:', x
            if image[y, x] == 0:
                cont0 += 1
    if cont0 > (dimX + 0.5) * (dimY + 0.5):
        return True
    return False


def pintar2(img_original, img_filter, value_line, conf_depth, conf_high, flag_depth, flag_high, rangex):
    result = []
    if flag_depth:
        result = values_depth(
            value_line,
            conf_depth['limit'],
            img_filter,
            rangex,
            conf_depth['rango_min'],
            conf_depth['h_min'])
    if flag_high:    
        result = values_high(
            value_line,
            conf_high['init_y'],
            img_filter,
            rangex,
            conf_high['matrix_redor'])
    for x in xrange(rangex[0], rangex[1]):
        # print x, y
        img_original[int(value_line[x]), x] = (255, 0, 0)
        img_original[int(value_line[x]) - 1, x] = (255, 0, 0)
        img_original[int(value_line[x]) + 1, x] = (255, 0, 0)
        # print x, len(result), rangex[1]
        pos = x - rangex[0]
        if flag_depth and result[pos] != "nan":
            img_original[int(value_line[x] + result[pos]), x] = (0, 255, 0)
            img_original[int(value_line[x] + result[pos]) - 1, x] = (0, 255, 0)
            img_original[int(value_line[x] + result[pos]) + 1, x] = (0, 255, 0)
        if flag_high and result[pos] != "nan":
            img_original[int(value_line[x] - result[pos]), x] = (0, 255, 0)
            img_original[int(value_line[x] - result[pos]) - 1, x] = (0, 255, 0)
            img_original[int(value_line[x] - result[pos]) + 1, x] = (0, 255, 0)


    return result


def export_list(
        nameCSV,
        result,
        real_height_right,
        real_height_left,
        px_heightright,
        px_heightleft):
    data = open(nameCSV, 'w')
    for i, val in enumerate(result):
        coef = (real_height_right / px_heightright - real_height_left / \
                px_heightleft) / (0 - len(result)) * i + real_height_right / px_heightright
        if i != 0:
            data.write(',')
        # print type(val)
        if val != 'nan':
            res = coef * val   
            data.write(str(res))
        else:
            data.write('nan')
                
        # print((real_height_right / px_heightright ))
        # print(real_height_left / px_heightleft)
        # print(coef)
    data.close()


def save(
        nameCSV,
        result):
    data = open(nameCSV, 'w')
    for i, val in enumerate(result):
        if i != 0:
            data.write(',')
            data.write(str(val))
            #  print(coef)
    data.close()


def safe_parameter(slug, phase, img, param_list):
    img_db = session.query(Image).filter(Image.slug == slug)
    if phase is not None:
        img_db.update({"phase": phase})
    if img is not None:
        img_db.update(img)
    img_db = img_db.one()
    for row in param_list:
        para = session.query(Parameter).filter(
            Parameter.variable == row[0],
            Parameter.image_id == img_db.id)
        if para.count() > 0:
            para.update({'value': row[2]})
        else:
            session.add(
                Parameter(
                    variable=row[0],
                    type_variable=row[1],
                    value=row[2],
                    image_id=img_db.id))
    session.commit()
    session.close()


def get_parameter(slug, param):
    img_db = session.query(Image).filter(Image.slug == slug)
    img_db = img_db.one()
    para = session.query(Parameter).filter(
        Parameter.variable == param,
        Parameter.image_id == img_db.id)
    session.close()
    if para.count() > 0:
        return para.one()
    return 0

def get_file_parameter(nameCSV, slug):
    img_db = session.query(Image).filter(Image.slug == slug)
    img_db = img_db.one()
    param = session.query(Parameter).filter(
        Parameter.type_variable == 'int',
        Parameter.image_id == img_db.id).all()
    session.close()
    if len(param) > 0:
        data = open(nameCSV, 'w')
        for row in param:
            data.write(row.variable+' = '+row.value+" /n ")
        data.close()