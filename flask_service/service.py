from flask import Flask, request
from flask.json import jsonify
from flask_cors import CORS
import cv2
from method import *
import random
import string
import numpy as np


app = Flask(__name__)
CORS(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db.sqlite3'
# db = SQLAlchemy(app)


@app.route('/disenaralturas', methods=['POST', 'GET'])
def disenarAlturas():

    # print params['img']
    if request.method == 'POST':
        # path /static/media/images/...jpg
        params = request.json['params']
        path_img = '..' + params['img']
        img = cv2.imread(path_img, 1)
        # print params['y1']
        value_straight = pintar(img, (int(params['x1']),int(params['y1'])), (int(params['x2']), int(params['y2'])))

        name_hash = ''.join(
            random.choice(
                string.ascii_lowercase +
                string.digits) for x in range(5))

        paths = params['img'].split('.')
        new_img = paths[0] + name_hash + '_alturas.' + paths[1]
        new_img_save = '..' + new_img
        cv2.imwrite(new_img_save, img)

        list_params = [
            ('yl', 'int', params['y1']),
            ('yr', 'int', params['y2']),
            ('xl', 'int', params['x1']),
            ('hl', 'int', params['hl']),
            ('hr', 'int', params['hr']),
            ('xr', 'int', params['x2']),
            ('hrreal', 'int', params['hrreal']),
            ('hlreal', 'int', params['hlreal']) #,
            # ('hash', 'string', name_hash)
        ]
        safe_parameter(params['slug'], 1, {"img_diseno": new_img}, list_params)

        return new_img


@app.route('/filtrar', methods=['POST', 'GET'])
def filtrar():
    if request.method == 'POST':
        # imagen = Image.query.filter_by(img=request.data['img']).first()
        params = request.json['params']
        # path /static/media/images/...jpg
        path_img = '..' + params['img']
        img = cv2.imread(path_img, 1)
        Gauss_filtre = [int(params['Gauss_filtre']),
                        int(params['Gauss_filtre'])]
        thresh = [int(params['thresh1']), int(params['thresh2'])]
        kernel_dim = [int(params['kernel_dim']), int(params['kernel_dim'])]

        frame_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(frame_hsv)
        img = v
        img = cv2.GaussianBlur(v, (Gauss_filtre[0], Gauss_filtre[1]), 0)
        img = cv2.adaptiveThreshold(
            img,
            255,
            int(params['adaptive']),
            cv2.THRESH_BINARY,
            thresh[0],
            thresh[1])
        kernel = np.ones((kernel_dim[0], kernel_dim[1]), np.uint8)
        opening = cv2.morphologyEx(
            img, cv2.MORPH_OPEN, kernel, iterations=2)
        # sure background area
        img_filtrada = cv2.dilate(opening, kernel, iterations=3)

        # name_hash = get_parameter(params['slug'],'hash')
        # print name_hash.value
        name_hash = ''.join(
            random.choice(
                string.ascii_lowercase +
                string.digits) for x in range(5))

        paths = params['img'].split('.')
        new_img = paths[0] + name_hash + '_filtrada.' + paths[1]
        new_img_save = '..' + new_img
        cv2.imwrite(new_img_save, img_filtrada)
        # data = {'img_bordes': new_img}

        list_params = [
            ('Gauss_filtre', 'int', params['Gauss_filtre']),
            ('thresh1', 'int', params['thresh1']),
            ('thresh2', 'int', params['thresh2']),
            ('kernel_dim', 'int', params['kernel_dim']),
            ('adaptive', 'int', params['adaptive'])
        ]
        safe_parameter(
            params['slug'], 2, {
                "img_bordes": new_img}, list_params)

        return new_img


@app.route('/calcular', methods=['POST', 'GET'])
def calcular():
    if request.method == 'POST':
        # imagen = Image.query.filter_by(img=request.data['img']).first()
        params = request.json['params']
        # path /static/media/images/...jpg
        path_original = '..' + params['img_original']
        path_img = '..' + params['img']
        img = cv2.imread(path_img, 0)
        img_original = cv2.imread(path_original, 1)

        m, n = calc_funcline(
            (int(params['x1']), int(params['y1'])), (int(params['x2']), int(params['y2'])))
        values = values_line(m, n, len(img[0, :]))

        # name_hash = get_parameter(params['slug'],'hash')
        name_hash = ''.join(
            random.choice(
                string.ascii_lowercase +
                string.digits) for x in range(5))

        paths = params['img_original'].split('.')
        new_img = paths[0] + name_hash + '_calculado.' + paths[1]
        # print new_img
        new_img_save = '..' + new_img

        if params['detection'] == '0':
            conf_depth = {
                'limit': int(params['depth']),
                'rango_min': [
                    int(params['rango_depth1']),
                    int(params['rango_depth2'])],
                'h_min': int(params['max_depth'])}

            depth = pintar2(img_original, img, values, conf_depth, None, True, False, (int(params['x1']), int(params['x2'])))
            cv2.imwrite(new_img_save, img_original)

            list_params = [
                ('depth', 'int', params['depth']),
                ('rango_depth1', 'int', params['rango_depth1']),
                ('rango_depth2', 'int', params['rango_depth2']),
                ('max_depth', 'int', params['max_depth']),
                ('img_depth', 'url_img', new_img)
            ]
            safe_parameter(
                params['slug'], 3, {
                    "img_values": new_img, "bool_depth": True}, list_params)

            return jsonify(url = new_img, depth = depth)

        if params['detection'] == '1':
            conf_high = {
                'init_y': int(params['high']),
                'matrix_redor': [
                    int(params['matrix_redor']),
                    int(params['matrix_redor'])]}

            high = pintar2(img_original, img, values, None, conf_high, False, True, (int(params['x1']), int(params['x2'])))
            cv2.imwrite(new_img_save, img_original)

            list_params = [
                ('high', 'int', params['high']),
                ('matrix_redor', 'int', params['matrix_redor']),
                ('img_high', 'url_img', new_img)
            ]
            safe_parameter(
                params['slug'], 3, {
                    "img_values": new_img, "bool_high": True}, list_params)

            return jsonify(url = new_img, high = high)


@app.route('/export', methods=['POST', 'GET'])
def export():
    if request.method == 'POST':
        # imagen = Image.query.filter_by(img=request.data['img']).first()
        params = request.json['params']

        # name_hash = ''.join(
        #     random.choice(
        #         string.ascii_lowercase +
        #         string.digits) for x in range(5))

        paths = params['img'].split('.')
        list_params = [
                ('file_parameters', 'file_txt', paths[0]+'.txt')
            ]
        # safe_parameter(params['slug'],None, None, list_params)

        get_file_parameter('..'+paths[0]+'.txt', params['slug'])

        if params['detection'] == '0':
            name_depth = paths[0] + '_depth.csv'
            export_list('..'+name_depth, params['depth'], int(params['hrreal']), int(params['hlreal']), int(params['hr']), int(params['hl']))
            list_params += [
                ('list_depth', 'url_csv', name_depth)
            ]
            safe_parameter(params['slug'],None, None, list_params)     
            return jsonify(url_depth = name_depth, file_parameters = paths[0]+'.txt')

        if params['detection'] == '1':    
            name_high = paths[0] + '_high.csv'
            export_list('..'+name_high, params['high'], int(params['hrreal']), int(params['hlreal']), int(params['hr']), int(params['hl']))
            list_params += [
                ('list_high', 'url_csv', name_high)
            ]
            safe_parameter(params['slug'],None, None, list_params)     
            return jsonify(url_high = name_high, file_parameters = paths[0]+'.txt')


@app.after_request
def after_request(response):
    response.headers.add(
        'Access-Control-Allow-Origin',
        'http://localhost:5800')
    response.headers.add(
        'Access-Control-Allow-Headers',
        'Content-Type,Authorization')
    # response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    # response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response


if __name__ == "__main__":
    app.run()
