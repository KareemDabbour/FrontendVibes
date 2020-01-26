from flask import Flask, make_response, request
from player import Player


app = Flask(__name__)
player = Player()


@app.route('/play', methods=['POST'])
def play():
    if 'name' in request.args:
        if player.play(request.args['name']):
            return make_response('playing', 200)
        else:
            return make_response('failed to play {}'.format(request.args['name']), 400)
    elif 'url' in request.args:
        url = request.args['url']

        # handle URL with query parameters
        if 'Key-Pair-Id' in request.args:
            url += '&Key-Pair-Id=' + request.args['Key-Pair-Id']
        if 'Expires' in request.args:
            url += '&Expires=' + request.args['Expires']

        print('Using URL:', url)

        file_name = player.download(url)

        player.play(file_name)

        return make_response('playing downloaded file: {}'.format(file_name), 200)
    else:
        return make_response('you need to pass either name or url', 400)


@app.route('/stop', methods=['POST'])
def stop():
    player.stop()

    return make_response('Stopped playing', 200)


@app.route('/pause', methods=['POST'])
def pause():
    player.pause()

    return make_response('Paused', 200)


@app.route('/unpause', methods=['POST'])
def unpause():
    player.unpause()

    return make_response('Unpaused', 200)


@app.route('/status', methods=['GET'])
def status():
    if player.status():
        return make_response('Playing', 200)
    else:
        return make_response('Idle', 200)


@app.route('/download', methods=['POST'])
def download():
    if 'url' not in request.args:
        return make_response('Missing url argument', 400)
    else:
        url = request.args['url']

        if 'Key-Pair-Id' in request.args:
            url += '&Key-Pair-Id=' + request.args['Key-Pair-Id']
        if 'Expires' in request.args:
            url += '&Expires=' + request.args['Expires']

        file_name = player.download(url)

        return make_response('Downloaded file: {}'.format(file_name), 200)
